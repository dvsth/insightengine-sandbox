import React, { useContext } from "react"
import { DragDropContext, Droppable, Draggable } from 'react-beautiful-dnd';

import { EntityContext } from "../EntityContext"

import "./List.scss"

// props
//  items -> array of items
export default function List(props) {
    let entities = useContext(EntityContext);
    return (
        <Droppable droppableId={props.listID}>
            {(provided) =>
            (
                <div className="list" ref={provided.innerRef} {...provided.droppableProps}>
                    {
                        entities.map((option, index) =>
                            <ListItem
                                key={index}
                                id={index}
                                name={option}
                                onClick={() => props.onChange(index)}
                                selected={index === props.selected}
                            />
                        )}
                    {provided.placeholder}
                </div>
            )
            }
        </Droppable>
    )
}

export function ListItem(props) {

    const colors = ["#FEACD5", "#56CCF2", "#75D99F", "#BB6BD9", "#F2C94C", "#FC611E"]

    return (
        <Draggable draggableId={"draggable" + props.id} index={props.id}>
            {(provided) => (
                <div className="list-item" key={props.id} ref={provided.innerRef} {...provided.draggableProps} {...provided.dragHandleProps}
                    // style={{ backgroundColor: colors[Math.floor(Math.random() * colors.length)] }}
                >
                    {props.name}
                </div>
            )}
        </Draggable>
    )
}
