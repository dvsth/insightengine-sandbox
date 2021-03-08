import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask, jsonify
from flask import request
from flask_cors import CORS
from random import random

app = Flask(__name__, instance_relative_config=True)
CORS(app)

class entity:
    def __init__(self, id, name):
        self.id = id
        self.name = name

G = nx.DiGraph()
nodeNumbers = {'Consciousness': 0, 'Mind-body problem': 1, 'Descartes': 2, 'France': 3,
    'Voltaire': 4, 'Rousseau': 5, 'Enlightenment': 6, 'Romanticism': 7, 'Delacroix': 8, 'Napoleon': 9, 
    'Symbolism': 10, 'Satire': 11, 'Social Contract': 12, 'French Revolution': 13, 'Monarchy': 14, 
    'Imperialism': 15, 'Meditations': 16, 'Candide': 17, 'Liberty Leading the People': 18, 'Diderot': 19, 
    'Encyclopedia': 20, 'Haitian Revolution': 21, 'Conrad':22, 'Heart of Darkness': 23, 'Rococo': 24, 
    'Fragonard': 25}




# Creates nodes and edges
    
    # G = nx.DiGraph()

for key in nodeNumbers.keys():
    G.add_node(nodeNumbers[key], label = key)

G.add_edge(nodeNumbers['Mind-body problem'], nodeNumbers['Descartes'], label = 'research topic of')
G.add_edge(nodeNumbers['Descartes'], nodeNumbers['Mind-body problem'], label = 'contributed to')

G.add_edge(nodeNumbers['Consciousness'], nodeNumbers['Descartes'], label = 'research topic of')
G.add_edge(nodeNumbers['Descartes'], nodeNumbers['Consciousness'], label = 'studied')

G.add_edge(nodeNumbers['Descartes'], nodeNumbers['Meditations'], label = 'wrote')
G.add_edge(nodeNumbers['Meditations'], nodeNumbers['Descartes'],label = 'work of')

G.add_edge(nodeNumbers['Rousseau'], nodeNumbers['Voltaire'], label = 'contemporary')
G.add_edge(nodeNumbers['Voltaire'], nodeNumbers['Rousseau'], label = 'commented on')

G.add_edge(nodeNumbers['Voltaire'], nodeNumbers['France'], label = 'citizen of')
G.add_edge(nodeNumbers['France'], nodeNumbers['Voltaire'], label = 'home country of')

G.add_edge(nodeNumbers['Rousseau'], nodeNumbers['France'], label = 'citizen of')
G.add_edge(nodeNumbers['France'], nodeNumbers['Rousseau'], label = 'home country of')

G.add_edge(nodeNumbers['Rousseau'], nodeNumbers['Enlightenment'], label = 'participated in')
G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['Rousseau'], label = 'inspired')

G.add_edge(nodeNumbers['Voltaire'], nodeNumbers['Enlightenment'], label = 'participated in')
G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['Voltaire'], label = 'inspired')

G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['France'], label = 'location')
G.add_edge(nodeNumbers['France'], nodeNumbers['Enlightenment'], label = 'intellectual history')

G.add_edge(nodeNumbers['Mind-body problem'], nodeNumbers['Enlightenment'], label = 'discussed in')
G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['Mind-body problem'], label = 'subtopic')

G.add_edge(nodeNumbers['Rousseau'], nodeNumbers['Social Contract'], label = 'addressed')
G.add_edge(nodeNumbers['Social Contract'], nodeNumbers['Rousseau'], label = 'inspired')

G.add_edge(nodeNumbers['Voltaire'], nodeNumbers['Social Contract'], label = 'addressed')
G.add_edge(nodeNumbers['Social Contract'], nodeNumbers['Voltaire'], label = 'inspired')

G.add_edge(nodeNumbers['Voltaire'], nodeNumbers['Candide'], label = 'wrote')
G.add_edge(nodeNumbers['Candide'], nodeNumbers['Voltaire'],  label = 'work of')

G.add_edge(nodeNumbers['Satire'], nodeNumbers['Candide'], label = 'example')
G.add_edge(nodeNumbers['Candide'], nodeNumbers['Satire'],  label = 'genre')

G.add_edge(nodeNumbers['Candide'], nodeNumbers['Imperialism'],  label = 'topic')
G.add_edge(nodeNumbers['Imperialism'], nodeNumbers['Candide'],  label = 'influenced')

G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['Romanticism'], label = 'inspired')
G.add_edge(nodeNumbers['Romanticism'], nodeNumbers['Enlightenment'], label = 'opposed ideas from')

G.add_edge(nodeNumbers['Romanticism'], nodeNumbers['Delacroix'], label = 'influenced')
G.add_edge(nodeNumbers['Delacroix'], nodeNumbers['Romanticism'],  label = 'participated in')

G.add_edge(nodeNumbers['Delacroix'], nodeNumbers['French Revolution'],  label = 'painting subject')
G.add_edge(nodeNumbers['French Revolution'], nodeNumbers['Delacroix'],  label = 'inspired')

G.add_edge(nodeNumbers['Monarchy'], nodeNumbers['French Revolution'],  label = 'caused')
G.add_edge(nodeNumbers['French Revolution'], nodeNumbers['Monarchy'], label = 'opposed')

G.add_edge(nodeNumbers['Delacroix'],  nodeNumbers['Symbolism'], label = 'contributed to')
G.add_edge(nodeNumbers['Symbolism'], nodeNumbers['Delacroix'],  label = 'derived ideas from')

G.add_edge(nodeNumbers['Delacroix'], nodeNumbers['Liberty Leading the People'], label = 'painted')
G.add_edge(nodeNumbers['Liberty Leading the People'], nodeNumbers['Delacroix'], label = 'work of')

G.add_edge(nodeNumbers['French Revolution'], nodeNumbers['Liberty Leading the People'], label = 'topic of')
G.add_edge(nodeNumbers['Liberty Leading the People'], nodeNumbers['French Revolution'], label = 'depicts')

G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['French Revolution'], label = 'contributed to')
G.add_edge(nodeNumbers['French Revolution'], nodeNumbers['Enlightenment'], label = 'derived ideas from')

G.add_edge(nodeNumbers['French Revolution'], nodeNumbers['France'], label = 'location')
G.add_edge(nodeNumbers['France'], nodeNumbers['French Revolution'], label = 'historical event')

G.add_edge(nodeNumbers['Napoleon'], nodeNumbers['French Revolution'], label = 'cause of')
G.add_edge(nodeNumbers['French Revolution'], nodeNumbers['Napoleon'], label = 'undone by')

G.add_edge(nodeNumbers['Napoleon'], nodeNumbers['Imperialism'], label = 'participated in')
G.add_edge(nodeNumbers['Imperialism'], nodeNumbers['Napoleon'], label = 'influenced')

G.add_edge(nodeNumbers['Diderot'], nodeNumbers['Enlightenment'], label = 'participated in')
G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['Diderot'], label = 'inspired')

G.add_edge(nodeNumbers['Diderot'], nodeNumbers['Encyclopedia'], label = 'wrote')
G.add_edge(nodeNumbers['Encyclopedia'], nodeNumbers['Diderot'], label = 'work of')

G.add_edge(nodeNumbers['Imperialism'], nodeNumbers['Haitian Revolution'], label = 'caused')
G.add_edge(nodeNumbers['Haitian Revolution'], nodeNumbers['Imperialism'], label = 'opposed')

G.add_edge(nodeNumbers['Imperialism'], nodeNumbers['Conrad'], label = 'influenced')
G.add_edge(nodeNumbers['Conrad'], nodeNumbers['Imperialism'], label = 'commented on')

G.add_edge(nodeNumbers['Conrad'], nodeNumbers['Heart of Darkness'], label = 'wrote')
G.add_edge( nodeNumbers['Heart of Darkness'], nodeNumbers['Conrad'], label = 'work of')

G.add_edge(nodeNumbers['Rococo'], nodeNumbers['Enlightenment'], label = 'influenced')
G.add_edge(nodeNumbers['Enlightenment'], nodeNumbers['Rococo'], label = 'opposed')

G.add_edge(nodeNumbers['Fragonard'], nodeNumbers['Rococo'], label = 'contributed to')
G.add_edge(nodeNumbers['Rococo'], nodeNumbers['Fragonard'], label = 'inspired')

G.add_edge(nodeNumbers['Fragonard'], nodeNumbers['Monarchy'], label = 'worked for')
G.add_edge(nodeNumbers['Monarchy'], nodeNumbers['Fragonard'], label = 'favored')


# returnShortestPath returns a list that shows nodes and edge labels in the shortest path from selected1 to selected2
def returnShortestPath(selected1, selected2):
    ret = []
    shortestPath = nx.shortest_path(G, source = selected1, target = selected2)
    keys = list(nodeNumbers.keys())
    for i in range(len(shortestPath)-1):
        node = shortestPath[i]
        nextNode = shortestPath[i+1]
        sentence = keys[node] + " " + G.get_edge_data(node, nextNode)['label'] + " " + keys[nextNode]
        ret.append(sentence)
    print(ret)
    return ret


# returnPolyAssociation takes every ordered pair of inputs in inputList, 
# finds the shortest between two nodes in each pair,
# and returns a list that contains strings in which all nodes and edge labels between the two nodes are converted to somewhat sentences
@app.route('/result', methods = ['POST'])
def returnPolyAssociation(inputList):
    for edge in G.edges():
        G[edge[0]][edge[1]]['weight'] = 1
    mst = nx.algorithms.minimum_spanning_tree(G.to_undirected())
    shortestPathEdges = []
    shortestPathEdgesFlipped = []
    for i in range(len(inputList) - 1):
        source = nodeNumbers[inputList[i]]
        target = nodeNumbers[inputList[i+1]]
        shortestPath = nx.shortest_path(mst, source = source, target = target)
        shortestPathFlipped = nx.shortest_path(mst, source = target, target = source)

        for j in range(len(shortestPath) - 1):
            originalEdge = (shortestPath[j], shortestPath[j + 1])
            shortestPathEdges.append(originalEdge)
        
        for k in range(len(shortestPathFlipped) - 1):
            originalEdgeFlipped = (shortestPathFlipped[k], shortestPathFlipped[k + 1])
            shortestPathEdgesFlipped.append(originalEdgeFlipped)

    associations = []
    combined = shortestPathEdges + shortestPathEdgesFlipped
    nodeNumbersKeys = list(nodeNumbers.keys())
    for i in range(len(combined)-1):
        edge = combined[i]
        node1 = nodeNumbersKeys[edge[0]]
        node2 = nodeNumbersKeys[edge[1]]
        associations.append(node1 + " " + G.get_edge_data(edge[0], edge[1])['label'] + " " + node2) 
    return jsonify(associations)


@app.route('/entities')
def entities():
    alreadyGenerated = []
    colors = ["#FEACD5", "#56CCF2", "#75D99F", "#BB6BD9", "#F2C94C", "#FC611E"]
    entities = dict()
    for nodeName in list(nodeNumbers.keys()):
        nodeId = nodeNumbers[nodeName]
        color = random.choice(colors)
        entities[nodeId] = {"name": nodeName, "color": color}
    return jsonify(entities)

if __name__=="__main__":
    returnPolyAssociation(['Consciousness', 'Delacroix', 'Napoleon', 'Descartes'])

# selected1 = nodeNumbers['Fragonard']
# selected2 = nodeNumbers['Meditations']
# returnShortestPath(selected1, selected2)
# @app.route('/result', methods = ['POST'])
# def result():
#     json1 = request.get_json()
#     print(json1)
#     start = json1["start"]
#     target = json1["target"]
#     print(start, type(start))
#     ret = returnShortestPath(start, target)
#     return jsonify(ret) 


# @app.route('/entities')
# def entities():
#     return jsonify(list(nodeNumbers.keys()))

# Displays the entire graph
# G.nodes.data()
