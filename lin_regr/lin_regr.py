"""
    @author Anthony (Tony) Poerio
    @email adp59@pitt.edu
    CS1571 - Artificial Intelligence
    Prof. Rebecca Hwa
    Fall 2016
    HW04 - Linear Regression
"""

import sys


###################
### ENTRY POINT ###
###################
def main():
    """  Accepts two (2) command line arguments.
         arg1 = filename for training
         arg2 = filename for testing
    """

    # check for univariate case
    if len(sys.argv) == 3:
        print "========UNIVARIATE CASE======="
        # parse the file data
        training_tuples = parse_data(sys.argv[1])
        testing_tuples = parse_data(sys.argv[2])

        # get gradient descent variables
        print "--------TRAINING--------"
        w0,w1 = gradient_descent(training_tuples)

        # make a prediction for x_i and compare to y_i
        # for each case in the test set
        # store the errors
        # and print the average squared error, overall
        sum_of_sq_err = sum_of_squared_error_over_entire_dataset(w0,w1,testing_tuples)
        avg_sq_err = sum_of_sq_err/len(testing_tuples)
        print "---------TESTING--------"
        print "USING LINEAR REGRESSION"
        print "The AVERAGE Squared Error over the Entire Testing Data Set = "+str(avg_sq_err)
    else:
        # if there's only one input file, we have the multivariate case,
        # and then we need to split up the data set ourselves
        print "=======MULTIVARIATE CASE========"
    return

def parse_data(filename):
    """
    We have pairs on each line in the file, (x,y)
    Where:
        x = is a feature (feature vector for pt2)
        y = is the the expected answer
    :param filename: the filename to parse
    :return: a list of tuples, for our (x,y) values
    """

    x_y_tuples = []
    with open(filename, 'r') as f:
        for line in f:
            stripped_line = line.strip("\r\n")
            split_data = stripped_line.split(",")
            x = float(split_data[0])
            y = float(split_data[1])
            pair = (x,y)
            x_y_tuples.append(pair)

    return x_y_tuples



######################
###### TRAINING ######
######################
def gradient_descent(training_examples, alpha=0.01):
    """
    Apply gradient descent on the training examples to learn a line that fits through the examples
    :param examples: set of all examples in (x,y) format
    :param alpha = learning rate
    :return:
    """
    # initialize w0 and w1 to some small value, here just using 0 for simplicity
    w0 = 0
    w1 = 0

    # repeat until "convergence", meaning that w0 and w1 aren't changing very much
    # --> need to define what 'not very much' means, and that may depend on problem domain
    convergence = False
    while not convergence:
        # initialize temporary variables, and set them to 0
        delta_w0 = 0
        delta_w1 = 0

        for pair in training_examples:
            # grab our data points from the example
            x_i = pair[0]
            y_i = pair[1]

            # calculate a prediction, and find the error
            h_of_x_i = model_prediction(w0,w1,x_i)
            delta_w0 += prediction_error(w0,w1, x_i, y_i)
            delta_w1 += prediction_error(w0,w1,x_i,y_i)*x_i

        # store previous weighting values
        prev_w0 = w0
        prev_w1 = w1

        # get new weighting values
        w0 = w0 + alpha*delta_w0
        w1 = w1 + alpha*delta_w1
        alpha -= 0.001

        # every few iterations print out current model
        #     1.  -->  (w0 + w1x1 + w2x2 + ... + wnxn)
        print "Current model is: ("+str(w0)+" + "+str(w1)+"x1)"
        #     2.  -->  averaged squared error over training set, using the current line
        summed_error = sum_of_squared_error_over_entire_dataset(w0, w1, training_examples)
        avg_error = summed_error/len(training_examples)
        print "Average Squared Error="+str(avg_error)


        # check if we have converged
        if abs(prev_w0 - w0) < 0.00001 and abs(prev_w1 - w1) < 0.00001:
            convergence = True

    # after convergence, print out the parameters of the trained model (w0, ... wn)
    print "Parameters of trained model are: w0="+str(w0)+", w1="+str(w1)
    return w0, w1


############################
##### TRAINING HELPERS #####
############################
def model_prediction(w0, w1, x_i):
    return w0 + (w1 * x_i)

def prediction_error(w0, w1, x_i, y_i):
    # basically, we just take the true value (y_i)
    # and we subtract the predicted value from it
    # this gives us an error, or J(w0,w1) value
    return y_i - model_prediction(w0, w1, x_i)

def sum_of_squared_error_over_entire_dataset(w0, w1, training_examples):
    # find the squared error over the whole training set
    sum = 0
    for pair in training_examples:
        x_i = pair[0]
        y_i = pair[1]
        sum += prediction_error(w0,w1,x_i,y_i) ** 2
    return sum

if __name__ == "__main__":
    main()


#######################
###### TESTING ########
#######################