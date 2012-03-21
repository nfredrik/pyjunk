from pre_commit_no_commit import main
from mock import Mock

from command import Command

assert True

cmds = Mock()
print 'testing with cm'
cmds.get_string_output.return_value = 'cm\n'
assert (main(repos='/srv/repos/svn/kalle', txn= '37', cmds=cmds) == 0)

print 'testing with cm'
cmds.get_string_output.return_value = 'cm\n'
assert (main(repos='/srv/repos/svn/trunk', txn= '37', cmds=cmds) == 0)

cmds2 = Mock()
print 'testing with fsv'
cmds2.get_string_output.return_value = 'fsv\n'
assert main(repos='/srv/repos/svn/nisse', txn= '73', cmds=cmds2) == 0

cmds2 = Mock()
print 'testing with fsv'
cmds2.get_string_output.return_value = 'fsv\n'
assert main(repos='/srv/repos/svn/trunk', txn= '73', cmds=cmds2) != 0


#cmds3 =Command(SVNLOOK +' author -r '+ 40 + ' ' + '/srv/repos/')
#assert main(repos='/srv/repos/svn/nisse', txn= '73', cmds=cmds3) != 0


