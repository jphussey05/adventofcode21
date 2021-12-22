class Node:

    def __init__(self, data, stub=False) -> None:
        self.left = None # left child
        self.right = None # right child
        self.data = data # this nodes value
        self.stub = stub


    def __str__(self) -> str:
        output = f'Root: {self.data}\n'
        if self.left:
            output += f'\tLeft: {self.left.data}\n'
        if self.right:
            output += f'\tRight: {self.right.data}'

        return output

    
    def height(self) -> int:
        # a child will have no left or right
        if self.stub:
            return 0
        else:
            return 1 + max(self.left.height(), self.right.height())
                

        
def build_bt(nodes):

    if type(nodes) == int:
        return Node(nodes, stub=True)
    else:
        root = Node(nodes)
        root.left = build_bt(nodes[0])
        root.right = build_bt(nodes[1])
        
        return root

nodes = [[6,[5,[4,[3,2]]]],1]

bt = build_bt(nodes)
print(bt)

# if height is 5 or more, find the left most pair with depth of 4
print(bt.height())
