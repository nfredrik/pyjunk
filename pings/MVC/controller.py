class Controller(object):
 
    def __init__(self, model=Model(), view=View()):
        self.model = model
        self.view  = view
 
    def getDefectSummary(self, defectid):
        summary_data = self.model.getSummary(defectid)
        self.view.summary(summary_data, defectid)
 
    def getDefectList(self, component):
        defectlist_data = self.model.getDefectList(component)
        self.view.defectList(defectlist_data, component)