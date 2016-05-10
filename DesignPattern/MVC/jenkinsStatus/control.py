import sys

class Control:

  def __init__(self,model, view):
    self.model = model
    self.view = view

  def get_status(self):
    nn = self.model.get_status()
    self.view.expose_it(nn)


class Model:
  def __init__(self, config):
    self.config = config

  def get_status(self):
    return 42

class View:

  def __init__(self):
    pass

  def expose_it(self, nn):
    print(nn)



def main(args):

  # Could be a connection or a file (fed by another polling script)
  model = Model('config')
  
  # Could be a CLI or a GUI using tkinter
  view = View()

  control = Control(model, view)

  control.get_status()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:] or 0))
