from OneByOne import *
from enumerate_vertical import *
from scorer import *

files = [
    "a_example.txt", 
    # "b_lovely_landscapes.txt", 
    "c_memorable_moments.txt"
    # "d_pet_pictures", 
    # "e_shiny_selfies"
]

for file in files:

    print("processing " + file)

    inputs = join_verticals(file)
    outputs = oneByOne(inputs)
    
    # debug
    # print(outputs[0])
    # print(outputs[1])
    # print(inputs[0])
    # print(inputs[1])
    
    print(score(outputs))
