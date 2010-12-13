import time

from tasks import tambah

hasil = tambah.delay(2,3)
while hasil.status == 'PENDING':
    print '.. menunggu hasil'
    time.sleep(1)
print 'hasil:', hasil.result

