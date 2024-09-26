class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class MyCircularDeque:
    def __init__(self, k: int):
        self.max=k
        self.head=None
        self.tail=None
        self.count=0
    def insertFront(self, value: int) -> bool:
        if self.count==self.max:
            return False
        node=Node(value)
        if not self.head:
            self.head=node
            self.tail=node
        else:
            node.next=self.head
            self.head=node
        self.count+=1
        return True
    def insertLast(self, value: int) -> bool:
        if self.count==self.max:
            return False
        node=Node(value)
        if not self.tail:
            self.tail=node
            self.head=node
        else:
            self.tail.next=node
            self.tail=node
        self.count+=1
        return True
        
    def deleteFront(self) -> bool:
        if not self.head:
            return False
        if self.count==1:
            self.head=None
            self.tail=None
        else:
            nexx=self.head.next
            self.head.next=None
            self.head=nexx
        self.count-=1
        return True

    def deleteLast(self) -> bool:
        if not self.tail:
            return False
        if self.count==1:
            self.head=None
            self.tail=None
        else:
            cur=self.head
            prev=None
            while cur.next:
                prev=cur
                cur=cur.next
            prev.next=None
            self.tail=prev
        self.count-=1
        return True
        

    def getFront(self) -> int:
        if self.head:
            return self.head.val
        return -1
        
    def getRear(self) -> int:
        if self.tail:
            return self.tail.val
        return -1

    def isEmpty(self) -> bool:
        return self.count==0
    def isFull(self) -> bool:
        return self.count==self.max
        


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