import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from math import factorial
from scipy.special import erfinv, comb
from scipy.stats import uniform, binom, norm
from dataclasses import dataclass
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt

import utils


def uniform_generator(a, b, num_samples=100):
    """
    Generates an array of uniformly distributed random numbers within the specified range.

    Parameters:
    - a (float): The lower bound of the range.
    - b (float): The upper bound of the range.
    - num_samples (int): The number of samples to generate (default: 100).

    Returns:
    - array (ndarray): An array of random numbers sampled uniformly from the range [a, b).
    """

    np.random.seed(42)

    ### START CODE HERE ###
    array = np.random.uniform(a, b, num_samples)
    ### END CODE HERE ###

    return array


data = uniform_generator(0.0, 1.0)
# plt.hist(data, bins=20, color="blue", alpha=0.7)
# plt.title("Histogram of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


def inverse_cdf_gaussian(y, mu, sigma):
    """
    Calculates the inverse cumulative distribution function (CDF) of a Gaussian distribution.

    Parameters:
    - y (float or ndarray): The probability or array of probabilities.
    - mu (float): The mean of the Gaussian distribution.
    - sigma (float): The standard deviation of the Gaussian distribution.

    Returns:
    - x (float or ndarray): The corresponding value(s) from the Gaussian distribution that correspond to the given probability/ies.
    """
    ### START CODE HERE ###

    x = sigma * np.sqrt(2) * erfinv(2 * y - 1) + mu
    ### END CODE HERE ###

    return x


# data = inverse_cdf_gaussian(data, 0, 1)
# plt.hist(data, bins=20, color="blue", alpha=0.7)
# plt.title("Histogram of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


def gaussian_generator(mu, sigma, num_samples):
    ### START CODE HERE ###

    # Generate an array with num_samples elements that distribute uniformally between 0 and 1
    u = uniform_generator(0, 1, num_samples)

    # Use the uniform-distributed sample to generate Gaussian-distributed data
    # Hint: You need to sample from the inverse of the CDF of the distribution you are generating
    array = inverse_cdf_gaussian(u, mu, sigma)
    ### END CODE HERE ###

    return array


# data = gaussian_generator(0, 1, 100)
# plt.hist(data, bins=20, color="blue", alpha=0.7)
# plt.title("Histogram of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


def inverse_cdf_binomial(y, n, p):
    """
    Calculates the inverse cumulative distribution function (CDF) of a binomial distribution.

    Parameters:
    - y (float or ndarray): The probability or array of probabilities.
    - n (int): The number of trials in the binomial distribution.
    - p (float): The probability of success in each trial.

    Returns:
    - x (float or ndarray): The corresponding value(s) from the binomial distribution that correspond to the given probability/ies.
    """

    ### START CODE HERE ###
    x = binom.ppf(y, n, p)
    ### END CODE HERE ###

    return x


# data = inverse_cdf_binomial(data, 100, 0.5)
# plt.hist(data, bins=20, color="blue", alpha=0.7)
# plt.title("Histogram of Data")
# plt.xlabel("Value")
# plt.ylabel("Frequency")
# plt.show()


def binomial_generator(n, p, num_samples):
    """
    Generates an array of binomially distributed random numbers.

    Args:
        n (int): The number of trials in the binomial distribution.
        p (float): The probability of success in each trial.
        num_samples (int): The number of samples to generate.

    Returns:
        array: An array of binomially distributed random numbers.
    """
    ### START CODE HERE ###

    # Generate an array with num_samples elements that distribute uniformally between 0 and 1
    u = uniform_generator(0, 1, num_samples)

    # Use the uniform-distributed sample to generate binomial-distributed data
    # Hint: You need to sample from the inverse of the CDF of the distribution you are generating
    array = inverse_cdf_binomial(u, n, p)
    ### END CODE HERE ###

    return array


data = binomial_generator(50, 0.5, 100)
plt.hist(data, bins=20, color="blue", alpha=0.7)
plt.title("Histogram of Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# FEATURES = ["height", "weight", "bark_days", "ear_head_ratio"]

# pre_loaded_df = pd.read_pickle("df_all_breeds.pkl")

# try:
#     # Generate the dataset using the graded functions from section 1
#     df_all_breeds = utils.generate_data(
#         gaussian_generator, binomial_generator, uniform_generator
#     )
# except:
#     # In case of an error
#     print(
#         "There was an error when generating the dataset using the generator functions.\n\nFalling back to the pre-loaded one."
#     )
#     df_all_breeds = pre_loaded_df
# else:
#     # In case that the generated dataset does not match the pre-loaded one
#     if not df_all_breeds.equals(pre_loaded_df):
#         print(
#             "The dataset generated from the generator functions is not identical to the expect one.\n\nFalling back to the pre-loaded one."
#         )
#         df_all_breeds = pre_loaded_df


# # Define a 70/30 training/testing split
# split = int(len(df_all_breeds) * 0.7)

# # Do the split
# df_train = df_all_breeds[:split].reset_index(drop=True)
# df_test = df_all_breeds[split:].reset_index(drop=True)


# def pdf_uniform(x, a, b):
#     """
#     Calculates the probability density function (PDF) for a uniform distribution between 'a' and 'b' at a given point 'x'.

#     Args:
#         x (float): The value at which the PDF is evaluated.
#         a (float): The lower bound of the uniform distribution.
#         b (float): The upper bound of the uniform distribution.

#     Returns:
#         float: The PDF value at the given point 'x'. Returns 0 if 'x' is outside the range [a, b].
#     """
#     ### START CODE HERE ###
#     pdf = uniform.pdf(x, a, b)
#     ### END CODE HERE ###

#     return pdf


# def pdf_gaussian(x, mu, sigma):
#     """
#     Calculate the probability density function (PDF) of a Gaussian distribution at a given value.

#     Args:
#         x (float or array-like): The value(s) at which to evaluate the PDF.
#         mu (float): The mean of the Gaussian distribution.
#         sigma (float): The standard deviation of the Gaussian distribution.

#     Returns:
#         float or ndarray: The PDF value(s) at the given point(s) x.
#     """

#     ### START CODE HERE ###
#     pdf = norm.pdf(x, mu, sigma)
#     ### END CODE HERE ###

#     return pdf


# def pmf_binomial(x, n, p):
#     """
#     Calculate the probability mass function (PMF) of a binomial distribution at a specific value.

#     Args:
#         x (int): The value at which to evaluate the PMF.
#         n (int): The number of trials in the binomial distribution.
#         p (float): The probability of success for each trial.

#     Returns:
#         float: The probability mass function (PMF) of the binomial distribution at the specified value.
#     """

#     ### START CODE HERE ###
#     pmf = binom.pmf(x, n, p)
#     ### END CODE HERE ###

#     return pmf


# train_params = utils.compute_training_params(df_train, FEATURES)


# def compute_breed_proportions(df):
#     """
#     Computes the estimated probabilities of each breed.

#     Args:
#         df (pandas.DataFrame): The dataframe containing the training data.

#     Returns:
#         - probs_dict (dict): A dictionary that contains the proportion of data belonging to each breed.
#     """

#     probs_dict = {}

#     ### START CODE HERE ###

#     # Loop over the breeds
#     for i in sorted(list(set(df.breed))):
#         # Slice the original df to only include data for the current breed
#         # You can use the syntax df[df['breed'] == group] replacing group with the corresponding variable
#         df_breed = df[df["breed"] == i]

#         # Compute the probability of each class (breed)
#         # You can get the number of rows in a dataframe by using len(dataframe)
#         prob_class = len(df_breed) / len(df)

#         # Save the probability of each class (breed) in the probabilities dict rouding to 3 decimal places
#         probs_dict[i] = round(prob_class, 3)

#     ### END CODE HERE ###

#     return probs_dict


# def prob_of_X_given_C(X, features, breed, params_dict):
#     """
#     Calculate the conditional probability of X given a specific breed, using the given features and parameters.

#     Args:
#         X (list): List of feature values for which the probability needs to be calculated.
#         features (list): List of feature names corresponding to the feature values in X.
#         breed (str): The breed for which the probability is calculated.
#         params_dict (dict): Dictionary containing the parameters for different breeds and features.

#     Returns:
#         float: The conditional probability of X given the specified breed.
#     """
# #     print(f"X: {X}")
# #     print(f"features: {features}")
# #     print(f"breed: {breed}")
# #     print(f"params_dict: {params_dict}")

#     if len(X) != len(features):
#         print("X and list of features should have the same length")
#         return 0


#     probability = 1.0

#     ### START CODE HERE ###

#     for feature_val, feature_name in zip(X, features):
# #         print(f"feature_val={feature_val},feature_name={feature_name} ")
#         # Match the current feature based on its name
#         match feature_name:
#             case "height" | "weight":
#                 # Get the relevant parameters out of the params_dict dictionary
#                 mu = params_dict[breed][feature_name]["mu"]
#                 sigma = params_dict[breed][feature_name]["sigma"]

#                 # Compute the relevant pdf given the distribution and the estimated parameters
#                 probability_f = pdf_gaussian(feature_val, mu, sigma)

#             case "bark_days":
#                 # Get the relevant parameters out of the params_dict dictionary
#                 n = params_dict[breed][feature_name]["n"]
#                 p = params_dict[breed][feature_name]["p"]

#                 # Compute the relevant pmf given the distribution and the estimated parameters
#                 probability_f = pmf_binomial(feature_val, n, p)

#             case "ear_head_ratio":
#                 # Get the relevant parameters out of the params_dict dictionary
#                 a = params_dict[breed][feature_name]["a"]
#                 b = params_dict[breed][feature_name]["b"]

#                 # Compute the relevant pdf given the distribution and the estimated parameters
#                 probability_f = pdf_gaussian(feature_val, mu, sigma)

#         # Multiply by probability of current feature
#         probability *= probability_f

#     ### END CODE HERE ###

#     return probability


# example_dog = df_test[FEATURES].loc[0]
# example_breed = df_test[["breed"]].loc[0]["breed"]
# print(f"Example dog has breed {example_breed} and features: height = {example_dog['height']:.2f}, weight = {example_dog['weight']:.2f}, bark_days = {example_dog['bark_days']:.2f}, ear_head_ratio = {example_dog['ear_head_ratio']:.2f}\n")

# print(f"Probability of these features if dog is classified as breed 0: {prob_of_X_given_C([*example_dog], FEATURES, 0, train_params)}")
# print(f"Probability of these features if dog is classified as breed 1: {prob_of_X_given_C([*example_dog], FEATURES, 1, train_params)}")
# print(f"Probability of these features if dog is classified as breed 2: {prob_of_X_given_C([*example_dog], FEATURES, 2, train_params)}")
