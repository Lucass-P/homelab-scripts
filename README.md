# 🔧 Homelab Scripts - Scripts d'Automatisation IT

Scripts Python et Bash développés pour l'administration de mon homelab personnel.

## 📋 Description

Collection de scripts d'automatisation pour la gestion quotidienne d'infrastructures Windows Server et Linux (Ubuntu).

**Projet personnel** dans le cadre de ma reconversion vers les métiers du support IT et de la cybersécurité.

## 🛠️ Scripts Disponibles

### Python Scripts

#### 1️⃣ `monitor_system.py`
- **Fonction** : Monitoring des ressources système (CPU, RAM, Disque)
- **Alertes** : Seuils configurables (>80%)
- **Usage** : `python3 monitor_system.py`

#### 2️⃣ `create_users_batch.py`
- **Fonction** : Génération de commandes pour création d'utilisateurs en batch
- **Support** : Windows (PowerShell) et Linux (Bash)
- **Usage** : `python3 create_users_batch.py`

#### 3️⃣ `network_scanner.py`
- **Fonction** : Scanner de ports ouverts sur localhost
- **Ports vérifiés** : SSH, HTTP, HTTPS, MySQL, RDP, PostgreSQL
- **Usage** : `python3 network_scanner.py`

### Bash Scripts

#### 4️⃣ `backup_script.sh`
- **Fonction** : Backup automatique avec compression et logs
- **Format** : tar.gz avec horodatage
- **Usage** : `bash backup_script.sh`

#### 5️⃣ `check_services.sh`
- **Fonction** : Vérification statut des services critiques
- **Services** : Apache2, SSH, Cron
- **Usage** : `bash check_services.sh`

## 💻 Prérequis

### Python Scripts
- Python 3.6+
- Module `psutil` pour monitoring : `pip install psutil`

### Bash Scripts
- Bash 4.0+
- Droits sudo pour certaines opérations

## 🚀 Installation
```bash
# Cloner le repository
git clone https://github.com/Lucass-P/homelab-scripts.git
cd homelab-scripts

# Rendre les scripts Bash exécutables
chmod +x *.sh

# Installer dépendances Python
pip install psutil
```

## 📚 Contexte du Projet

Ces scripts ont été développés dans le cadre de mon **homelab personnel** :

- **Infrastructure** : 2 VMs (Windows Server 2019 + Ubuntu Server 22.04)
- **Environnement** : VirtualBox
- **Objectif** : Apprentissage pratique de l'administration système et de l'automatisation
- **Temps investi** : ~25 heures

### Compétences développées

- Scripting Python et Bash
- Administration Windows Server (Active Directory)
- Administration Linux (systemd, services)
- Monitoring et surveillance système
- Automatisation de tâches répétitives

## 📧 Contact

**Lucas Pereira**  
📧 Email : pereira.lucas01@gmail.com  
💼 LinkedIn : [lucas-pereira-807bb9124](https://linkedin.com/in/lucas-pereira-807bb9124)

## 📝 Licence

Projet personnel à des fins d'apprentissage - Libre d'utilisation avec attribution.

---

*Scripts créés dans le cadre de ma préparation à la formation Technicien Informatique de Proximité avec Simplon.co*
