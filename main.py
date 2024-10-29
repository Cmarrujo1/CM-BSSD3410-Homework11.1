from sklearn.datasets import load_iris

def load_data():
    iris = load_iris()

    cutoff = list(iris.target).index(2)
    iris.data = iris.data[:cutoff]
    iris.target = iris.taret[:cutoff]
    return iris

def sum_row(row):
    return sum(row)

def average(data):
    size = data.shape[0]
    sum = 0
    for row in range(size):
        sum += sum_row(data[row])
    return sum/size

def test(data, ans, tol):
    for row in_data:
        sum = sum_row(row)
        result = sum + tol > ans and sum - tol < ans
        print(result)


def main():
    iris = load_data()

    versic_idx = list(iris.target).index(1)
    sertosa = iris.data[:versic_idx]
    versic = iris.data[versic_idx:]

    sertosa_train = sertosa[:int(len(sertosa)*.8)]
    sertosa_test = sertosa[:int(len(sertosa) * .8):]

    versic_train = versic[:int(len(versic) * .8)]
    versic_test = versic[:int(len(versic) * .8):]

    test(sertosa_test, average(sertosa_train), 1)
    test(versic_test, average(sertosa_train), 1)

    test(versic_test, average(versic_train), 1)
    test(sertosa_test, average(versic_train), 1)


if __name__ == "__main__":
    main()