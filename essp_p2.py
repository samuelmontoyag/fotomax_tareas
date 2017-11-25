import time
from essp_api import EsspApi
print("prueba essp2")
essp = EsspApi('/dev/ttyUSB0')
print("prueba habilita")
essp.enable()

while True:
    print("Escucha")
    for p in essp.poll():
        if p['status'] == essp.CREDIT_NOTE:
            print 'A note (code=%s) has passed through the device' % p['param']
    time.sleep(0.5)
