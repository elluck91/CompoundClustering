import random
import sys

def main(inputfile, linecount):
    # read the fingerprint
    inp = open(inputfile, 'r')

    # select 100,000 samples randomly
    output1 = open("sample_0_morgan_1024.fps", "w+")
    output2 = open("sample_1_morgan_1024.fps", "w+")
    output3 = open("sample_2_morgan_1024.fps", "w+")
    output4 = open("sample_3_morgan_1024.fps", "w+")
    output5 = open("sample_4_morgan_1024.fps", "w+")

    size = 100000

    row_ids1 = random.sample(range(0, linecount), size)
    row_ids2 = random.sample(range(0, linecount), size)
    row_ids3 = random.sample(range(0, linecount), size)
    row_ids4 = random.sample(range(0, linecount), size)
    row_ids5 = random.sample(range(0, linecount), size)

    row_ids1.sort()
    row_ids2.sort()
    row_ids3.sort()
    row_ids4.sort()
    row_ids5.sort()


    row_num = 0
    ids_num1 = 0
    ids_num2 = 0
    ids_num3 = 0
    ids_num4 = 0
    ids_num5 = 0

    print("%d %% completed." % (row_num/linecount * 100), end='')

    for row in inp:
        # progress status
        print("\r %d %% completed." % (row_num/linecount * 100), end='')
        if row_num == row_ids1[ids_num1]:
            output1.write(row)
            if ids_num1 < size-1:
                ids_num1 = ids_num1 + 1
        if row_num == row_ids2[ids_num2]:
            output2.write(row)
            if ids_num2 < size-1:
                ids_num2 = ids_num2 + 1
        if row_num == row_ids3[ids_num3]:
            output3.write(row)
            if ids_num3 < size-1:
                ids_num3 = ids_num3 + 1
        if row_num == row_ids4[ids_num4]:
            output4.write(row)
            if ids_num4 < size-1:
                ids_num4 = ids_num4 + 1
        if row_num == row_ids5[ids_num5]:
            output5.write(row)
            if ids_num5 < size-1:
                ids_num5 = ids_num5 + 1

        row_num = row_num + 1

    inp.close()
    output1.flush()
    output1.close()
    output2.flush()
    output2.close()
    output3.flush()
    output3.close()
    output4.flush()
    output4.close()
    output5.flush()
    output5.close()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print "Please provide fingerprint file for random sample generation."
    else:
        main(sys.argv[1])