from node import Node

class LinkedList:

    def __init__(self):
        #Empty linked list means (0=>nodes)
        self.head = None
        #Length of the node 
        self.size = 0
    
    # print the length of the linked list
    def __len__(self):
        return self.size

    # insert function which will help to insert from head
    def insert_head(self,value):
        # create new node
        new_node = Node(value)
        # create connection
        new_node.next = self.head
        #reassign the head
        self.head = new_node
        # increament the size
        self.size = self.size + 1

    #traverse (print the list)
    def __str__(self):

        current = self.head
        result = ''

        while current != None:
            result = result + str(current.data) + '->'
            current = current.next

        return result[:-2]
    
    #insert value from the tail
    def append(self,value):

        new_node = Node(value)

        if self.head == None:
            #empty
            self.head = new_node
            self.size = self.size
            return
            
        current = self.head

        while current.next != None:
            current = current.next
        
        #you are at the last node
        current.next = new_node
        self.size = self.size

    #insert at given value insert after
    def insert_after(self,after,value):

        new_node = Node(value)

        current = self.head

        while current != None:
            if current.data == after:
                break
            current = current.next

        #case 1 : come out from while loop through break so in this case current -> not none
        if current != None:
            #logic
            new_node.next = current.next
            current.next = new_node
            self.size = self.size + 1   
        #case 2 : whole loop executed means you haven't found the item in the linked list so in this case current -> none
        else:
            return 'Given Item not FOUND !!!'
        
    #delete whole liked list
    def clear(self):
        self.head = None
        self.size = 0

    #delete from head
    def delete_from_head(self):

        if self.head == None:
            return 'Empty Linked List !!!'
        
        self.head = self.head.next
        self.size = self.size -1

    #delete from last or tail or pop
    def delete_from_tail(self):

        current = self.head

        if current == None:
            return 'Empty Linked List !!!'

        if current.next == None:
            return self.delete_from_head()
        
        while current.next.next != None:
            current = current.next
        
        #now we are on the second last node 
        current.next = None
        self.size = self.size -1

    
    #delete from the given value
    def delete_from_value(self,value):

        current = self.head

        if current == None:
            return 'Empty Linked List !!!'

        if current.data == value:
            #you want to remove the head node
            return self.delete_from_head()

        while current.next != None:
            if current.next.data == value:
                break
            current = current.next

        #case 1: we have found the item
        if current.next == None:
            #we did not find any item in the linked list
            return 'Given Item not FOUND !!!'
        else:
            current.next = current.next.next
            self.size = self.size -1

    #searching the value index from the linked list ( we are passig the value and finding the value position i.e. index)
    def search_by_value(self,value):

        current = self.head
        index_position = 0

        while current !=None:
            if current.data == value:
                return index_position
            index_position = index_position + 1
            current = current.next

        return 'Given Item not FOUND !!!'
    
    #searching the index value from the linked list ( we are passing the index and getting the value present on that index)
    def search_by_index(self,index):

        current = self.head
        index_position = 0

        while current !=None:
            if index_position == index:
                return current.data
            index_position = index_position + 1
            current = current.next
            
        return 'Given Index is not there as List is EMPTY !!!'
    




    ########################QUESTIONS AND ANSWER#########################

    #Q1. FIND THE MAXIMUM NUMBER FROM THE LINKED LIST AND REPLACE IT WITH GIVEN VALUE 

    def replace_max(self,value):

        current = self.head

        if current == None:
            return 'Empty Linked List !!!'

        maximum = current

        while current !=None:
            if current.data > maximum.data:
                maximum = current
            current = current.next

        maximum.data = value


    #Q2. CREATE A FUNTION WHICH WILL SUM ALL THE VALUE OF THE ODD NODE
    
    def sum_of_odd_nodes(self):

        current = self.head

        if current == None:
            return 'Empty Linked List !!!'
        
        sum_of_odd_nodes = 0
        index = 0

        while current !=None:
            if index%2 != 0:
                sum_of_odd_nodes = sum_of_odd_nodes + current.data
            
            index = index + 1
            current = current.next

        return sum_of_odd_nodes
    

    #Q3. CREATE A FUNCTION TO REVERSE A LINKED LIST CONTAINING INTEGER DATA

    def reverse(self):

        previous_node = None

        current_node = self.head

        while current_node !=None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node

        self.head = previous_node

         
# =======================================================================================

l = LinkedList()
# l.insert_head(1)
# l.insert_head(2)
# l.insert_head(3)
# l.insert_head(4)

l.append(10)


    
