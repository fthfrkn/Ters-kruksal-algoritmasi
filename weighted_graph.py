class EdgeWeightedGraph :
    class Node:
        def __init__(self, key, weight, next):
            self.key = key
            self.next = next
            self.weight = weight

    def __init__(self, V):
        self.V = V
        self.E = 0
        self.adj = []
        for i in range(V):
            self.adj.append(None)

    def v(self):
        return self.V

    def e(self):
        return self.E

    def addEdge(self, v1, v2, weight):
        self.adj[v1] = EdgeWeightedGraph.Node(v2, weight, self.adj[v1])
        self.adj[v2] = EdgeWeightedGraph.Node(v1, weight, self.adj[v2])
        self.E = self.E + 1

    def adjj(self, v):
        vv = self.adj[v]
        t = []
        while vv != None:
            # kenar temsil seklimiz (v, w, weight) tuple'i seklinde
            t.append((v, vv.key, vv.weight))
            vv = vv.next
        return t

    def edges(self):
        list =  []
        for v in range (self.V):
            selfLoops = 0
            komsu_kenarlar = self.adjj(v)
            for komsu_kenar in komsu_kenarlar:
                # Her bir kenarı sadece bir kez eklemek icin w > v kontrolu yapiyoruz.
                if komsu_kenar[1] > v:
                    list.append(komsu_kenar)
                # cizgede kendine donen kenarlar (w = v) da olabilir (self-loop), 
                # bu tip kenarlari da sadece bir kez eklemeliyiz
                elif (komsu_kenar[1] == v):
                    if (selfLoops % 2 == 0) :
                        list.append(komsu_kenar)
                    selfLoops += 1
        return list;

    def __str__(self):
        s = str(self.V) + " dugumler, " + str(self.E) + " kenarlar\n"
        for v in range(self.V):
            s = s + str(v) + ": "
            w = self.adj[v]
            while w != None:
                s = s + str(w.key) + " "
                w = w.next
            s = s + "\n"
        return s


if __name__ == "__main__":
    mygraph = EdgeWeightedGraph(5)
    mygraph.addEdge(0, 1, 10)
    mygraph.addEdge(0, 2, 8)
    mygraph.addEdge(0, 3, 6)
    mygraph.addEdge(1, 3, 12)
    mygraph.addEdge(2, 3, 4)
    mygraph.addEdge(3, 4, 1)
    mygraph.addEdge(1, 1, 3)

    #print (mygraph.adjj(0))
    print (mygraph)
    print ("---------------")
    print (mygraph.edges())