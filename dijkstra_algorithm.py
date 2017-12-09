#!/usr/bin/env python3
# -*- coding: utf-8 -*-

__author__ = ["@alantsv", "@eltonpeniche"]

INF = float("inf")

class graph:
  vertex = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
  edge = {"A" : {"B" : 60, "C" : 54, "D" : 42},
          "B" : {"A" : 60, "F" : 29, "D" : 71},
          "C" : {"A" : 54, "E" : 67, "D" : 56},
          "D" : {"A" : 42, "B" : 71, "C" : 56, "F" : 52, "G" : 87, "E" : 26},
          "E" : {"C" : 67, "D" : 26, "G" : 70, "I" : 73},
          "F" : {"B" : 29, "D" : 52, "G" : 20, "H" : 25},
          "G" : {"D" : 87, "E" : 70, "F" : 20, "H" : 36, "I" : 32, "J" : 59},
          "H" : {"F" : 25, "G" : 36, "J" : 25},
          "I" : {"E" : 73, "G" : 59, "J" : 26},
          "J" : {"G" : 32, "H" : 25, "I" : 26}}

def getMin(nodes, distance):
  min = INF
  for node in nodes:
    if distance[node] < min:
      min = distance[node]
      vertex = node
      index = nodes.index(node)
  for i in range(len(nodes)):
    if nodes[i] == vertex:
      nodes.pop(i)
      return nodes, vertex
  return [], "nil"

def dijkstra(graph, start, end):
  distance = {}
  path = {}
  for node in graph.vertex:
    distance[node] = INF
    path[node] = -1
  
  distance[start] = 0
  
  nodes = graph.vertex
  
  while len(nodes) > 0:
    nodes, u = getMin(nodes, distance)
    for v, d in graph.edge[u].items():
      if distance[v] > distance[u] + d:
        distance[v] = distance[u] + d
        path[v] = u
        nodes.append(v)
  
  finale = path[end]
  res = ""
  
  while finale != start:
    res = finale + res
    finale = path[finale]
  return start + res + end, distance[end]
  

print("Minimum distance of A to I: {0}.\nCust = {1}".format(*dijkstra(graph, "A", "I")))

