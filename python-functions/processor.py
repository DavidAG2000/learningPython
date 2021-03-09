def process_numbers(lista):
    res = []
    
    if (type(lista) is list):
        for item in lista:
            if (type(item) is int):
                res.append(item)
            elif (isinstance(item, str)):
                if item.isnumeric():
                    res.append(int(item))

    res.sort()
    return res

def process_names(lista):
    res = []

    if (type(lista) is list):
        for item in lista:
            if (type(item) is str):
                if not(item.isnumeric()):
                    res.append(item)
    
    res.sort()
    return res
