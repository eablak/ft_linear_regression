# tmpθ0 = learningRate ∗ 1/m   m−1∑i=0(estimatePrice(mileage[i]) − price[i])
# tmpθ1 = learningRate ∗ 1/m   m−1∑i=0(estimatePrice(mileage[i]) − price[i]) ∗ mileage[i]
import pandas
import sys
import matplotlib.pyplot as plt
from sklearn.preprocessing import minmax_scale
import numpy as np


def get_dataset():
    try:
        return pandas.read_csv('dataset/data.csv')
    except:
        sys.exit("No dataset")


def normalize_dataset(dataset):

    normalized = dataset.copy()
    normalized['km'] = minmax_scale(dataset['km'])
    return normalized


def train_model(theta0, theta1, learning_rate, epochs, X, y):

    m = len(X)

    for i in range(epochs):
        prediction = theta0 + (theta1 * X)
        error = prediction - y

        tmp_theta0 = (1/m) * np.sum(error)
        tmp_theta1 = (1/m) * np.sum(error*X)

        theta0 -= learning_rate * tmp_theta0
        theta1 -= learning_rate * tmp_theta1

    return (theta0, theta1)


def denormalize_theta(normalized_theta0, normalized_theta1, dataset):
    theta1 = normalized_theta1 / (dataset['km'].max() - dataset['km'].min())
    theta0 = normalized_theta0 - (theta1 * dataset['km'].min())

    return theta0, theta1


def save_into_file(theta0, theta1):
    with open("output.txt", "w") as f:
        f.write(str(theta0) + "\n" + str(theta1))



if __name__ == "__main__":

    theta0 = 0
    theta1 = 0
    learning_rate = 0.001
    epochs = 10000

    dataset = get_dataset()
    normalized_dataset = normalize_dataset(dataset)
    X = normalized_dataset.iloc[:, 0].values
    y = dataset.iloc[:, 1].values

    normalized_theta0, normalized_theta1 = train_model(theta0, theta1, learning_rate, epochs, X, y)
    theta0, theta1 = denormalize_theta(normalized_theta0, normalized_theta1, dataset)
    save_into_file(theta0, theta1)