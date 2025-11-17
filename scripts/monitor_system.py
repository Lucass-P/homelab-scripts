#!/usr/bin/env python3
"""
Script de monitoring système basique
Surveille CPU, RAM et espace disque
"""

import psutil
import datetime

def check_system():
    """Vérifie l'utilisation des ressources système"""

    # Récupération des métriques
    cpu = psutil.cpu_percent(interval=1)
    ram = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    # Affichage
    print(f"=== SYSTEM MONITOR - {datetime.datetime.now()} ===")
    print(f"CPU Usage: {cpu}%")
    print(f"RAM Usage: {ram}%")
    print(f"Disk Usage: {disk}%")
    print()

    # Alertes si seuils dépassés
    if cpu > 80:
        print("⚠️  ALERT: High CPU usage!")
    if ram > 80:
        print("⚠️  ALERT: High RAM usage!")
    if disk > 80:
        print("⚠️  ALERT: Low disk space!")

if __name__ == "__main__":
    check_system()
