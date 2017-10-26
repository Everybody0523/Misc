from graph import UndirectedGraph

def main():
    g0 = UndirectedGraph()
    g0.addVertex(1)
    g0.addVertex(2)
    g0.addVertex(3)
    g0.addEdge((1, 2))
    g0.addEdge((1, 3))
    print(g0)
    x = g0.isTree(1, {})
    if x:
        print("g0 is a tree")
    else:
        print("g0 is not a tree")

    print("\n")
    g0.addVertex(4)
    g0.addEdge((3, 4))
    print(g0)
    x = g0.isTree(1, {})
    if x:
        print("g0 is a tree")
    else:
        print("g0 is not a tree")

    print("\n")
    g0.addEdge((2, 4))
    print(g0)
    x = g0.isTree(1, {})
    if x:
        print("g0 is a tree")
    else:
        print("g0 is not a tree")


if __name__ == '__main__':
    main()
