from model import Model
from view import View

class Control(object):

    def __init__(self, model= Model(), view = View()):
        self.model = model
        self.view = view

    def get_list(self):
        self.list = self.model.get_date_4_object(object='oracle.com')
        self.view.list(list=self.list)
