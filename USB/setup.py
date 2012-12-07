
import sys
sys.path.append(r'C:\Users\Assaf\MyProjects\USBEmailNotifier\pywinusb\pywinusb')
from distutils.core import setup
import py2exe

setup(
            options = {"py2exe" : {
                "packages" : "pywinusb" }},
            version = "1.0.0",
            description = "Usb Mail Notifier Controller",
            name = "controlMailLED",
            windows = ["controlMailLED.pyw"]
            )
