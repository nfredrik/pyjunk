from steps.customworld import CustomWorld


def before_all(context):
    # -- SET LOG LEVEL: behave --logging-level=ERROR ...
    # on behave command-line or in "behave.ini".

    # -- ALTERNATIVE: Setup logging with a configuration file.
    # context.config.setup_logging(configfile="behave_logging.ini")
    context.config.setup_logging()


    
    context.CustomWorld = CustomWorld()

def after_all(context):
    pass