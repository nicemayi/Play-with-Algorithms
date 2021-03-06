from collections import deque


class ShortestPath:
    def __init__(self, graph, s):
        self._G = graph
        assert 0 <= s < self._G.V()
        # s是从哪里起步
        self._s = s
        self._from = [-1] * self._G.V()
        self._visited = [False] * self._G.V()
        # order数组记录从s到每一个点的距离
        self._ord = [-1] * self._G.V()
        self._bfs()

    def has_path(self, w):
        """从s到w有没有路径"""
        assert 0 <= w < self._G.V()
        return self._visited[w]

    def path(self, w):
        """从s到w点的路径"""
        assert 0 <= w < self._G.V()
        s = []
        p = w
        while p != -1:
            s.append(p)
            p = self._from[p]
        return s

    def show_path(self, w):
        """打印从s到w点的路径"""
        vec = self.path(w)
        print('start ' +  ' -> '.join(str(i) for i in vec[::-1]) + ' end')

    def length(self, w):
        assert 0 <= w < self._G.V()
        return self._ord[w]

    def _bfs(self):
        queue = deque()
        queue.append(self._s)
        self._visited[self._s] = True
        while queue:
            curr = queue.popleft()
            for i in self._G[curr]:
                if not self._visited[i]:
                    queue.append(i)
                    self._visited[i] = True
                    self._from[i] = curr
                    self._ord[i] = self._ord[curr] + 1
