def read_file(path) :
    with open(path) as f :
        lines = f.readlines()
        for line in lines  :
            words= line.split(",")
            return words 
       