def swap_case(s):
    answer = ''
    for i in range(len(s)):
        if s[i].islower():
            answer += s[i].upper()
        else:
            answer +=s[i].lower()
            
    return answer

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
