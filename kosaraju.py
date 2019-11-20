#!/usr/bin/python
from collections import deque
import sys
"""
Kosaraju's algorithm to find strongly-connected components of a 
directed graph.

Strongly-connected component of a graph G:- set of nodes S, such that between any nodes u,v in the set
                                            path exists from u->v & v->u
"""

# dfs implementation using stack
def dfs(G,V,loop):
    """ G should be an adjacency list - a dictionary """
    dfs_order = []
    global visited,fin_times,t,scc
    
    scc[V] = [V];
    visited[V] = 1 # Mark starting node as visited
    dfs_order.append(V)
    stack = deque(); # initialise stack for dfs
    stack.append(V)

    while len(stack) > 0:
        head = stack.pop()
        
        for tail in G[head]:
            if visited[tail] == 0:
                visited[tail] = 1 # mark as explored
                if loop == 2:
                    scc[V].append(tail)
                else:
                    dfs_order.append(tail) # used to print the dfs visited order
                stack.append(tail) # push into stack
                
    # compute finish times
    if loop == 1: # first dfs loop in kosaraju
        l = len(dfs_order)
        for i in range(l-1,-1,-1) :
            t=t+1
            fin_times[dfs_order[i]] = t
        
    return

def kosaraju(G):
    """
    dfs in run twice.
    1st dfs computes finish times for each of the nodes in the edge-reverse graph - dict{finish time:orig node}
    2nd dfs computes the scc components - stored as dict{leadernode:[scc nodes]}
    """
    # compute the edge-reverse graph from G - O(m)
    #R = {x:[] for x in range(1,len(G)+1)}
    R={}
    for (head,tails) in G.items():
        for tail in tails:
            if tail in R:
                R[tail].append(head)
            else:
                R[tail] = [head]

    # print reverse graph - testing
    #print(R)

    global visited,fin_times,t,scc # global vars
    visited = {x:0 for x in range(1,len(G)+1)} # dict marking visited/unvisited nodes, # 1- visited, 0- not visited
    fin_times = {};t=0;scc={};

    # 1st dfs run in kosaraju
    for node in range(len(G),0,-1):
        if node in R and visited[node] == 0:
            dfs(R,node,loop=1)

    # 2nd dfs run in kosaraju
    # re-labeling the nodes based on fin_times in the graph
    scc={}
    G1 = {x:[] for x in range(1,len(G)+1)}
    for (head,tails) in G.items():
        for tail in tails:
            G1[fin_times[head]].append(fin_times[tail])
            
    visited = {x:0 for x in range(1,len(G)+1)} # dict marking visited/unvisited nodes, # 1- visited, 0- not visited
    for node in range(len(G),0,-1):
        if visited[node] == 0:
            dfs(G1,node,loop=2)
    
    # sort the lengths of sccs
    scc_lens = [len(comp) for comp in scc.values()]
    scc_lens.sort(reverse=True)
    print(scc_lens[0:5])
        
    
a = sys.stdin.readlines()
n = 875714
#n=6
#G = {x:[] for x in range(1,n+1)}
G={}
for line in a:
    (head,tail) = line.split()
    head = int(head)
    if head in G:
        G[head].append(int(tail))
    else:
        G[head] = [int(tail)]

#dfs_order = dfs(G,1)
kosaraju(G)
    
    
