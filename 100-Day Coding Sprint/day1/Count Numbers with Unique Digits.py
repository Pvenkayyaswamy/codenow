#my approach 1:
def count_unique_digit_numbers(n1, n2):
    count = 0
    for i in range(n1,n2+1):
        st=str(i)
        if(len(st)==len(set(st))):
            count+=1
    return count





#my approach 2
def count_unique_digit_numbers(n1, n2):
    count = 0
    
    for i in range(n1, n2 + 1):
        if i == 0:
            count += 1
            continue
            
        num = i
        # Create a tracker for digits 0-9 (all initially False)
        digit_seen = [False] * 10
        has_duplicate = False
        
        while num > 0:
            digit = num % 10  # Get the last digit
            
            if digit_seen[digit]:
                has_duplicate = True
                break  # Found a duplicate, stop checking this number
                
            digit_seen[digit] = True
            num //= 10  # Remove the last digit
            
        if not has_duplicate:
            count += 1
            
    return count
