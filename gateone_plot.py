# This example shows how to use matplotlib and plot directly in
# the GateOne terminal or IPython session.
#
# Use execfile('gateone_ploy.py') in IPython to run this example.

import sys
import matplotlib
matplotlib.use('Agg')
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
import pylab

fig = Figure()
canvas = FigureCanvasAgg(fig)
ax = fig.add_subplot(111)
x = pylab.randn(1000)
ax.hist(x, 100)
ax.set_title('Wakari Inline Matplotlib Example')
canvas.print_figure(sys.stdout)

