import pysvn
client = pysvn.Client()
entry_list = client.ls('.')
