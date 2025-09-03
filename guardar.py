import os
import shutil
import re
import time

# Ruta de descargas
descargas = os.path.expanduser("C:\\Users\\frank\\Downloads")

# Ruta base de OneDrive
onedrive_base = os.path.expanduser("C:\\Users\\frank\\OneDrive\\IACC_CONTENIDOS")

# Detectar semana y ramo desde nombre
def extraer_info(nombre):
    semana_match = re.search(r"S(\d{1,2})_", nombre)
                            # aca pones el identificador del ramo que se desea organizar 
    ramo_match = re.search(r"(MATLOG1301|ETGDT1303|PROGR1303|BASBD1305|HERQA1301|FUNRS1305|PROHT2305|PROHT1305|PROOO1301|PRGAV1301)", nombre)
    if semana_match and ramo_match:
        semana = f"Semana_{semana_match.group(1).zfill(2)}"
        ramo = ramo_match.group(1)
        return semana, ramo
    return None, None

# Mover archivos 
for archivo in os.listdir(descargas):
    ruta_archivo = os.path.join(descargas, archivo)
    if os.path.isfile(ruta_archivo):
        semana, ramo = extraer_info(archivo)
        if semana and ramo:
            destino = os.path.join(onedrive_base, ramo, semana)
            os.makedirs(destino, exist_ok=True)
            shutil.move(ruta_archivo, os.path.join(destino, archivo))
            print(f"✅ {archivo} → {destino}")
        else:
            print(f"⚠️ No se pudo clasificar: {archivo}")

while True:
    for archivo in os.listdir(descargas):
        ruta_archivo = os.path.join(descargas, archivo)
        if os.path.isfile(ruta_archivo):
            semana, ramo = extraer_info(archivo)
            if semana and ramo:
                destino = os.path.join(onedrive_base, ramo, semana)
                os.makedirs(destino, exist_ok=True)
                shutil.move(ruta_archivo, os.path.join(destino, archivo))
                print(f"✅ {archivo} → {destino}")
            else:
                print(f"⚠️ No se pudo clasificar: {archivo}")
    time.sleep(10)  # Esperar 10 segundos antes de volver a comprobar