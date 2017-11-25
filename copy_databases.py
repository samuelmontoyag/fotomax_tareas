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

        filepath = "%s/app.db" % (maquina)

        with SCPClient(ssh.get_transport(), socket_timeout=30) as scp:
            scp.get('/app/cabinas/app.db', filepath)

        ssh.close()
    except Exception as e:
        print("error en la conexion", e)
