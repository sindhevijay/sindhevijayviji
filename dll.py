class Node:
    def _init_(self,data):
        self.item = data
        self.next =  None
        self.prev = None
class doblyLinkedList:
    def _init_(self):
        self.start_node is None
    def InsertToEmptyList (self,data):
        if self.start_node is None:
            new_node = Node(data)
            self.start_Node = new_node
        else:
            print("the list is empty")
    def InsertTOEnd(self, data):
        if start_Node is None:
            new_node = Node(data)
            self.start_node = new_node
            return
        n = self.start_node
        while n.next is not None:
            n =n.next
            new_node = Node(data)
            n.next = new_node
            new_node.prev = n
    def DeleteAtstart(self):
        if self.start_node is None:
            print("the Linked list is empty, no element to delete")
            return
        if self.start_node.next is None:
            self.start_node=None
            self.start_node  = self.start_node.next
            self.start_prev = None;
            delete_at_end(self)
        if self.start_node is None:
            print("the Linked list is empty, no element to delete")
            return
        if  self.start_node.next is None:
            self.start_node=None
            return
        n = self_node.next is None
        while n.next is not None:
            n = n.next
            n.prev.next =None
            Display(self)
            if  self.start_node.next is None:
                print("the  list is empty")
                return
            else:
                n = self.start_node
                while n is not None:
                    print("Element is: ", n.item)
                    n =n.next
                    print ("\n")
                    NewDoubleYLinkedList = doublyLinkedList()
                    NewDoubleYLinkedList.InsertToEmptyList(10)
                    NewDoubleYLinkedList.InsertToEnd(20)
                    NewDoubleYLinkedList.InsertToEnd(30)
                    NewDoubleYLinkedList.InsertToEnd(40)
                    NewDoubleYLinkedList.InsertToEnd(50)
                    NewDoubleYLinkedList.InsertToEnd(60)
                    NewDoubleYLinkedList.Dispaly()
                    NewDoubleYLinkedList.DeleteAtStart()
                    NewDoubleYLinkedList.DeleteAtStart()
                    NewDoubleYLinkedList.Display()
                           
