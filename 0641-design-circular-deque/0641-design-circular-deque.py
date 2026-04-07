class MyCircularDeque:

    def __init__(self, k: int):
        self.head = ListNode()
        
        self.tail = ListNode()

        self.head.next = self.tail

        self.tail.prev = self.head

        self.size = 0 
        self.k = k

    def insertFront(self, value: int) -> bool:
        if self.isFull():
            return False
        temp = ListNode(value)
        temp.next = self.head.next
        temp.prev = self.head 
        self.head.next.prev = temp
        self.head.next = temp
        self.size +=1
        return True



    def insertLast(self, value: int) -> bool:
        if self.isFull():
            return False
        
        
        temp = ListNode(value)
        temp.next = self.tail
        temp.prev =  self.tail.prev
        self.tail.prev.next = temp
        self.tail.prev = temp 

        self.size+=1
        return True
        
         

    def deleteFront(self) -> bool:
        if self.isEmpty():
            return False
        
        node_remove =  self.head.next
        self.head.next = node_remove.next
        node_remove.next.prev = self.head
        self.size-=1
        return True
        


    def deleteLast(self) -> bool:
        if self.isEmpty():
            return False
        
        node_remove = self.tail.prev
        node_remove.prev.next = self.tail
        self.tail.prev = node_remove.prev
        self.size-=1
        return True

    def getFront(self) -> int:
        if self.isEmpty():
            return -1

        
        return self.head.next.val

    def getRear(self) -> int:
        if self.isEmpty():
            return -1
        return self.tail.prev.val
        

    def isEmpty(self) -> bool:
        return self.size == 0
        

    def isFull(self) -> bool:
        return self.k == self.size
        


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()