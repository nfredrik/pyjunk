import commands

"""
Module to handle shell commands in a neat way.
"""


class Command(object):
    """
    Execute shell command and take care of output.
    """
    def __init__(self, cmd):
        (self.status, self.output) = commands.getstatusoutput(cmd)

    def get_status(self):
        """
        Get status of command execution.
        """
        return self.status

    def get_string_output(self):
        """
        Get output of command execution in string format.
        """
        return self.output

    def get_list_output(self):
        """
        Get output of command execution in list format.
        """
        return self.output.split()
