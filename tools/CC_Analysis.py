# perform connected components graph analysis
import numpy as np
import matplotlib.pyplot as plt

def main():
    sample_count = 5 # generated 5 random unique samples (each size 100,000)
    cutoffs_per_sample = 10 # similarities between 0.1 and 1

    # values in percent
    lower_threshold = 10
    upper_threshold = 100

    increment = 10

    # first 8 lines in the connected component file are irrelevant
    skip_lines = 8

    # results come out in row-pairs
    # even rows store number of components in the connected component
    # odd rows store the size of the largest component in the connected component
    matrix_height = sample_count*2;
    p_val_matrix = [[0 for x in range(cutoffs_per_sample)] for y in range(matrix_height)] 

    filename_prefix = "../cutoff/"
    filename_mid = "cutoff_"
    filename_suffix = ".txt"

    for current_sample in range(0, sample_count):
        for cutoff in range(lower_threshold, upper_threshold+1, increment):
            filename = filename_prefix + filename_mid + str(cutoff) + filename_suffix
            file = open(filename)

            n_components = 0
            largest_component = 0

            for i in range(skip_lines):
                next(file)

            counter = 0
            line_num = 0

            for line in file:
                line_num = line_num + 1
                l = line.replace("\n", "").split(" ")

                if "//" in l:
                    n_components = n_components + 1
                    if counter > largest_component:
                        largest_component = counter
                        counter = 0
                else:
                    counter = counter + len(l[3].split(","))


            p_val_matrix[2*current_sample][(cutoff/10) - 1] = n_components
            p_val_matrix[(2*current_sample)+1][(cutoff/10) - 1] = largest_component
    
    for i in range(sample_count):
        line1, = plt.plot(range(lower_threshold, upper_threshold, 2), p_val_matrix[2*i], 'r--', label="Number of components")
        line2,= plt.plot(range(lower_threshold, upper_threshold, 2), p_val_matrix[int(2*i)+1], 'bs', label="Largest component")
        plt.ylabel('number')
        plt.legend()
        plt.show()

if __name__ == "__main__":
    main()