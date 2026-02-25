class Solution:
    def customSortString(self, order: str, s: str) -> str:
        order_char_values = {}
        for i in range(len(order)):
            order_char_values[order[i]] = i

        def compare(a ,b):
            if a in  order_char_values and b in order_char_values:
                return order_char_values[a] - order_char_values[b]
            else: 
                if a in  order_char_values:
                    return -1
                elif  b in  order_char_values:
                    return 1
                else:
                    return ord(a) - ord(b)



        s_sorted = sorted(s , key = cmp_to_key(compare))

        print(s_sorted)
        return ''.join(s_sorted)



        
        