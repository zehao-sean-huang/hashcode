from reader import *
from OneByOne import oneByOne

num_pic, orient, labels, label_pics = read_for_rank(filename)

def intersect(lab1, lab2):
    return [e for e in lab1 if e in lab2]

def subtract(lab1, lab2):
    return [e for e in lab1 if e not in lab2]

def form_freqs(labels):
    freqs = {}
    for i in range(len(labels)):
        for l in labels[i][1]:
            if get(freqs):
                freqs[l].append(labels[i][0])
            else:
                freqs[l] = [labels[i][0]]
    return freqs

"""
Input: a list of labels, frequencies, threshold
Output: an ordered list of labels
"""
def recursive_find(labels, thres):
    freqs = form_freqs(labels)
    if len(labels) < thres:
        return oneByOne(labels)

    # find label with the highest occurrence
    a = max(freqs.keys(), key=lambda x: freqs[x])
    la = freqs[a]
    del freqs[a]

    # find label with the second highest occurrence
    b = max(freqs.keys(), key=lambda x: freqs[x])
    lb = freqs[b]
    del freqs[b]

    # find order within only first, only second, and intersection label groups
    order_int = recursive_find([labels[i] for i in intersect(la, lb)], freqs, thres)
    order_a = recursive_find([labels[i] for i in subtract(la, lb)], freqs, thres)
    order_b = recursive_find([labels[i] for i in subtract(la, lb)], freqs, thres)

    return order_a + order_int + order_b + recursive_find(subtract(subtract(labels, la)), freqs, thres)