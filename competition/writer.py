def output(outputs, input_filename, random=False):
    if random:
        output_filename = input_filename[0] + (".random.out")
    else:
        output_filename = input_filename[0] + (".out")
    
    
    fout = open(output_filename, "w")
    
    fout.write(str(len(outputs)) + "\n")
    for slide in outputs:
        if len(slide[0]) == 1:
            fout.write(str(slide[0][0]))
        else:
            fout.write(str(slide[0][0]) + " " + str(slide[0][1]))
        fout.write("\n")

    fout.close()
