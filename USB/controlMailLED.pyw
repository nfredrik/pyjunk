import sys
from pywinusb import hid

if len( sys.argv ) != 2:
    print "Need a color id"
    sys.exit( 1 )

color = int( sys.argv[ 1 ] )

# Evelop device
devices = hid.HidDeviceFilter( vendor_id = 0x1294, product_id = 0x1320 ).get_devices()
if 0 != len(devices):
    device = devices[ 0 ]
    if device is None:
        print "Device not found"
        sys.exit( 1 )
    device.open()
    report = device.find_output_reports()[ 0 ]
    report[ 0xff000001 ][ 0 ] = color
    report.send()
    device.close()
    sys.exit(0)

# Airplain device
devices = hid.HidDeviceFilter(vendor_id=0xc45, product_id=0x826).get_devices()
if 0 != len(devices):
    for device in devices:
        device.open()
        reports = device.find_output_reports()
        if 0 != len(reports):
            report = reports[0]
            if 0 != color:
                report[0xc0000] = [0x82, 0x5a, 0xc3, 7, 0,0,0,0]
            else:
                report[0xc0000] = [0x84, 0x5a, 0xc3, 7, 0,0,0,0]
            report.send()
        device.close()

