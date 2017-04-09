lines_seen = set() # holds lines already seen
outfile = open("/Users/fabriziofrasca/Desktop/filtered_again.txt", "w")
for line in open("/Users/fabriziofrasca/Desktop/filtered.txt", "r"):
    if line not in lines_seen: # not a duplicate
        outfile.write(line)
        lines_seen.add(line)
outfile.close()
