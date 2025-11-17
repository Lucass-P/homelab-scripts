#!/bin/bash
# Script de vérification de l'état des services
# Vérifie si les services critiques sont actifs

echo "=== SERVICE STATUS CHECK - $(date) ==="
echo

# Liste des services à vérifier
services=("apache2" "ssh" "cron")

# Boucle de vérification
for service in "${services[@]}"; do
    if systemctl is-active --quiet $service; then
        echo "✅ $service is running"
    else
        echo "❌ $service is NOT running"
    fi
done

echo
echo "=== Check completed ==="
