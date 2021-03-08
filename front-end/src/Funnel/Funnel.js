import React, { useContext } from "react"
import { EntityContext } from "../EntityContext"
import "./Funnel.scss"

export default function Funnel(props) {
    let entities = useContext(EntityContext)
    return (
        <div className="funnel">
            {Object.entries(props.items).map(([index, item]) =>
                item ?
                    <FunnelItem key={index} id={index} name={entities[index].name} color={entities[index].color} onClick={() => props.onItemClick(index)} />
                    : null
            )}
        </div>
    )
}

function FunnelItem(props) {
    return (
        <div className="funnel-item" id={props.id} onClick={props.onClick} style={{backgroundColor: props.color}}>
            {props.name}
        </div>
    )
}