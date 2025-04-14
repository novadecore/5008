|V| number of vertices
|E| number of edges

cardinality

degree:
in degree of a vertex v – The number of incoming edges; i.e., how many edges have v as their destination.
out degree of a vertex v – The number of outgoing edges; i.e., how many edges have v as their source.

```c
#include <stdio.h>
#include <limits.h>

#define V 100   // 最多支持 100 个节点
#define INF 1000000000

// 选出当前未访问节点中 dist 最小的点
int minDistance(int dist[], int visited[], int n) {
    int min = INF;
    int min_index = -1;
    for (int v = 0; v < n; v++) {
        if (!visited[v] && dist[v] < min) {
            min = dist[v];
            min_index = v;
        }
    }
    return min_index;
}

// Dijkstra 核心函数
void dijkstra(int graph[V][V], int src, int n) {
    int dist[V];     // 最短路径
    int visited[V];  // 是否访问过

    for (int i = 0; i < n; i++) {
        dist[i] = INF;
        visited[i] = 0;
    }
    dist[src] = 0;

    for (int count = 0; count < n - 1; count++) {
        int u = minDistance(dist, visited, n);
        if (u == -1) break;  // 没有可达点了
        visited[u] = 1;

        for (int v = 0; v < n; v++) {
            if (!visited[v] && graph[u][v] != INF &&
                dist[u] + graph[u][v] < dist[v]) {
                dist[v] = dist[u] + graph[u][v];
            }
        }
    }

    // 输出结果
    for (int i = 0; i < n; i++) {
        if (dist[i] == INF)
            printf("dist[%d] = INF\n", i);
        else
            printf("dist[%d] = %d\n", i, dist[i]);
    }
}
```