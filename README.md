# obvs_to_mean_deviation_to_sample_covariance
Observations to mean deviation to sample covariance matrix

A pure python (no libaries, only primitives approach to solveing for sample covariance given a 2-D matrix of observations.

This script will take in a top and bottom row for a matrix of observations and produce:
  the sample mean
  the "X hat" values
  the "B" matrix
  the sample covariance matrix

The scripts allows any length of list given the top and bottom are the same length. However, the observations matrix must be two rows only.

The reason I wrote this script is because although it is doable by hand with so many calculations making a single mistake over so many entries into
a calculator is high.

I have verified this against several similar format problems and it appears to work. I wrote this in micropython so it can be used in an environment
without the need for any external libraries.

Example run:

    Convers Mtrx of obsvsn to mean-deviation form
    Given matrix A create M=(1/N)[X_1,X_2...X_N]
    Input top row of matrix comma separated
    14,6,9,16,6,19
    Input bottom row of matrix comma separated
    3,15,8,7,6,5
    Size (n): 6
    Sample Mean Matrix: 
    [[2.333333333333333, 1.0, 1.5, 2.6666666666666665, 1.0, 3.1666666666666665], [0.5, 2.5, 1.3333333333333333, 1.1666666666666665, 1.0, 0.8333333333333333]]
    Sample Mean Matrix totalled: [top, bottom] respectively
    [11.666666666666666, 7.333333333333333]
    Press any key to proceed:
    
    Finding Xhat for each vector
    B (matrix of Xhat vectors)[[2.333333333333334, -5.666666666666666, -2.666666666666666, 4.333333333333334, -5.666666666666666, 7.333333333333334], [-4.333333333333333, 7.666666666666667, 0.666666666666667, -0.33333333333333304, -1.333333333333333, -2.333333333333333]]
    Press any key to proceed
    
    Sample covariance matrix is S=(1/N-1)*B*B^Transpose
    B^Transpose
    [[2.333333333333334, -4.333333333333333], [-5.666666666666666, 7.666666666666667], [-2.666666666666666, 0.666666666666667], [4.333333333333334, -0.33333333333333304], [-5.666666666666666, -1.333333333333333], [7.333333333333334, -2.333333333333333]]
    Press any key to proceed
    
    B*B^Transpose is:
    [[149.33333333333331, -66.33333333333334], [-66.33333333333334, 85.33333333333333]]
    Press any key to proceed
    
    [[29.866666666666664, -13.26666666666667], [-13.26666666666667, 17.066666666666666]]
    > 

The functions are reusable, especially the scalar multiplication, matrix multiplication and transpose functions. Thus these could theoretically be
used in other linear algebra or statistics applications. The goal was not memory management nor performance so there may be more performant ways
of doing this.

I hope you enjoy. If you make any improvements I would appreciate a pull request!
