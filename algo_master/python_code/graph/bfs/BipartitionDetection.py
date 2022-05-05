from collections import deque

from python_code.graph.AdjSet import AdjSet


class BipartitionDetection:
    def __init__(self, g: AdjSet):
        if g is None:
            return
        #属性设置
        self.g = g
        #0:红 1:蓝色
        self.visited = [False] * self.g.getV()
        self.colors = [-1] * self.g.getV()
        #
        self.isBipartition = True
        for v in range(self.g.getV()):
            if not self.visited[v]:
                if not self.bfs(v):
                    self.isBipartition=False
                    break

    def bfs(self, v):
        if self.g is None:
            return True
        queue = deque()
        queue.append(v)
        self.visited[v] = True
        self.colors[v] = 0
        while len(queue):
            curr = queue.popleft()
            for w in self.g.adj(curr):
                # 如果 w 没有遍历过，则需要染色
                if not self.visited[w]:
                    queue.append(w)
                    self.visited[w] = True
                    # 给顶点 w 染色，和 curr 的颜色不一样
                    self.colors[w] = 1 - self.colors[curr]
                elif self.colors[w] == self.colors[curr]:
                    # 如果 w 被访问过，并且它的颜色和相邻点一样
                    # 那么可以判定不是二分图
                    return False
        return True

    def getIsBipartition(self):
        return self.isBipartition


if __name__ == '__main__':
    g = AdjSet("D:\install by myself\BaiduNetdiskDownload\新建文件夹(桌面)\深度学习总结系列\douma-algo-master\data\graph-bfs.txt")
    graphBFS = BipartitionDetection(g)
    print(graphBFS.getIsBipartition())
