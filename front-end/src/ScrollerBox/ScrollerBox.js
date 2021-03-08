import React, { useContext } from "react"
import { EntityContext } from "../EntityContext"

import "./ScrollerBox.scss"

/**
 * 
 * @param {*} props int selected and function onChange(int newSelectionIndex) 
 */
export default function ScrollerBox(props) {

    const options = useContext(EntityContext);
    // console.log(options)
    return (
        <div className="scroller-box">
            {/* <div className="fade-box" id="top" /> */}
            <div className="items">
                <div className="spacer" />
                {Object.entries(options).map(([index, option]) =>
                    <Entity
                        id={index}
                        name={option.name}
                        color={option.color}
                        onClick={() => props.onItemClick(index)}
                    />
                )}
            </div>
            {/* <div className="fade-box" id="bottom" /> */}
        </div>
    )
}

// name, onclick
function Entity(props) {
    return (
        <div className={"entity" + (props.selected ? " selected" : "")}
            id={"entity" + props.id}
            onClick={props.onClick}
            style={{backgroundColor: props.color}}
        >
            {props.name}
        </div>
    )
}