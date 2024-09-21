import numpy as np 
from matplotlib import pyplot as plt
from matplotlib import style
def main():
    # x and y data list
    x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    y = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # set plot style
    style.use('ggplot')
    # line plot example
    plt.plot(x, y, label="line plot example", linewidth=2)
    plt.legend()
    plt.grid(True,color="k")
    plt.ylabel('y axis')
    plt.xlabel('x axis')
    plt.title('Line Plot')
    plt.show()
    print("Hello")

if __name__ == '__main__':
    main()
python -m pip install -U pip
