def read(filename):
    """
    0 -- Tomato
    1 -- Mushroom
    """
    f = open(filename)
    r, c, l, h = tuple([int(parameter) for parameter in f.readline().split()])

    pizza = []
    used = []

    for i in range(r):
        pizza.append([0 if char == 'T' else 1 for char in f.readline()][:-1])
        used.append([False for _ in pizza[i]])

    # Debug
    # print(pizza)
    # print(used)
    # End Debug

    return r, c, l, h, pizza, used
