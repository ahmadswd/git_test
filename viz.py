import matplotlib as plt

def plot_this(x_data, y_data):
    try:
        plt.plot(x_data, y_data)
        print("Success rendering plot")
    except Exception as e:
        print(e)