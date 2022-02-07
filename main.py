class Node:
    def __init__(self,*args,**kwargs):
        self.data = kwargs.get("Data")
        self.next = None

class Link_List:
    def __init__(self,*args,**kwargs):
        self.head = Node(Data=kwargs.get("Data")) #佢.頭

    def Lappend(self,*args,**kwargs):
        current_node = self.head
        while (current_node.next)!= None: #搵到個尾先
            current_node = current_node.next
        current_node.next = Node(Data=kwargs.get("Data")) #喺條尾加新node

    def Lprint(self):
        current_node = self.head
        while (current_node) != None:
            print("["+str(current_node.data)+"] -> ",end="")
            current_node = current_node.next
        print("None")

if __name__ == '__main__':
    link_list = Link_List(Data = 3)
    link_list.Lappend(Data = "BB")
    link_list.Lappend(Data="哥哥")
    link_list.Lprint()


