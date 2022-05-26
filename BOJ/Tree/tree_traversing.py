from collections import defaultdict

def solution():
    def preorder(graph, root):
        visited = []
        if root != '.':
            nodes = graph[root]
            left = nodes[0]
            right = nodes[1]
            visited.append(root)
            visited = visited + preorder(graph, left)
            visited = visited + preorder(graph, right)
        return visited
    
    def inorder(graph, root):
        visited = []
        if root != '.':
            nodes = graph[root]
            left = nodes[0]
            right = nodes[1]
            visited = visited + inorder(graph, left)
            visited.append(root)
            visited = visited + inorder(graph, right)
        return visited

    def postorder(graph, root):
        visited = []
        if root != '.':
            nodes = graph[root]
            left = nodes[0]
            right = nodes[1]
            visited = visited + postorder(graph, left)
            visited = visited + postorder(graph, right)
            visited.append(root)
        return visited

    
    N = int(input())
    tree = defaultdict(list)

    for _ in range(N):
        root, left, right = map(str, input().split())
        tree[root].append(left)  # 0 for left node index
        tree[root].append(right) # 1 for right node index
    
    print("".join(i for i in preorder(tree, 'A')))
    print("".join(j for j in inorder(tree, 'A')))
    print("".join(k for k in postorder(tree, 'A')))

if '__main__' == __name__:
    solution()