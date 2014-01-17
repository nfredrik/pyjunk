
from savejson import save_json, JSONFILE
 

from nph import get_the_prices

current = get_the_prices()

save_json(current)

print 'the end'