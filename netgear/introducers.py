import pygeoip

gi4 = pygeoip.GeoIP('GeoLiteCity.dat', pygeoip.MEMORY_CACHE)

print 'help'

print gi4.country_code_by_name('172.22.1.45')