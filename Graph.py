# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 16:28:57 2019
图
1、深度有限遍历
2、广度优先遍历
@author: Jason
"""

graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}
print(graph)

def bfs(graph, start):
    visited, queue = set(), [start]
    while queue:
        vertex = queue.pop(0)
        visited.add(vertex)
        queue.extend(graph[vertex]-visited)
    return visited


def dfs(graph, start):
    visited, stack = set(), [start]
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        stack.extend(graph[vertex]-visited)
    return visited        
    
    return visited

print(dfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}
print(bfs(graph, 'A')) # {'E', 'D', 'F', 'A', 'C', 'B'}