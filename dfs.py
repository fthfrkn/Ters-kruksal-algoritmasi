class DepthFirstSearch:
        def __init__(self, G, s):
                self.marked = []
                self.cnt = 0
                for i in range(G.v()):
                        self.marked.append(False)
                self.dfs(G, s)

        def dfs(self, G, x):
               self.marked[x] = True
               self.cnt = self.cnt + 1
               w = G.adj[x]
               while w != None:
                      if not self.marked[w.key]:
                              self.dfs(G, w.key)
                      w = w.next

	def isMarked(self, w):
    		return self.marked[w]

	def count(self):
		return self.cnt

