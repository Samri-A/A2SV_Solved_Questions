class DoublyListNode:
    def __init__(self, val=0, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory:

    def __init__(self, homepage: str):
        self.browser = DoublyListNode(homepage)

    def visit(self, url: str) -> None:
        self.browser.next = None
        node = DoublyListNode(url)
        node.prev = self.browser
        self.browser.next = node
        self.browser = node

    def back(self, steps: int) -> str:
        for i in range(steps):
            if self.browser.prev:
                self.browser = self.browser.prev

        return self.browser.val 
        

    def forward(self, steps: int) -> str:
        for i in range(steps):
            if self.browser.next:
                self.browser = self.browser.next
            
        return self.browser.val 


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
