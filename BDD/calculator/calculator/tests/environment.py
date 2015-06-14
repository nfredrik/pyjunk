from calculator.calculator import Calculator
def before_all(context):
    context.calc = Calculator()

def after_all(context):
    context.calc = None

