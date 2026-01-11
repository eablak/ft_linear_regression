# estimatePrice(mileage) = θ0 + (θ1 ∗ mileage)
import sys


def get_parameters():
    try:
        file = open('output.txt')
        content = file.readlines()

        theta0 = content[0].strip()
        theta1 = content[1].strip()
    except:
        theta0, theta1 = 0, 0
    
    return theta0, theta1


def estimatePrice(theta0, theta1, milage):
    return theta0 + (theta1 * milage)
    

if __name__ == "__main__":

    if len(sys.argv) != 2:
        sys.exit("Write your milage as a argument!")

    try:
        float(sys.argv[1])
    except:
        sys.exit("Write only float")

    theta0, theta1 = get_parameters()
    print(estimatePrice(float(theta0), float(theta1), float(sys.argv[1])))
