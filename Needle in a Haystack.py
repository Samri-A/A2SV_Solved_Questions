n = int(input())
for _ in range(n):
    s = input()
    t = input()

    s_sorted = ''.join(sorted(s))
    t_sorted = ''.join(sorted(t))

    count = 0

    t_without_s = ''
    for i in t_sorted:
        if count < len(s_sorted):
            if s_sorted[count] == i:
                count+=1
            else:
                t_without_s+= i
        else: t_without_s+= i
            
        
    
    
    if count != len(s_sorted):
        print("Impossible")
    else:
    

    
        reordered_t = ''
    
        pointer_t = 0
        pointer_s = 0
        while pointer_s < len(s) and pointer_t < len(t_without_s):
            if ord(t_without_s[pointer_t]) < ord(s[pointer_s]):
                reordered_t+=t_without_s[pointer_t]
                pointer_t+=1
            elif ord(t_without_s[pointer_t]) == ord(s[pointer_s]):
                reordered_t+= s[pointer_s]
                pointer_s+=1
            else:
                reordered_t+= s[pointer_s]
                pointer_s+=1
    
        if pointer_t < len(t_without_s):
            reordered_t+=t_without_s[pointer_t:]
    
        if pointer_s < len(s):
            reordered_t+= s[pointer_s:]
    
    
        
        print(reordered_t) 
