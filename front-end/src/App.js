import React, { useEffect, useState } from "react"
import { EntityContext } from "./EntityContext"

import ScrollerBox from "./ScrollerBox/ScrollerBox"

import "./App.scss"

export default function App(props) {

    // initial fetch of entities
    useEffect(
        () => {
            fetch("/entities").then(response => {

                return response.json()
            })
                .then(json => {
                    console.log(json)
                    setEntities(json[0])
                })
        }
    )

    // get new results on each selection change event
    useEffect(() => {
        fetch("/result", {
            method: "POST",
            body: { start: first, target: second }
        }
        ).then(response => {

            return response.json()
        })
            .then(json => {
                setResults(json[0])
            })
    }, [first, second])

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
                        <ScrollerBox selected={first} onChange={(newItem) => setFirst(newItem)} />
                        <ScrollerBox selected={second} onChange={(newItem) => setSecond(newItem)} />
                    </div>
                    <div id="results">
                        {results && results.map((sentence) => {
                            <p>{sentence}</p>
                        })}
                    </div>
                </EntityContext.Provider>
            }
        </div>
    )
}