def convert_camel_case(cstr):
    chars = list(cstr)
    final = []
    for i in chars:
        if i.isupper():
            final.append(" ")
        
        final.append(i.lower())


    return "".join(final)
