from rdkit import Chem
from rdkit.Chem import AllChem
import sys

def main(filepath):
    fin = open(filepath, 'r')


    f1024 = open("morgan_1024.fps", 'w+')
    f2048 = open("morgan_2048.fps", "w+")
    f4096 = open("morgan_4096.fps", "w+")

    counter = 1
    for line in fin:
        print("#" + str(counter))
        smi = line.split(" ")[0]
        m1 = Chem.MolFromSmiles(smi)
        fp1 = AllChem.GetMorganFingerprintAsBitVect(m1,2,1024)
        fp2 = AllChem.GetMorganFingerprintAsBitVect(m1,2,2048)
        fp3 = AllChem.GetMorganFingerprintAsBitVect(m1,2,4096)
        temp1 = ""
        for i in range(fp1.GetNumBits()):
            if fp1.GetBit(i):
                temp1 = temp1 + '1'
            else:
                temp1 = temp1 + '0'
        f1024.write(temp1 + "\n")

        temp1 = ""
        for i in range(fp2.GetNumBits()):
            if fp2.GetBit(i):
                temp1 = temp1 + '1'
            else:
                temp1 = temp1 + '0'
        f2048.write(temp2 + "\n")

        temp1 = ""
        for i in range(fp3.GetNumBits()):
            if fp3.GetBit(i):
                temp1 = temp1 + '1'
            else:
                temp1 = temp1 + '0'
        f4096.write(temp1 + "\n")
        counter = counter + 1

    f1024.flush()
    f2048.flush()
    f4096.flush()

    f1024.close()
    f2048.close()
    f4096.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide smiles input file to be converted to fingerprints."
    else:
        main(sys.argv[1])
