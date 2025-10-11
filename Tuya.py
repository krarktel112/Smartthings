# Example Usage of TinyTuya
import tinytuya

d = tinytuya.Device('DEVICE_ID_HERE', 'IP_ADDRESS_HERE', 'LOCAL_KEY_HERE', version=3.3)
data = d.status() 
print('Device status: %r' % data)
