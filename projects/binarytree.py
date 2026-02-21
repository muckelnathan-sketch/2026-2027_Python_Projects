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
                comp.has_left = True
                break
            else:
                comp = comp.right
        else:
            if comp.left == None:
                node.before = comp
                comp.left = node
                comp.has_right = True
                break
            else:
                comp = comp.left

def print_tree():
    iteration = 2
    l = root
    r = None 
    c = 100
    while True:
        iteration += 1
        if l == None and r == None:
            break
        elif r != None:
            c-=2
            print(f"{l.value}" + " "*iteration + f"{r.value}".center(c))
            print("/" + " "*(iteration+1) + "\\".center(c-1))
            l = l.left
            r = r.right
        else:
            print(str(l.value).center(c))
            print("/".center(c-1) if l.has_left else " ","\\".center(c+1) if l.has_right else None )
            l = l.left
            r = l.right
            

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
        finally:
            print(f"added {action}")