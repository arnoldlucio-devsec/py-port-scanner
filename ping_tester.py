#Este script va a verificar si una dirección IP responde 
#(si está "viva").

import subprocess

# Dirección a probar (ejmp. 8.8.8.8)
target = "8.8.8.8" 

print(f"[*] Iniciando reconocimiento de red en: {target}...")

# Ejecutamos un comando de sistema desde Python
response = subprocess.run(['ping', '-c', '1', target], capture_output=True)
#ping: Es el comando de red.
#c 1: (Count 1) Le ordenaste enviar solo un paquete.

if response.returncode == 0:
    #returncode == 0: Esta es la clave de Linux.
    #"Si es 0, está vivo".-----------
    print(f"[+] DISPOSITIVO ONLINE: {target} respondió con éxito.")
else:
    print(f"[-] DISPOSITIVO OFFLINE: {target} no responde.")
