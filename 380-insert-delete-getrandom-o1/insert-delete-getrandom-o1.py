import random
class RandomizedSet(object):

    def __init__(self):
        self.track = {}

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.track:
            return False
        else:
            self.track[val] = 1
            return True

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """
        if val in self.track:
            del self.track[val]
            return True
        else:
            return False
        

    def getRandom(self):
        """
        :rtype: int
        """
        return random.choice(list(self.track))
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()