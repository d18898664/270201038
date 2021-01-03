counter = 0
def number_evens(liste):
    global counter
    if liste == []:
        return print(counter)
    else:
        if liste[0] % 2 == 0:
            counter += 1
            return number_evens(liste[1:])
        else:
            return number_evens(liste[1:])