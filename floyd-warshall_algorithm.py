#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = ["@alantsv", "@eltonpeniche"]

INF = float("inf")

class graph:
  vertex = ["1", "2", "3"]
  edge = {"1" : {"1" : 2, "2" : 8, "3" : 5},
          "2" : {"1" : 3},
          "3" : {"2" : 2}}
          
def _getPath(path, start, end, res):
  if start == end:
    return start + res
  return _getPath(path, start, path[end], end + res)

def getPath(path, start, end):
  return _getPath(path, start, end, "")
  
def floydWarshall(graph):
  distance = {}
  path = {}
  for v in graph.vertex:
    for w in graph.vertex:
      if v not in distance:
        distance[v] = {}
      if v == w:
        distance[v][w] = 0
      else:
        try:
          distance[v][w] = graph.edge[str(v)][str(w)]
        except:
          distance[v][w] = INF
  for k in graph.vertex:
    for v in graph.vertex:
      for w in graph.vertex:
        if distance[v][k] + distance[k][w] < distance[v][w]:
          distance[v][w] = distance[v][k] + distance[k][w]
          path[w] = k
  
  for i, j in distance.items():
    for k, w in j.items():
      if i != k:
        print("Cust of " + str(i) + " to " + str(k) + " = "+ str(w) +". Path: "+ getPath(path, i, k))


floydWarshall(graph)
