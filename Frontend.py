import matplotlib
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random
import time
import threading

class Graph:
	
    # Initialize Graph Object
    def __init__(self):
	# Declare the arrays for all graphs
        self.graphs = []
	# Initialize the Figure
        self.fig = plt.figure()
	# Set some spacing for the Figure
        plt.subplots_adjust(left=0.1, bottom=0.1, right=0.95, top=0.95, hspace=0.45)
        return
	
    def addGraph(self, title, xlabel, ylabel):
	# Change the Geometry of already existing Graphs
        count = len(self.fig.axes)
        for i in range(count):
            self.fig.axes[i].change_geometry(count + 1, 1, i + 1)
		
	# Add a new "subplot" aka Graph to the Figure
        axes = self.fig.add_subplot(count + 1, 1, count + 1)
		
	# Set Title, X-Label and Y-Label
        axes.set_title(title)
        axes.set_xlabel(xlabel)
        axes.set_ylabel(ylabel)
		
	# Create Info-Dictionary
        info = {
            'axes': axes,
            'line': [],
            'data': []
        }
	# Add it to the graphs-Array
        self.graphs.append(info)
		
	# Return the "ID" of the Graph
        return len(self.graphs) - 1
	
    # Returns the Graph
    def getGraph(self, id):
        return self.graphs[id]

    # Add Data to the Graph
    def addData(self, id, values, labels):
	# If there are more than two lines
        if(isinstance(labels, list)):
	    # Check if there are already two lines
            if(len(self.getGraph(id)['line']) < len(labels)):
		# If not add them
                for label in labels:
		    # Get the Axes
                    axes = self.getGraph(id)['axes']
		    # Create the lines
                    line, = axes.plot([], [], label=label)
		    # Add them to the Graph-Dictionary
                    self.getGraph(id)['line'].append(line)
		    # Show the Legend
                    axes.legend()
        else:
	    # If there is only one line, check if the line exists
            if(len(self.getGraph(id)['line']) == 0):
 		# If not create it
                axes = self.getGraph(id)['axes']
                line, = axes.plot([], [], label=labels)
                self.getGraph(id)['line'].append(line)
                axes.legend()
		
	# Set the Data 
        self.getGraph(id)['data'] = values
        return

    def showGraph(self):
	# Update Function
        def update(frame):
	    # For every Graph
            for info in self.graphs:
		# Check if Data exists
                if (len(info['data']) != 0):
		    # If there is more than one Data-Set
                    if (isinstance(info['data'][0], list)):
			# If the Data-Set contains Data
                        if (len(info['data'][0]) != 0):
			    # Add it to the Line
                            for i, data in enumerate(info['data']):
                                info['line'][i].set_data(range(len(data)), data)
				# Adjust X and Y - Lim
                                info['axes'].set_xlim(0, len(data))
                                if(info['axes'].get_ylim()[1] < data[len(data) - 1]):
                                    info['axes'].set_ylim(0, data[len(data) - 1] + 10)
                    else:
			# If there is only one Data-Set, add it to the line
                        info['line'][0].set_data(range(len(info['data'])), info['data'])
			# And adjust the X and Y - Lim
                        info['axes'].set_xlim(0, len(info['data']))
                        if(info['axes'].get_ylim()[1] < info['data'][len(info['data']) - 1]):
                            info['axes'].set_ylim(0, info['data'][len(info['data']) - 1] + 10)
		
	# Start the "Animation" with 60 Frames => every iteration calls the Update function 60 times
        ani = FuncAnimation(self.fig, update, frames=60)
		
	# Show the Graph
        plt.show()
        return

# ---------------------------------------Testing Area---------------------------------------
# Thread - Function
# Args: Graph - Object, ID - First Graph, ID - Second Graph
def addValues(graph, valueGraph, lossGraph):
    predicted = []
    real = []

    loss = []
	
    # Simulate Values for all Graphs
    for i in range(0, 20):
        predicted.append(random.randrange(10))
        real.append(random.randrange(10))

        loss.append(random.randrange(100))
		
	# First Graph has 2 Lines
        graph.addData(valueGraph, [predicted, real], ["Predicted", "Real"])
        graph.addData(lossGraph, loss, "Loss")
		
	# Sleep 1 second
        time.sleep(1)

if __name__ == "__main__":
    # Create Object
    graph = Graph()
    # Create both Graphs
    valueGraph = graph.addGraph("Bitcoin", "Time (sec)", "Value (€)")
    lossGraph = graph.addGraph("Loss - Function", "Time (sec)", "Loss (%)")
	
    # Create and start the Thread 
    # Is needed because graph.showGraph() stops the Main-Thread and can't be executed on another thread
    thread = threading.Thread(target=addValues, args=(graph, valueGraph, lossGraph))
    thread.start()
	
    # Show the Graph
    graph.showGraph()

    # Wait for the termination of the thread
    thread.join()
