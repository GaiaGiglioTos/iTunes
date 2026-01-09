import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._grafo = nx.Graph()
        self._idMap = {}

    def build_graph(self,d):
        album = DAO.getAlbum(d)
        self._grafo.add_nodes_from(album)
        for a in album:
            self._idMap[a.AlbumId] = a

        archi = DAO.getArchi(self._idMap)
        for a in archi:
            self._grafo.add_edge(a[0],a[1])

    def getNumNodi(self):
        return self._grafo.number_of_nodes()

    def getNumArchi(self):
        return self._grafo.number_of_edges()

    def getInfoConnessa(self,n):
        cc = nx.node_connected_component(self._grafo,n)
        durata = 0
        for c in cc:
            t = DAO.getDurata(c.AlbumId)
            durata += t
        return len(cc), durata
