from reader import *

# 0 -> horizontal
# 1 -> vertical

def compute(labels1, labels2):
    v1_tags_cnt = len(labels1) # array
    v2_tags_cnt = len(labels2) # array
    intersect = [label for label in labels1 if label in labels2]
    return len(intersect) / (v1_tags_cnt + v2_tags_cnt - len(intersect))

def join_verticals(filename):

    print("sorting verticals for " + filename)

    num_pic, orient, labels, freqs = read(filename)

    vertical_photos = [i for i in range(num_pic) if orient[i] == 1]
    vertical_photos_cnt = len(vertical_photos)
    horizontal_photos = [i for i in range(num_pic) if orient[i] == 0]
    horizontal_photos_cnt = len(horizontal_photos)

    mapping = dict()

    # print(vertical_photos_cnt)

    for i in range(vertical_photos_cnt - 1):
        print("iterating from " + str(i) + "th vertical...")
        for j in range(i + 1, vertical_photos_cnt):
            picture_1 = vertical_photos[i]
            picture_2 = vertical_photos[j]
            efficiency = compute(labels[picture_1], labels[picture_2])
            mapping[(picture_1, picture_2)] = efficiency

    sorted_mapping = sorted(mapping.items(), key=lambda item: item[1], reverse=True)
    remaining = set(vertical_photos)
    output = []

    for item in sorted_mapping:
        if item[0][0] in remaining and item[0][1] in remaining:
            remaining.remove(item[0][0])
            remaining.remove(item[0][1])
            output.append(((item[0][0], item[0][1]), list(set(labels[item[0][0]]).union(set(labels[item[0][1]])))))

    for photo in horizontal_photos:
        output.append(((photo), labels[photo]))

    print("sorting verticals for " + filename + " finished.")

    return output

