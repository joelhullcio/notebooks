# This example use bokeh to generate a line graph
# The graph is output to a html file.
# Open the html file in a browser to see the graph.
# 
# Use execfile('bokeh_line.py') to run this in IPython

import numpy as np
from bokeh.plotting import *

N = 80

x = np.linspace(0, 4*np.pi, N)
y = np.sin(x)

output_file("bokeh_line.html", title="Wakari bokeh_line.py Example")

line(x,y, color="#0000FF", tools="pan,wheel_zoom,box_zoom,reset,previewsave",
     name="line_example")

show()

