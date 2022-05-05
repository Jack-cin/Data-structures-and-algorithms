from python_code.graph.AdjSet import AdjSet


class GraphDFS:
    def __init__(self, g: AdjSet):
        if g is None:
            return
        self.g = g
        # self.visited 用于防止一个节点被重复访问
        self.res, self.visited = [], [False] * self.g.getV()
        # 遍历图中每个顶点
        for v in range(self.g.getV()):
            # 先判断，没有遍历的顶点才能进行深度优先遍历
            if not self.visited[v]:
                self.dfs(v)

    # 时间复杂度：O(V)
    # 空间复杂度：O(V)
    def dfs(self, v):
        stack, self.visited[v] = [v], True
        while len(stack):
            curr = stack.pop()
            self.res.append(curr)
            for w in self.g.adj(curr):#注：升序入，降序出
                # 如果已经访问过了，就不压入栈，就不会再次访问了
                if not self.visited[w]:
                    stack.append(w)
                    self.visited[w] = True

    def getRes(self):
        return self.res


if __name__ == '__main__':
    adjSet = AdjSet("D:\install by myself\BaiduNetdiskDownload\新建文件夹(桌面)\深度学习总结系列\douma-algo-master\data\graph-dfs.txt")
    graphDFS = GraphDFS(adjSet)
    print(graphDFS.getRes())
