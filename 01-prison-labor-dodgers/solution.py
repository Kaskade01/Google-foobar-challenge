def answer(x, y):
    lookuptable = dict()
    
    # count each occurence of a number in X array and save its count in a map
    for id_number in x:
        if(id_number in lookuptable):
            lookuptable[id_number] += 1
        else:
            lookuptable[id_number] = 1

    # keep counting numbers in Y array
    for id_number in y:
        if(id_number in lookuptable):
            lookuptable[id_number] += 1
        else:
            lookuptable[id_number] = 1

    # find the answer
    for id in lookuptable:
        if lookuptable[id] % 2 != 0:
            return id

x = (14, 27, 1, 4, 2, 50, 3, 1, -4, 82)
y = (2, 4, -4, 3, 1, 1, 14, 27, 50)
print(answer(x,y))