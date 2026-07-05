def solvemove_multiples_of_ten(n, arr):
    non_div,div=[],[]
    for i in arr:
        if i % 10 == 0:
            div.append(i)
        else:
            non_div.append(i)
    
    return (non_div+div)
