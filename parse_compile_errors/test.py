import re
data="""
host node20007 
{
    hardware ethernet 00:22:38:8f:1f:43; 
    fixed-address node20007.domain.com;      
} 
"""

regex = re.compile(r""" 
                    (hardware[ ]ethernet \s+ 
                         (\S+) # MAC
                    ) ; 
                    \s+ # includes newline 
                    \S+ # variable(??) text e.g. "fixed-address" 
                    \s+ 
                    (\S+) # e.g. "node20007.domain.com"  ;  """, re.VERBOSE) 

print regex.search(data).groups() 
