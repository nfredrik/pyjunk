from pygooglechart import Chart
from pygooglechart import SimpleLineChart
from pygooglechart import Axis



class PlotObject(object):

    def __init__(self):

        # Set the vertical range from 0 to 100
        factor = 8 - 1 
        max_y = 20 * factor
        max_x = 250
        # Chart size of 200x125 pixels and specifying the range for the Y axis
        self.chart = SimpleLineChart(width=50*factor, height=25*factor, 
                                     title='ping ftp.sunet.se',
#                                     legend=True,
                                     x_range=[0, max_x],                                      
                                     y_range=[0, max_y])


        # Set the line colour to blue
        self.chart.set_colours(colours=['0000FF'])

        # Set the vertical stripes:arguments area, angle etc.
        #self.chart.fill_linear_stripes(Chart.CHART, 0, 'CCCCCC', 0.2, 'FFFFFF', 0.2)

        # Set the horizontal dotted lines
        #self.chart.set_grid(x_step=0, y_step=5*factor, line_segment=factor, blank_segment=factor)

        # The Y axis labels contains 0 to 100 skipping every 25, but remove the
        # first number because it's obvious and gets in the way of the first X
        # label.
        left_axis = range(0, max_y + 1, 25)
        left_axis[0] = ''
        self.chart.set_axis_labels(axis_type=Axis.LEFT, values=left_axis)

        # X axis labels
        self.chart.set_axis_labels(axis_type=Axis.BOTTOM, \
#        ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'])
        values= [ ' ', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

    def list(self, list):

        self.chart.add_data(data=list)

        self.chart.download(file_name='misse.png')


if __name__ == '__main__':
  plotobj = PlotObject()

  # Add the chart data
  data = [        32, 34, 34, 32, 34, 34, 32, 32, 32, 34, 34, 32, 29, 29, 34, 34, 34, 37,
                  37, 39, 42, 47, 50, 54, 57, 60, 60, 60, 60, 60, 60, 60, 62, 62, 60, 55,
                  55, 52, 47, 44, 44, 40, 40, 37, 34, 34, 32, 32, 32, 31, 32
         ]

  plotobj.plot(data)

