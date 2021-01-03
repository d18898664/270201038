def reversed_list(liste):
    if liste == []:
        return []
    else:
        return [liste[-1]] + reversed_list(liste[:-1])