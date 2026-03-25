import socket
from datetime import datetime

class Scanner:
    def __init__(self, objetivo):
        self.objetivo = objetivo
        self.puertos = [21, 22, 80, 443, 3306, 8080] # Agregué FTP y bases de datos
        self.resultados = []

    def ejecutar_escaneo(self):
        print(f"\n[!] Iniciando escaneo en: {self.objetivo}")
        print(f"[!] Tiempo: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
        
        for puerto in self.puertos:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            
            result = s.connect_ex((self.objetivo, puerto))
            
            if result == 0:
                estado = "ABIERTO"
                print(f"[+] Puerto {puerto}: {estado}")
            else:
                estado = "CERRADO/FILTRADO"
                # Solo imprimimos los abiertos para no saturar la pantalla
            
            # Guardamos la info en una lista interna
            self.resultados.append(f"Puerto {puerto} | {estado}")
            s.close()
            
        self.guardar_reporte()

    def guardar_reporte(self):
        nombre_archivo = "reporte_escaneo.txt"
        with open(nombre_archivo, "a") as archivo:
            archivo.write(f"\n--- REPORTE DE ESCANEO: {self.objetivo} ---\n")
            archivo.write(f"Fecha: {datetime.now()}\n")
            for linea in self.resultados:
                archivo.write(linea + "\n")
        print(f"\n[✔] Reporte guardado en {nombre_archivo}")

# --- SECCIÓN DE EJECUCIÓN (INTERACTIVA) ---

target = input("Introduce la IP o dominio a escanear (ej: google.com): ")

# Creamos el objeto 'mi_scanner' con el input del usuario
mi_scanner = Scanner(target)

# Ejecutamos el método principal
mi_scanner.ejecutar_escaneo()