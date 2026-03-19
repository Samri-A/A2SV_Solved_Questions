class DataStream:

    def __init__(self, value: int, k: int):
        self.count = { value : 0}
        self.k = k
        self.value = value

    def consec(self, num: int) -> bool:
        if self.value == num:
            self.count[self.value] += 1
        else:
            self.count[self.value] = 0
            
        
        if self.count[self.value] < self.k :
            return False
        else:
            return True



# Your DataStream object will be instantiated and called as such:
# obj = DataStream(value, k)
# param_1 = obj.consec(num)
