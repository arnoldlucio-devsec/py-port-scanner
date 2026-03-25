#¿Qué estás aprendiendo aquí?
#import: Estás trayendo "librerías" (herramientas externas). En ciberseguridad usarás mucho scapy (para redes) o requests (para web).
#Variables con f-strings: La forma más rápida de imprimir datos dinámicos.
import os
import platform

print("--- REPORTE DE SISTEMA OPERADOR ---")
print(f"Sistema: {platform.system()}")
print(f"Versión: {platform.version()}")
print(f"Usuario Actual: {os.getlogin()}")
print(f"Directorio de Trabajo: {os.getcwd()}")
print("-----------------------------------")