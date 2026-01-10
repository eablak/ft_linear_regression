# tmpθ0 = learningRate ∗ 1/m   m−1∑i=0(estimateP rice(mileage[i]) − price[i])
# tmpθ1 = learningRate ∗ 1/m   m−1∑i=0(estimateP rice(mileage[i]) − price[i]) ∗ mileage[i]

import pandas
import sys
import matplotlib.pyplot as plt


def get_dataset():
    try:
        return pandas.read_csv('dataset/data.csv')
        
    except:
        sys.exit("No dataset")


def plotting_data(dataset):
    plt.scatter(dataset.km, dataset.price)
    plt.show()


def loss_function(m, b, points):
    total_error = 0
    for i in range(len(points)):
        x = points.iloc[i].km
        y = points.iloc[i].price
        total_error += (y - (m*x + b)) **2
    total_error / float(len(points)) 


def gradient_descent(m_now, b_now, points, L):
    m_gradient = 0
    b_gradient = 0

    n = len(points)

    for i in range(n):
        x = points.iloc[i].km
        y = points.iloc[i].price

        m_gradient += -(2/n) * x * (y - (m_now * x + b_now))
        b_gradient += -(2/n) * (y - (m_now * x + b_now))

    m = m_now - L * m_gradient
    b = b_now - L * b_gradient

    return m, b


def trainModel(m, b, learningRate, epochs, dataset):
    for i in range(epochs):
        m, b = gradient_descent(m, b, dataset, learningRate)

    print(m, b)

def plotResult(dataset):
    plt.scatter(dataset.km, dataset.price, color="black")
    plt.plot(color="red")
    plt.show()



if __name__ == "__main__":
    dataset = get_dataset()
    # plotting_data(dataset)
    trainModel(0, 0, 0.0001, 1000, dataset)
    # plotResult(dataset)

    