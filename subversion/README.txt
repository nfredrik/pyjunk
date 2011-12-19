Är det en repository taggning eller working copy?


fredrik@linux-f1uk:~/test> svn commit -m "hej hopp i galopp"
Adding         tags/DELIVERY_1_10
Adding         tags/DELIVERY_1_10/olle.txt

Committed revision 33.

Warning: post-commit hook failed (exit code 1) with no output.
fredrik@linux-f1uk:~/test> svn copy trunk/ tags/DELIVERY_1_11
A         tags/DELIVERY_1_11
fredrik@linux-f1uk:~/test> svn commit -m "hej hopp i galopp"
Adding         tags/DELIVERY_1_11
Adding         tags/DELIVERY_1_11/olle.txt

Committed revision 34.

Warning: post-commit hook failed (exit code 1) with output:
A   tags/DELIVERY_1_11/
D   tags/DELIVERY_1_11/olle.txt
A   tags/DELIVERY_1_11/olle.txt
