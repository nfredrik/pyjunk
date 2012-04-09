import mvc
controller = mvc.Controller()
 
# Displaying Summary for defect id # 2
print controller.getDefectSummary(2)
 
# Displaying defect list for 'ABC' Component
print controller.getDefectList('ABC')