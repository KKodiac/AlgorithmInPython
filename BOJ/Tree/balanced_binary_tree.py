def check_if_balanced(node):
    if node == None:
        return 0 
        
    left = check_if_balanced(node.left)
    right = check_if_balanced(node.right)

    if left == -1 or right == -1 or abs(left - right) > 1:
        return -1
    
    return 1 + max(left, right)

