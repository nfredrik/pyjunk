
class PdfWriter(object):
    def drawstring(self, text):
        pass
    def endpage(self):
        pass


# Inherit is inflexible
class PdfReportInherit(PdfWriter):
    def make_report(self):
        self.drawstring(self, title)
        for t in self.lines:
            self.drawstring(t)
        self.endpage()


# Composition gives you options nad mockability

class PdfReport:
    def __init__(self, pdf=None):
        self.pdf = pdf or PdfWiter()

    def make_report(self):
        self.pdf.drawstring(self, title)
        for t in self.lines:
            self.pdf.drawstring(t)
        self.pdf.endpage()
