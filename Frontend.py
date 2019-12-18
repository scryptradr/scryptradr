import matplotlib.pyplot as plt

# TODO Show Loss Graph

# Initialize Graph
def initGraph():
    # Set Title and X/Y-Label
    plt.title("BitCoin - Course")
    plt.xlabel("Time (sec)")
    plt.ylabel("Value (€)")

    # Show the Graph
    plt.show()
    return

def drawGraph(predicted, real):
    # Add predicted and real Values to the Graph
    plt.plot(range(len(predicted)), predicted, label="Predicted")
    plt.plot(range(len(real)), real, label="Real")
    # Show the legend
    plt.legend()
    # Update Graph, run GUI Loop during pause
    plt.pause(0.05)
    return