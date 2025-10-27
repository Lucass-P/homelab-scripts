#!/usr/bin/env python3
"""
Script de création d'utilisateurs en batch
Génère des commandes pour créer plusieurs utilisateurs Windows/Linux
"""

# Liste d'utilisateurs à créer
users = [
    {"username": "jdupont", "fullname": "Jean Dupont"},
    {"username": "mmartin", "fullname": "Marie Martin"},
    {"username": "pdurand", "fullname": "Pierre Durand"},
    {"username": "sbernard", "fullname": "Sophie Bernard"},
    {"username": "lrobert", "fullname": "Luc Robert"}
]

def generate_windows_commands():
    """Génère commandes PowerShell pour Windows"""
    print("=== COMMANDES WINDOWS (PowerShell) ===\n")
    for user in users:
        print(f"New-LocalUser -Name '{user['username']}' -FullName '{user['fullname']}' -Password (ConvertTo-SecureString 'Password123!' -AsPlainText -Force)")
    print()

def generate_linux_commands():
    """Génère commandes pour Linux"""
    print("=== COMMANDES LINUX (Bash) ===\n")
    for user in users:
        print(f"sudo useradd -m -c '{user['fullname']}' {user['username']}")
        print(f"echo '{user['username']}:Password123!' | sudo chpasswd")
    print()

if __name__ == "__main__":
    print("Script de création d'utilisateurs en batch\n")
    generate_windows_commands()
    generate_linux_commands()
