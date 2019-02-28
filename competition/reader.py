def read(filename):

    f = open(filename)
    num_pic = int(f.readline().split()[0])

    """
    For orientation:
    0 -- Horizontal
    1 -- Vertical
    """
    orient, labels, freqs = [], [], {}

    for i in range(num_pic):
        line, label = f.readline().split(), []
        orient.append(line[0] == 'V')
        for k in range(int(line[1])):
            l = line[k+2]
            if freqs.get(l):
                freqs[l] += 1
            else:
                freqs[l] = 1
            label.append(l)
        labels.append(label)
        assert len(label) == len(line) - 2
    
    return num_pic, orient, labels, freqs
