def score(order):
    total_score = 0
    for i in range(len(order) - 1):
        p1, p2 = order[i][1], order[i+1][1]
        sc = 0 # number of common tags
        for k in range(len(p1)):
            if p1[k] in p2:
                sc += 1
        total_score += min(sc, len(p1) - sc, len(p2) - sc)
    return total_score
