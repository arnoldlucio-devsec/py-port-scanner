#En ciberseguridad, lo más importante es saber qué "puertas" 
#(puertos) están abiertas en un servidor.

import socket

target = "google.com"
puertos = [80, 443, 22] # Lista de objetivos

print(f"--- ESCÁNER DE RECONOCIMIENTO V1.1 ({target}) ---")

for port in puertos:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    
    result = s.connect_ex((target, port))
    
    if result == 0:
        print(f"[+] PUERTO {port}: ABIERTO")
    else:
        print(f"[-] PUERTO {port}: CERRADO / FILTRADO")
    
    s.close()

print("--- ESCANEO FINALIZADO ---")

#Puerto 80 (Abierto): Google permite que cualquiera entre a su 
# buscador (HTTP).

#Puerto 443 (Abierto): Google protege tus datos con cifrado (HTTPS).
#Es la puerta "segura".

#Puerto 22 (Cerrado/Filtrado): Google tiene guardias en la puerta 
# trasera (SSH). Nadie entra a sus servidores a menos que sea 
# un administrador autorizado.