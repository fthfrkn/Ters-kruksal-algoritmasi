import weighted_graph
import dfs

class KruskalMSTReverse:
    def __init__(self, EWG):
        # mst oncelikle cizgedeki tum kenarlari icerir
        self.mst = EWG.edges()      # mst = [(v1, v2, weight), (v1, v2, weight), (), (), ....]
        self.pq = sorted(self.mst, reverse=True, key=lambda x: x[2])
               
        for i in range (len(self.pq)):
            # kenarlari buyukten kucuge dogru agirlik degerleriyle ele al.
            pivot_edge = self.pq[i]
            # Ele aldiginin kenar haric kalan kenarlarla bir yonlu olmayan cizge olustur.
            # Onde kenarsiz sadece dugumlerden olusan bir cizge yaratalim.
            g = weighted_graph.EdgeWeightedGraph(EWG.v())        
            # Simdi bu ara cizgemize o an icin mst'de olan kenarlari ekleyelim.    
            for edge in self.mst:
                if edge != pivot_edge:
                    g.addEdge(edge[0], edge[1], edge[2])
              
            # g uzerinde DFS ile gezinti yap.
            d = dfs.DepthFirstSearch(g, 0)
            # Eger g'nin tum dugumleri ziyaret edildiyse, g'de kesi (cut) yok demektir
            if self._isConnected(g, d):
                # Bu durumda olusmakta olan mst'den bu kenari cikartabiliriz.
                self.mst.remove(pivot_edge)
            else:
                # Aksi takdirde (cut varsa), kenari cikartamayiz, ayni mst ile devam
                continue            

    def _isConnected(self, g, d):
        for v in range(g.v()):
            if not(d.isMarked(v)):
                return False
        return True
        
    def edges(self):
        return self.mst

    def weight(self):
        weg = 0
        for e in self.mst:
            weg += e[2]
        return weg

mygraph = weighted_graph.EdgeWeightedGraph(8)
mygraph.addEdge(0, 1, 6)
mygraph.addEdge(0, 2, 12)
mygraph.addEdge(1, 2, 5)
mygraph.addEdge(1, 3, 14)
mygraph.addEdge(1, 4, 8)
mygraph.addEdge(3, 4, 3)
mygraph.addEdge(2, 5, 9)
mygraph.addEdge(2, 6, 7)
mygraph.addEdge(6, 7, 15)
mygraph.addEdge(4, 6, 10)

mst = KruskalMSTReverse(mygraph)
print(mst.mst)
print(mst.weight())

mygraph = weighted_graph.EdgeWeightedGraph(8)
mygraph.addEdge(1, 5, 32)
mygraph.addEdge(4, 5, 35)
mygraph.addEdge(5, 7, 28)
mygraph.addEdge(1, 7, 19)
mygraph.addEdge(4, 7, 37)
mygraph.addEdge(1, 3, 29)
mygraph.addEdge(1, 2, 36)
mygraph.addEdge(2, 7, 34)
mygraph.addEdge(0, 7, 16)
mygraph.addEdge(0, 4, 38)
mygraph.addEdge(3, 6, 52)
mygraph.addEdge(2, 3, 17)
mygraph.addEdge(2, 6, 40)
mygraph.addEdge(0, 2, 26)
mygraph.addEdge(0, 6, 58)
mygraph.addEdge(4, 6, 93)

mst = KruskalMSTReverse(mygraph)
print(mst.mst)
print(mst.weight())