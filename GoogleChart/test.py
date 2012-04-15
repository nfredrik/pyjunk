from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis

# Set the vertical range from 0 to 100
max_y = 100

# Chart size of 200x125 pixels and specifying the range for the Y axis
chart = SimpleLineChart(200, 125, y_range=[0, max_y])

# Add the chart data
data = [
    32, 34, 34, 32, 34, 34, 32, 32, 32, 34, 34, 32, 29, 29, 34, 34, 34, 37,
    37, 39, 42, 47, 50, 54, 57, 60, 60, 60, 60, 60, 60, 60, 62, 62, 60, 55,
    55, 52, 47, 44, 44, 40, 40, 37, 34, 34, 32, 32, 32, 31, 32
]
chart.add_data(data)

# Set the line colour to blue
chart.set_colours(['0000FF'])

# Set the vertical stripes
chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)

# Set the horizontal dotted lines
chart.set_grid(0, 25, 5, 5)

# The Y axis labels contains 0 to 100 skipping every 25, but remove the
# first number because it's obvious and gets in the way of the first X
# label.
left_axis = range(0, max_y + 1, 25)
left_axis[0] = ''
chart.set_axis_labels(Axis.LEFT, left_axis)

# X axis labels
chart.set_axis_labels(Axis.BOTTOM, \
    ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])

chart.download('line-stripes.png')
