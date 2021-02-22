import React, { useCallback, useEffect, useState } from "react"
import { EntityContext } from "./EntityContext"

import ScrollerBox from "./ScrollerBox/ScrollerBox"

import "./App.scss"

export default function App(props) {

    // initial fetch of entities
    useEffect(
        () => {
            fetch("http://localhost:5000/entities").then(response => {
                console.log(response)
                return response.json()
            })
                .then(json => {
                    console.log(json)
                    setEntities(json)
                }).catch((error) => console.log(error))
        }
        , [])

    // get new results on each selection change event
    let refresh = (one, two) => {
        fetch("http://localhost:5000/result",
            {
                method: "POST",
                body: JSON.stringify({ start: one, target: two }),
                cache: "no-cache",
                headers: new Headers({
                    "content-type": "application/json"
                })
            }
        ).then(response => {
            return response.json()
        })
            .then(json => {
                setResults(json)
            })
    }

    // these store indexes into options array
    let [first, setFirst] = useState(0);
    let [second, setSecond] = useState(1);

    let [entities, setEntities] = useState(null);
    let [results, setResults] = useState(null);

    return (
        <div id="App">
            {entities &&
                <EntityContext.Provider value={entities}>
                    <div id="scrollers">
                        <ScrollerBox selected={first} onChange={(newItem) => {
                            setFirst(newItem)
                            refresh(newItem, second);
                        }} />
                        <ScrollerBox selected={second} onChange={(newItem) => {
                            setSecond(newItem)
                            refresh(first, newItem);
                        }} />
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
            }
        </div>
    )
}