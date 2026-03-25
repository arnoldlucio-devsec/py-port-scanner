
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

