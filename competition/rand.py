from random import shuffle
from OneByOne import *
from enumerate_vertical import *
from scorer import *
from writer import *

files = [
    "a_example.txt", 
    "b_lovely_landscapes.txt", 
    "c_memorable_moments.txt",
    "d_pet_pictures.txt", 
    "e_shiny_selfies.txt"
]

scores_file = open("scores.out", "w")

for file in files:

    print("processing " + file)

    inputs = join_verticals(file)
    shuffle(inputs)
    
    output(inputs, file, random=True)

    scores_file.write(str(score(inputs)) + "\n")
