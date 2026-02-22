import random;nodes = 1
class node:
    def __init__(self, value:int):
        self.value = value
        self.left = None
        self.right = None
        self.before = None
        self.has_left = False
        self.has_right = False
    def __repr__(self):
        return str(self.value)
root = node(50)
def insert(node):
    comp = root
    while True:
        if node.value >= comp.value:
            if comp.right == None:
                node.before = comp
                comp.right = node
                comp.has_right = True
                break
            else:
                comp = comp.right
        else:
            if comp.left == None:
                node.before = comp
                comp.left = node
                comp.has_left = True
                break
            else:
                comp = comp.left

def print_tree():

    current = root
    node_coordinates = []
    class nodee:
        def __init__(self, value, x, y):
            self.value = str(value)
            self.x = x
            self.y = y
    prev = nodee(root.value,50,0)
    node_coordinates.append(prev)
    while nodes > len(node_coordinates):
        if current.has_right:
            if current.right not in node_coordinates:
                node_coordinates.append(nodee("\\", prev.x+1, prev.y+1))
                node_coordinates.append(nodee(current.right.value, prev.x+2, prev.y+2 ))
            if current.has_right:
                current = current.right
            else: current = current.left
        if current.has_left:
            if current.left not in node_coordinates:
                node_coordinates.append(nodee("/", prev.x-1, prev.y+1))
                node_coordinates.append(nodee(current.left.value, prev.x-2, prev.y+2 ))
            if current.has_left:
                current = current.left
            else: current = current.right
        r = []
        if current.has_left: r.append(current.left)
        if current.has_right: r.append(current.right)
        current = random.choice(r)
        if not current.has_left and not current.has_right:
            current = root
    else:
        for y in range(100):
            for x in range(100):
                for n in node_coordinates:
                    if n.x == x and n.y == y:
                        print(n.value, end = "")
                    else:   
                        print(" ", end = "")
            print("\n")
while True:
    action = input("enter a number to add to the tree or say stop: ")
    if action.lower() == "stop":
        print("thank you!")
        print_tree()
        break
    else:
        try:
            int(action)
        except ValueError:
            print("thats not a number")
        else:
            insert(node(int(action)))
            nodes += 1
        finally:
            print(f"added {action}")