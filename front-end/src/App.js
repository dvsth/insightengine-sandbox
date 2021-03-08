import React, { useEffect, useState } from "react"
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

import { EntityContext } from "./EntityContext"
import ScrollerBox from "./ScrollerBox/ScrollerBox"

import "./App.scss"
import List from "./List/List";

export default function App(props) {

    // initial fetch of entities
    // useEffect(
    //     () => {
    //         fetch("http://localhost:5000/entities").then(response => {
    //             console.log(response)
    //             return response.json()
    //         })
    //             .then(json => {
    //                 console.log(json)
    //                 setEntities(json)
    //             }).catch((error) => console.log(error))
    //     }
    //     , [])

    // // get new results on each selection change event
    // let refresh = (one, two) => {
    //     fetch("http://localhost:5000/result",
    //         {
    //             method: "POST",
    //             body: JSON.stringify({ start: one, target: two }),
    //             cache: "no-cache",
    //             headers: new Headers({
    //                 "content-type": "application/json"
    //             })
    //         }
    //     ).then(response => {
    //         return response.json()
    //     })
    //         .then(json => {
    //             setResults(json)
    //         })
    // }

    // these store indexes into options array
    let [first, setFirst] = useState(0);
    let [second, setSecond] = useState(1);

    let [entities, setEntities] = useState(["Dev", "Ashley", "Bill"]);
    let [results, setResults] = useState(null);


    const reorder = (list, startIndex, endIndex) => {
        const result = Array.from(list);
        const [removed] = result.splice(startIndex, 1);
        result.splice(endIndex, 0, removed);

        return result;
    };
    
    const copy = (source, destination, droppableSource, droppableDestination) => {
        const sourceClone = Array.from(source);
        const destClone = Array.from(destination);
        const item = sourceClone[droppableSource.index];

        destClone.splice(droppableDestination.index, 0, { ...item, id: uuid() });
        return destClone;
    };

    const move = (source, destination, droppableSource, droppableDestination) => {
        const sourceClone = Array.from(source);
        const destClone = Array.from(destination);
        const [removed] = sourceClone.splice(droppableSource.index, 1);

        destClone.splice(droppableDestination.index, 0, removed);

        const result = {};
        result[droppableSource.droppableId] = sourceClone;
        result[droppableDestination.droppableId] = destClone;

        return result;
    };


    function handleOnDragEnd(result) {
        if (!result.destination) return;

        const items = Array.from(characters);
        const [reorderedItem] = items.splice(result.source.index, 1);
        items.splice(result.destination.index, 0, reorderedItem);
        setEntities(items);
    }

    return (
        <div id="App">
            <div className="heading">
                <div id="title">Poly-Association Sandbox</div>
                <div id="subtitle">Insight Engine</div>
            </div>
            <EntityContext.Provider value={entities}>
                <div id="scrollers">
                    <DragDropContext>
                        <List listID={"abc1"} />
                    </DragDropContext>
                </div>
                <div id="results">
                    <ol>
                        {results ? results.map((sentence) =>
                            <li>{sentence}</li>
                        )
                            : null
                        }
                    </ol>
                </div>
            </EntityContext.Provider>
        </div>
    )
}