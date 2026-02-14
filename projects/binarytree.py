class node:
    def __init__(self, value:int,):
        self.value = value
        self.left = None
        self.right = None
        self.before = None
    def __repr__(self):
        return str(self.value)
def insert(node):
    comp = root
    while True:
        if node.value >= comp.value:
            if comp.right == None:
                node.before = comp
                comp.right = node
                break
            else:
                comp = comp.right
        else:
            if comp.left == None:
                node.before = comp
                comp.left = node
                break
            else:
                comp = comp.left


root = node(50)
while True:
    action = input("enter a number to add to the tree or say stop: ")
    if action.lower() == "stop":
        print("thank you!")
        break
    else:
        try:
            int(action)
        except ValueError:
            print("thats not a number")
        else:
            insert(node(int(action)))
        finally:
            print(root.left)