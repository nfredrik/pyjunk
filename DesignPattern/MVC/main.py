import mvc
from mock import Mock

controller = mvc.Controller()
 
# Displaying Summary for defect id # 2
controller.getDefectSummary(2)
controller.getDefectSummary(1)
controller.getDefectSummary(3)
 
# Displaying defect list for 'ABC' Component
controller.getDefectList('ABC')


# Displaying defect list for 'XYZ' Component
controller.getDefectList('XYZ')


MockModel = Mock()

MockModel.getDefectList.return_value = ['37','98']
MockModel.getSummary.return_value = 33


controller1 = mvc.Controller(model=MockModel())

print 'Mocking'

controller1.getDefectSummary(3)
controller1.getDefectList('XYZ')
