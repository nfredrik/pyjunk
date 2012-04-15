from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis



class PlotObject(object):

    def __init__(self):

        # Set the vertical range from 0 to 100
        factor = 8 - 1 
        max_y = 20 * factor
        # Chart size of 200x125 pixels and specifying the range for the Y axis
        self.chart = SimpleLineChart(40*factor, 25*factor, y_range=[0, max_y])


        # Set the line colour to blue
        self.chart.set_colours(['0000FF'])

        # Set the vertical stripes
        self.chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)

        # Set the horizontal dotted lines
        #self.chart.set_grid(0, 5*factor, factor, factor)

        # The Y axis labels contains 0 to 100 skipping every 25, but remove the
        # first number because it's obvious and gets in the way of the first X
        # label.
        left_axis = range(0, max_y + 1, 5 * factor)
        left_axis[0] = ''
        self.chart.set_axis_labels(Axis.LEFT, left_axis)

        # X axis labels
        self.chart.set_axis_labels(Axis.BOTTOM, \
#        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
        ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    def plot(self, data):

        self.chart.add_data(data)

        self.chart.download('misse.png')


if __name__ == '__main__':
  plotobj = PlotObject()

  # Add the chart data
  data = [        32, 34, 34, 32, 34, 34, 32, 32, 32, 34, 34, 32, 29, 29, 34, 34, 34, 37,
                  37, 39, 42, 47, 50, 54, 57, 60, 60, 60, 60, 60, 60, 60, 62, 62, 60, 55,
                  55, 52, 47, 44, 44, 40, 40, 37, 34, 34, 32, 32, 32, 31, 32
         ]

  plotobj.plot(data)

