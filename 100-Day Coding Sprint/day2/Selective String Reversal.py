def reverse_letters_only(s):
    left,right = 0,len(s)-1
    chars=list(s) # since string is immutable so convert to list 

    while left<right:
        if not chars[left].isalpha():
            left += 1
        elif not chars[right].isalpha():
            right -= 1
        else:
            chars[left],chars[right] = chars[right],chars[left]
            left +=1
            right -= 1


    return "".join(chars)
