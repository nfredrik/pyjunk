from steps.customworld import CustomWorld


def before_all(context):
    context.CustomWorld = CustomWorld()

def after_all(context):
    pass