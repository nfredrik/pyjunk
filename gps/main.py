import DataObject
import GpsReader


io = EmulateSerialPort('./gpsdata.txt')

gps = GpsReader(io,  signalFix)


