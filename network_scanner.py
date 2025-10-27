#!/usr/bin/env python3
"""
Scanner réseau basique
Vérifie quels ports sont ouverts sur localhost
"""

import socket

def scan_port(ip, port):
    """Teste si un port est ouvert"""
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        result = sock.connect_ex((str(ip), port))
        sock.close()
        return result == 0
    except:
        return False

def scan_common_ports():
    """Scanner les ports courants sur localhost"""
    print("=== NETWORK PORT SCANNER ===")
    print("Scanning localhost (127.0.0.1)...\n")

    # Ports courants à vérifier
    common_ports = {
        22: "SSH",
        80: "HTTP",
        443: "HTTPS",
        3306: "MySQL",
        3389: "RDP",
        5432: "PostgreSQL"
    }

    for port, service in common_ports.items():
        if scan_port('127.0.0.1', port):
            print(f"✅ Port {port} ({service}) is OPEN")
        else:
            print(f"❌ Port {port} ({service}) is CLOSED")

if __name__ == "__main__":
    scan_common_ports()
