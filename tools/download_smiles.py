import urllib2
base = 'http://zinc15.docking.org/substances/ZINC0000000'
counter = 0
found = 0
not_found = 0
fout = open("smiles.smi", 'w+')
stop = 0
while found < 10000:
    url = ""
    string = ""
    if len(str(counter)) < 5:
        for l in range(5-len(str(counter))):
            string = "0" + str(counter)
            
    url = base + str(string) + ".smi"
    try:
        response = urllib2.urlopen(url)
        to_file = response.read().replace("\n", "")
        temp = to_file.split(" ")
        found = found + 1
        fout.write(temp[1] + "," + temp[0] + "\n")
    except:
        not_found = not_found + 1
    counter = counter + 1
    print("Downloaded: " + str(found) + " SMILEs")

fout.flush()
fout.close()
print("Downloaded " + str(found) + " SMILES")
