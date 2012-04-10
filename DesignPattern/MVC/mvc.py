import sqlite3
 
class DefectModel(object):
 
    def getDefectList(self, component):
        query = '''select ID from defects where Component = '%s' ''' %component
        defectlist = self._dbselect(query)
        list = []
        for row in defectlist:
            list.append(row[0])
        return list
 
    def getSummary(self, id):
        query = '''select summary from defects where ID = '%d' ''' % id
        summary = self._dbselect(query)
        for row in summary:
            return row[0]
 
    def _dbselect(self, query):
        connection = sqlite3.connect('./TMS')
        cursorObj = connection.cursor()
        cursorObj.execute(query)
        return cursorObj.fetchall()
 
class DefectView(object):
 
    def summary(self, summary, defectid):
        print "#### Defect Summary for defect# %d####\n%s" % (defectid,summary)

    def defectList(self, list, category):
        print "#### Defect List for %s ####" % category
        for defect in list:
            print defect
 
class Controller(object):
 
    def __init__(self, model=DefectModel(), view=DefectView()):
        self.model = model
        self.view  = view
 
    def getDefectSummary(self, defectid):
        summary_data = self.model.getSummary(defectid)
        return self.view.summary(summary_data, defectid)
 
    def getDefectList(self, component):
        defectlist_data = self.model.getDefectList(component)
        return self.view.defectList(defectlist_data, component)
