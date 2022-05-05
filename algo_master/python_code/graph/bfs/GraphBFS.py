from collections import deque

from python_code.graph.AdjSet import AdjSet
from python_code.graph.direct.GraphImpl import GraphImpl


class GraphBFS:
    def __init__(self, g: AdjSet):
        if g is None:
            return
        self.g = g
        self.res = []
        self.visited = [False] * self.g.getV()
        for v in range(self.g.getV()):
            if not self.visited[v]:
                self.bfs(v)

    def bfs(self, v):
        if self.g is None:
            return
        queue = deque()
        queue.append(v)
        self.visited[v] = True
        while len(queue):
            curr = queue.popleft()
            self.res.append(curr)
            for w in self.g.adj(curr):
                if not self.visited[w]:
                    queue.append(w)
                    self.visited[w] = True

    def getRes(self):
        return self.res


if __name__ == '__main__':
    g = GraphBFS("D:\install by myself\BaiduNetdiskDownload\新建文件夹(桌面)\深度学习总结系列\douma-algo-master\data\graph-dfs.txt")
    graphBFS = GraphBFS(g)
    print(graphBFS.getRes())
