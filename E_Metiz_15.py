# Визуализация данных
import matplotlib.pyplot as plt


def print_plot():
    input_values = [1, 2, 3, 4, 5]
    squares = [1, 4, 9, 16, 25]
    # x - y
    plt.plot(input_values, squares, linewidth=5)

    plt.title("Sqaure Numbers", fontsize=12)
    plt.xlabel("Value", fontsize=12)
    plt.ylabel("Sqaure", fontsize=12)

    plt.tick_params(axis='both', labelsize=14)

    plt.show()


def print_scatter():
    one_group = [11, 22, 33, 44]
    two_group = [1, 2, 3, 4]
    plt.scatter(2, 3, c='black', s=100)
    plt.scatter(one_group, two_group, c=two_group, cmap=plt.cm.Blues, edgecolors='none', s=150)
    plt.axis([0, 110, 0, 22])
    # plt.savefig('squares_plot.png', bbox_inches='tight')
    plt.show()


# 15-1 15-2
def print_kub(value: int):
    one_group = list(range(value))
    two_group = [x ** 3 for x in one_group]

    plt.scatter(one_group, two_group, c=two_group, cmap=plt.cm.Oranges, edgecolors='none', s=10)
    plt.show()


# print_plot()
# print_scatter()
print_kub(int(input("Input value: ")))
