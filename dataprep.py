with open('Ru5.txt', 'r') as data_file:
    with open('output5.txt', 'a') as output_file:
          # read each line from data.txt
        for line in data_file:
             
            # change case for the line and write
            # it into output file
            output_file.write(line.lower())




