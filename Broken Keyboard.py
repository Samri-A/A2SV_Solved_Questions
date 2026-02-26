n = int(input())

for _ in range(n):
    typed_str = input()
    
    pointer = 0
    answer = {}
    
    while pointer < len(typed_str):
        if pointer + 1 < len(typed_str):
            if typed_str[pointer] == typed_str[pointer+1]:
                pointer+=2
            else:
                if typed_str[pointer] not in answer:
                    answer[typed_str[pointer]] = 1
                pointer+=1
        else: 
            if typed_str[pointer] not in answer:
                    answer[typed_str[pointer]] = 1
            pointer+=1
    
    un_answer =''
    for key in answer:
         un_answer+=key
         
    sorted_answer = ''.join(sorted(un_answer))
    print(sorted_answer)

