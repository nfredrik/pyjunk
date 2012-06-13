import re

l = ["555-8396 Neu, Allison", 
     "Burns, C. Montgomery", 
     "555-5299 Putz, Lionel",
     "555-7334 Simpson, Homer Jay"]

for i in l:
    res = re.search(r"([0-9-]*)\s*([A-Za-z]+),\s+(.*)", i)
    print res.group(3) + " " + res.group(2) + " " + res.group(1)
    print res.group(1)


example_codes = ["SW1A 0AA", # House of Commons
                 "SW1A 1AA", # Buckingham Palace
                 "SW1A 2AA", # Downing Street
                 "BX3 2BB", # Barclays Bank
                 "DH98 1BT", # British Telecom
                 "N1 9GU", # Guardian Newspaper
                 "E98 1TT", # The Times
                 "TIM E22", # a fake postcode
                 "A B1 A22", # not a valid postcode
                 "EC2N 2DB", # Deutsche Bank
                 "SE9 2UG", # University of Greenwhich
                 "N1 0UY", # Islington, London
                 "EC1V 8DS", # Clerkenwell, London
                 "WC1X 9DT", # WC1X 9DT
                 "B42 1LG", # Birmingham
                 "B28 9AD", # Birmingham
                 "W12 7RJ", # London, BBC News Centre
                 "W12 7EJ", # London, BBC News Centre
                 "BBC 007" # a fake postcode
                ]

#pc_re = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABD-HJLNP-UW-Z]{2}"
pc_re = r"[A-z]{1,2}[0-9R][0-9A-Z]? [0-9][ABDHJLNPUWZ]{2}"

for postcode in example_codes:
    r = re.search(pc_re, postcode)
    if r:
        print postcode + " matched!"
    else:
        print postcode + " is not a valid postcode!"
