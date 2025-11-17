#!/bin/bash
# Script de backup automatique avec logs
# Sauvegarde un dossier et enregistre l'opération

BACKUP_DIR="/home/backups"
SOURCE_DIR="/home/important_files"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_FILE="backup_$DATE.tar.gz"

# Création du dossier backup si inexistant
mkdir -p $BACKUP_DIR

# Compression et sauvegarde
echo "[$(date)] Starting backup of $SOURCE_DIR..." | tee -a $BACKUP_DIR/backup.log
tar -czf $BACKUP_DIR/$BACKUP_FILE $SOURCE_DIR 2>/dev/null

# Vérification du succès
if [ $? -eq 0 ]; then
    echo "[$(date)] ✅ Backup completed: $BACKUP_FILE" | tee -a $BACKUP_DIR/backup.log
else
    echo "[$(date)] ❌ Backup failed!" | tee -a $BACKUP_DIR/backup.log
fi
