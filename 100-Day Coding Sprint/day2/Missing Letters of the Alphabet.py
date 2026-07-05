import string
def find_missing_letters(str):
    st=set(str.lower())
    miss=[]
    for let in string.ascii_lowercase:
        if let not in st:
            miss.append(let)

    if not miss:
        return 0
    return "".join(miss)
