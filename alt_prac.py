def diameterOfBinaryTree(root,dia=0):
    if not root: return 0
    if root:
        lh=diameterOfBinaryTree(root.left,dia)
        rh=diameterOfBinaryTree(root.right.dia)
        dia = max(dia,lh+rh)
        return 1+max(lh,rh)
     