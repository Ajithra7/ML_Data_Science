# importing the modules
from bokeh.plotting import figure, output_file, show
		
# instantiating the figure object
graph = figure(title = "Bokeh Wedge Graph")
	
# the points to be plotted
x = 0
y = 0

# radius of the wedge
radius = 15

# start angle of the wedge
start_angle = 1

# end angle of the wedge
end_angle = 2

# plotting the graph
graph.wedge(x, y, radius = radius,
			start_angle = start_angle,
			end_angle = end_angle)
	
# displaying the model
show(graph)
