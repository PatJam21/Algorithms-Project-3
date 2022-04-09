#https://programmingpraxis.com/2010/04/09/minimum-spanning-tree-prims-algorithm/

from collections import defaultdict
from heapq import *
new_cost = 0

def prim( nodes, edges ):
    global new_cost

    conn = defaultdict( list )
    for n1,n2,c in edges:
        conn[ n1 ].append( (c, n1, n2) )
        conn[ n2 ].append( (c, n2, n1) )
 
    mst = []
    used = set( [nodes[ 0 ]] )
    usable_edges = conn[ nodes[0] ][:]
    heapify( usable_edges )
 
    while usable_edges:
        cost, n1, n2 = heappop( usable_edges )

        if n2 not in used:
            used.add( n2 )
            mst.append( ( n1, n2, cost ) )
            new_cost += cost
            for e in conn[ n2 ]:
                if e[ 2 ] not in used:
                    heappush( usable_edges, e )


    return mst
 
#test
nodes = list("ABCDEFGHI")
edges = [('A', 'B', 22), ('A', 'C', 9), ('A', 'D', 12), \
    ('B', 'A', 22), ('B', 'C', 35), ('B', 'H', 34), ('B', 'F', 36), \
    ('C', 'A', 9), ('C', 'B', 35), ('C', 'D', 4), ('C', 'E', 65), ('C', 'F', 42), \
    ('D', 'A', 12), ('D', 'C', 4), ('D', 'E', 33), ('D', 'I', 30), \
    ('E', 'C', 65), ('E', 'F', 18), ('E', 'G', 23), ('E', 'D', 33), \
    ('F', 'B', 36), ('F', 'H', 24), ('F', 'G', 39), ('F', 'E', 18), ('F', 'C', 42), \
    ('G', 'F',39), ('G', 'E', 23), ('G', 'H', 25), ('G', 'I', 21), \
    ('H', 'B', 34), ('H', 'G', 25), ('H', 'F', 24), ('H', 'I', 19), \
    ('I', 'H', 19), ('I', 'G', 21), ('I', 'D', 30)]
 
print ("Minimum path:", prim( nodes, edges ), "\n")

print("Weight of minimum spanning tree: " + str(new_cost))
