"""
    @author Anthony (Tony) Poerio
    @email adp59@pitt.edu
    CS1571 - Artificial Intelligence
    Prof. Rebecca Hwa
    Fall 2016
    HW04 - Linear Regression
"""

import sys
import ast
import itertools
import random
import numpy

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
        # read in all data
        # permute the examples, because they are currently sorted in some way
        # need to do a random(0,9) and if < 2 --> put in test set
        # get a training_set and test_set
        # get gradient descent variables
        print "--------TRAINING--------"
        training_set, test_set = get_training_and_test_set(sys.argv[1])
        # we'll then have a feature vector on each line --> normalize each data point so that all fall in range [0,1)
        print "Training Set: \n\n" + str(training_set)
        print "Test Set: \n\n" + str(test_set)
        # need to display outputs for at least 3 (aim for 5) different feature vector representations
        # and have some rationale for why, to use in writeup
        w0, ws = multivariate_gradient_descent(training_set)
        sum_of_sq_err = multivariate_sum_of_squared_error_over_entire_dataset(w0,ws,test_set)
        avg_sq_err = sum_of_sq_err/len(test_set)
        print "---------TESTING--------"
        print "USING MULTIPLE LINEAR REGRESSION"
        print "The AVERAGE Squared Error over the Entire Testing Data Set = "+str(avg_sq_err)
        print "The AVERAGE Overall Error For __any given prediction__ = "+str(numpy.sqrt(avg_sq_err))
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


####################################
##### MULTIVARIATE REGRESSION ######
####################################
def parse_data_multivariate(filename):
    # read all of the data
    with open(filename, 'r') as f:
        fileData = f.read()

    print fileData

    # split it on \n values
    fileData = fileData.split('\n')

    # strip all the \r values and make it a vector
    vectors = []
    for value in fileData:
        value = value.strip('\r')
        value = ast.literal_eval(value)
        value = list(value)
        vectors.append(value)

    return vectors

def normalize_vectors(vector_list):
    # create a dictionary to hold max for each dimension in our vector
    vector_max = {}
    # and initialize it to avoid key errors, as we iterate
    ex_vector = vector_list[0]
    for index in range(0, len(ex_vector)):
        vector_max[str(index)] = ex_vector[index]

    # now find the max value at each dimension so we can normalize
    for vector in vector_list:
        for index in range(0,len(vector)):
            if vector[index] > vector_max[str(index)]:
                vector_max[str(index)] = vector[index]

    # print vector for now, so we can see what's going on
    print str(vector_max)

    # normalize each item in the vector list, according to the max
    for vector in vector_list:
        for index in range(0, len(vector)):
            vector[index] = float(vector[index]) / float(vector_max[str(index)])

    print str(vector_list)
    return vector_list

def permute_vector_list(vector_list):
    # randomize the vector
    randomized_vector = random.sample(vector_list, len(vector_list))

    # and assert that we did not LOSE data
    assert len(vector_list) == len(randomized_vector)

    # and that the lists are not the same
    assert not vector_list == randomized_vector

    return randomized_vector


def get_training_and_test_set(filename):
    # get the raw feature vectors, whole list of them
    raw_feature_vectors = parse_data_multivariate(filename)

    # normalize the vectors first
    norm_vectors = normalize_vectors(raw_feature_vectors)

    # then permute them
    random_norm_vectors = permute_vector_list(norm_vectors)

    # then assign 80% training; 20% test, randomly
    training_set =[]
    test_set = []
    for vector in random_norm_vectors:
        random_num = random.randint(0,9)
        if random_num < 2:
            test_set.append(vector)
        else:
            training_set.append(vector)

    # assert that we aren't too far off of an 80/20 split
    assert float(len(test_set)) / float(len(random_norm_vectors)) > 0.15

    # get (x,y) pairs for all values
    training_tuples = []
    for vector in training_set:
        y = vector.pop()
        pair = (vector, y)
        training_tuples.append(pair)

    testing_tuples = []
    for vector in test_set:
        y = vector.pop()
        pair = (vector, y)
        testing_tuples.append(pair)

    # return our divided & normalized training and test sets
    return training_tuples, testing_tuples


# generalize to work with multiple variables
# update this to either be more general, or work for the number of variables used
# y_i = very last data point in each vector.
def multivariate_gradient_descent(training_examples, alpha=0.01):
    """
    Apply gradient descent on the training examples to learn a line that fits through the examples
    :param examples: set of all examples in (x,y) format
    :param alpha = learning rate
    :return:
    """
    # initialize the weight and x_vectors
    W = [0 for index in range(0, len(training_examples[0][0]))]
    X = [0 for index in range(0, len(training_examples[0][0]))]

    # set X_0 = 1, because W_0 is a constant
    X_0 = 1
    W_0 = 0

    # initialize w0 and w1 to some small value, here just using 0 for simplicity
    #w0 = 0
    #w1 = 0

    # repeat until "convergence", meaning that w0 and w1 aren't changing very much
    # --> need to define what 'not very much' means, and that may depend on problem domain
    convergence = False
    while not convergence:

        # initialize temporary variables, and set them to 0
        deltaW_0 = 0
        deltaW_n = [0 for x in range(0,len(training_examples[0][0]))]

        # initialize temporary variables, and set them to 0
        #delta_w0 = 0
        #delta_w1 = 0

        for pair in training_examples:
            # grab our data points from the example
            x_i = pair[0]
            y_i = pair[1]

            # calculate a prediction, and find the error
            #h_of_x_i = model_prediction(w0,w1,x_i)
            # needs to be an element-wise plus
            #pred_error = multivariate_prediction_error(W_0, y_i, W, x_i)
            deltaW_0 += multivariate_prediction_error(W_0, y_i, W, x_i)
            deltaW_n = numpy.multiply(numpy.add(deltaW_n, multivariate_prediction_error(W_0, y_i, W, x_i)), x_i)
            #print "CHANGE = " + str(deltaW_n)
            #delta_w1 += prediction_error(w0,w1,x_i,y_i)*x_i

        #print "DELTA_WN = " + str(deltaW_n)
        # store previous weighting values
        prev_w0 = W_0
        prev_Wn = W

        # get new weighting values
        W_0 = W_0 + alpha*deltaW_0
        W = numpy.add(W,numpy.multiply(alpha,deltaW_n))
        alpha -= 0.001

        # every few iterations print out current model
        #     1.  -->  (w0 + w1x1 + w2x2 + ... + wnxn)
        print "Current model is: ("+str(W_0)+" + "+str(W) #+"x1)"
        #     2.  -->  averaged squared error over training set, using the current line
        summed_error = sum_of_squared_error_over_entire_dataset(W_0, W, training_examples)
        avg_error = summed_error/len(training_examples)
        print "Average Squared Error="+str(avg_error)


        # check if we have converged
        if abs(prev_w0 - W_0) < 0.00001 and abs(numpy.subtract(prev_Wn, W)).all() < 0.00001:
            convergence = True

    # after convergence, print out the parameters of the trained model (w0, ... wn)
    print "Parameters of trained model are: w0="+str(W_0)+", weights="+str(W)
    return W_0, W


################################
##### MULTIVARIATE HELPERS #####
################################
# generalize these to just take a w0, a vector of weights, and a vector x-values
def multivariate_model_prediction(w0, weights, xs):
    return w0 + numpy.dot(weights, xs)

# again, this needs to take just a w0, vector of weights, and a vector of x-values
def multivariate_prediction_error(w0, y_i, weights, xs):
    # basically, we just take the true value (y_i)
    # and we subtract the predicted value from it
    # this gives us an error, or J(w0,w1) value
    return y_i - multivariate_model_prediction(w0, weights, xs)

# should be the same, but use the generalize functions above, and update the weights inside the vector titself
# also need to have a vector fo delta_Wn values to simplify
def multivariate_sum_of_squared_error_over_entire_dataset(w0, weights, training_examples):
    # find the squared error over the whole training set
    sum = 0
    for pair in training_examples:
        x_i = pair[0]
        y_i = pair[1]
        # cast back to values in range [1 --> 20]
        prediction = multivariate_model_prediction(w0,weights,x_i) / (1/20.0)
        actual = y_i / (1/20.0)
        error = abs(actual - prediction)
        error_sq = error ** 2
        # prediction_error = multivariate_prediction_error(w0,y_i,weights,x_i)
        sum += error_sq
        #sum += multivariate_prediction_error(w0,y_i,weights,x_i) ** 2
    return sum

if __name__ == "__main__":
    main()

