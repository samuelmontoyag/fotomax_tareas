import os
from paramiko import SSHClient, AutoAddPolicy
from scp import SCPClient
from time import sleep
from datetime import datetime

maquinas = ['ftmx022', 'ftmx023', 'ftmx024', 'ftmx025', 'ftmx026', 'ftmx027',
            'ftmx028', 'ftmx029']
IMAGES_PER_MACHINE = 2
for maquina in maquinas:

    if not os.path.exists(maquina):
        os.makedirs(maquina)
    hostname = "%s.ddns.net" % maquina
    try:
        print("conectando a  maquina: ", maquina)
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())
        ssh.load_system_host_keys()
        ssh.connect(hostname, username='fotomax', password='fotomax1',
                    timeout=120)
        for index in range(IMAGES_PER_MACHINE):
            print("Limpiando foto %d: " % index)
            ssh.exec_command("rm -f /tmp/out.xwd")
            ssh.exec_command("rm -f /tmp/img.jpg")

            print("Tomando Foto %d: " % index)
            ssh.exec_command("xwd -out /tmp/out.xwd -root -display :0.0 ", timeout=50)
            print("transformando foto: %d: " % index)
            ssh.exec_command("convert -quality 8% /tmp/out.xwd /tmp/img.jpg", timeout=50)

            print("Copiando imagen ... ")
            fname = "img_%d_%s.jpg" % (index, str(datetime.now().strftime("%Y%m%d-%H_%M_%S")))
            filepath = "%s/%s" % (maquina, fname)
            try:
                with SCPClient(ssh.get_transport(), socket_timeout=30) as scp:
                    scp.get('/tmp/img.jpg', filepath)
            except Exception as e:
                print("error al copiar la imagen %d" % index, e)
        ssh.close()
    except Exception as e:
        print("error en la conexion", e)
