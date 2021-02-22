import networkx as nx
import matplotlib.pyplot as plt
from flask import Flask

app = Flask(__name__, instance_relative_config=True)
G = nx.DiGraph()

def start():
# Creates nodes and edges
    nodeNumbers = {'Consciousness': 0, 'Mind-body problem': 1, 'Descartes': 2, 'France': 3,
    'Voltaire': 4, 'Rousseau': 5, 'Enlightenment': 6, 'Romanticism': 7, 'Delacroix': 8, 'Napoleon': 9, 
    'Symbolism': 10, 'Satire': 11, 'Social Contract': 12, 'French Revolution': 13, 'Monarchy': 14, 
    'Imperialism': 15, 'Meditations': 16, 'Candide': 17, 'Liberty Leading the People': 18, 'Diderot': 19, 
    'Encyclopedia': 20, 'Haitian Revolution': 21, 'Conrad':22, 'Heart of Darkness': 23, 'Rococo': 24, 
    'Fragonard': 25}
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

# selected1 = nodeNumbers['Fragonard']
# selected2 = nodeNumbers['Meditations']
# returnShortestPath(selected1, selected2)
@app.route('/result', methods = ['POST'])
def result():
    start = request.json.start
    target = request.json.target

    print(request.json)
    # if player_id:
    #    data = get_player(player_id)
    #    name = str(data['name'][0])
    #    return jsonify(name)
   return "No player information is given"

    
# Displays the entire graph
# G.nodes.data()

