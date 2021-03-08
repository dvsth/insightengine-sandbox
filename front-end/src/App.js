import React, { useEffect, useState } from "react"
import { EntityContext } from "./EntityContext"

import ScrollerBox from "./ScrollerBox/ScrollerBox"

import "./App.scss"
import Funnel from "./Funnel/Funnel"

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
    let refresh = (funnel) => {
        fetch("http://localhost:5000/result",
            {
                method: "POST",
                body: JSON.stringify(funnel),
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
    const colors = ["#FEACD5", "#56CCF2", "#75D99F", "#BB6BD9", "#F2C94C", "#FC611E"]
    let test_entities = {
        0: { name: "Dev", color: colors[Math.floor(Math.random() * colors.length)] },
        1: { name: "Ashley", color: colors[Math.floor(Math.random() * colors.length)] },
        2: { name: "Bill", color: colors[Math.floor(Math.random() * colors.length)] },
        3: { name: "John", color: colors[Math.floor(Math.random() * colors.length)] },
    }
    let [entities, setEntities] = useState(test_entities);

    let [results, setResults] = useState(null);

    let [funnelItems, setFunnelItems] = useState({});

    function addToFunnel(entityIndex) {
        let newfunnel = { ...funnelItems, [entityIndex]: true }
        let x = Object.entries(newfunnel).filter(([index, bool]) => bool).map(([index, bool]) => index)
        refresh(x)
        setFunnelItems(newfunnel)
    }

    function removeFromFunnel(entityIndex) {
        setFunnelItems({ ...funnelItems, [entityIndex]: false })
    }

    return (
        <div id="App">
            <div className="heading">
                <div id="title">Poly-Association Sandbox</div>
                <div id="subtitle">Ashley Kwon, Dev Seth</div>
            </div>
            {entities &&
                <EntityContext.Provider value={entities}>
                    <div className="funnel-list-section">
                        <div id="scrollers">
                            <ScrollerBox onItemClick={addToFunnel} />
                        </div>
                        <div id="funnel">
                            <Funnel items={funnelItems} onItemClick={removeFromFunnel} />
                        </div>
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