def output(outputs, input_filename):
    output_filename = input_filename[0] + (".out")
    
    fout = open(output_filename, "w")
    
    fout.write(str(len(outputs)) + "\n")
    for slide in outputs:
        print(slide)
        if len(slide[0]) == 1:
            fout.write(str(slide[0][0]))
        else:
            fout.write(str(slide[0][0]) + " " + str(slide[0][1]))
        fout.write("\n")

    fout.close()
