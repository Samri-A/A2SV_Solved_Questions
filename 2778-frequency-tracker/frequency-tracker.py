class FrequencyTracker(object):

    def __init__(self):
        self.array = []
        self.freq_tracker = {}
        self.freqs_counter = {}

    def add(self, number):
        """
        :type number: int
        :rtype: None
        """
        self.array.append(number)

        if number in self.freq_tracker:
            
            self.freqs_counter[self.freq_tracker[number]] -= 1
            self.freq_tracker[number] += 1
            if  self.freq_tracker[number] in self.freqs_counter:
                self.freqs_counter[self.freq_tracker[number]] += 1
            else:
                self.freqs_counter[self.freq_tracker[number]] = 1
        else:
            
            self.freq_tracker[number] = 1

            if  self.freq_tracker[number] in self.freqs_counter:
                self.freqs_counter[self.freq_tracker[number]] += 1
            else:
                self.freqs_counter[self.freq_tracker[number]] = 1
        
        

        

    def deleteOne(self, number):
        """
        :type number: int
        :rtype: None
        """
        if number in self.freq_tracker:
            self.array.remove(number)
            self.freqs_counter[self.freq_tracker[number]] -= 1
            if self.freqs_counter[self.freq_tracker[number]] == 0:
                del  self.freqs_counter[self.freq_tracker[number]] 
            self.freq_tracker[number] -= 1
            if self.freq_tracker[number] == 0:
                del self.freq_tracker[number] 
            else : 
                if  self.freq_tracker[number] in self.freqs_counter:
                    self.freqs_counter[self.freq_tracker[number]] += 1
                else:
                    self.freqs_counter[self.freq_tracker[number]] = 1
            

    def hasFrequency(self, frequency):
        """
        :type frequency: int
        :rtype: bool
        """
        if frequency in self.freqs_counter:
            if self.freqs_counter[frequency] > 0: return True
        return False 





        


# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)