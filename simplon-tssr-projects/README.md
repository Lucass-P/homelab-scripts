# 🎓 Projets Techniques TSSR - Simplon.co

**Formation :** Technicien Supérieur Systèmes et Réseaux (TSSR)  
**Organisme :** Simplon.co Lyon  
**Période :** Octobre - Novembre 2025  
**Réalisé par :** Lucas PEREIRA

---

## 📋 Vue d'ensemble

Ce dépôt contient l'ensemble des projets techniques réalisés dans le cadre de ma préparation à la formation TSSR en alternance. Ces projets démontrent mes compétences en administration systèmes, réseaux et cybersécurité.

**4 projets complets** couvrant :
- 🌐 Conception et simulation réseau (Cisco Packet Tracer)
- 🔒 Analyse de menaces cyber
- 🖥️ Administration Windows Server (DHCP, Active Directory)
- 🐧 Déploiement de services sur Linux (GLPI)

---

## 🗂️ Structure du projet

Chaque projet comprend :
- 📄 **Documentation PDF** : Procédure technique complète et reproductible
- 🔧 **Fichier Packet Tracer (.pkt)** : Configuration réseau testée et validée (Parties 1 et 2)

```
simplon-tssr-projects/
├── README.md (ce fichier)
│
├── Partie1_Topologie_Menaces_Cyber.pdf
├── Partie1_Topologie_Reseaux.pkt
│
├── Partie2_DHCP_Multi_Sites.pdf
├── Partie2_DHCP_Multi_Sites.pkt
│
├── Partie3_Active_Directory_Rue25.pdf
└── Partie4_GLPI_Gestion_Parc.pdf
```

---

## 🚀 Projets réalisés

### 📡 Partie 1 : Topologie réseau et analyse des menaces cyber

**Technologies :** Cisco Packet Tracer, Réseaux TCP/IP, Cybersécurité

**Objectifs :**
- Concevoir une topologie réseau inter-sites (2 LAN interconnectés via routeur)
- Configurer les équipements réseau (routeur ISR4331, switches, PCs)
- Identifier et analyser 3 menaces courantes en cybersécurité

**Menaces identifiées :**
1. **Man-in-the-Middle (MITM)** - Interception du trafic inter-sites
2. **Accès non autorisé aux équipements** - Exploitation de configurations faibles
3. **Propagation de malware** - Ransomware et infection réseau

**Compétences développées :**
- Conception d'architectures réseau
- Configuration Cisco IOS
- Analyse de risques cyber
- Documentation technique

📥 **Fichiers :**
- [📄 Documentation PDF](Partie1_Topologie_Menaces_Cyber.pdf)
- [🔧 Fichier Packet Tracer](Partie1_Topologie_Reseaux.pkt)

---

### 🔄 Partie 2 : DHCP Multi-sites avec IP Helper

**Technologies :** Cisco Packet Tracer, DHCP, Routage, IP Helper

**Objectifs :**
- Mettre en place un serveur DHCP centralisé pour 2 sites distants
- Configurer la fonction IP Helper sur le routeur
- Automatiser la distribution d'adresses IP sur les deux réseaux

**Architecture :**
- **Site A (192.168.1.0/24)** : Serveur DHCP centralisé
- **Site B (192.168.2.0/24)** : Client DHCP via IP Helper
- **Routeur ISR4331** : Relais DHCP (broadcast → unicast)

**Compétences développées :**
- Configuration serveur DHCP multi-scopes
- Mise en œuvre IP Helper sur routeur Cisco
- Gestion centralisée des adresses IP
- Tests et validation réseau (ping, ipconfig)

📥 **Fichiers :**
- [📄 Documentation PDF](Partie2_DHCP_Multi_Sites.pdf)
- [🔧 Fichier Packet Tracer](Partie2_DHCP_Multi_Sites.pkt)

---

### 🏢 Partie 3 : Active Directory - Agence Rue25

**Technologies :** Windows Server 2019, Active Directory, DHCP, VirtualBox

**Contexte :**
Installation du parc informatique de l'agence immobilière Rue25 (9 collaborateurs, 4 services).

**Objectifs :**
- Installer et configurer Windows Server 2019
- Déployer Active Directory Domain Services (domaine `rue25.com`)
- Créer une structure organisationnelle (OUs, groupes, utilisateurs)
- Configurer un serveur DHCP pour attribution automatique des IP

**Réalisations :**
- Domaine Active Directory : `rue25.com`
- 4 Unités Organisationnelles (Direction, Consultants, Commerciaux, Comptables)
- 9 comptes utilisateurs avec groupes de sécurité
- Serveur DHCP avec étendue configurée

**Compétences développées :**
- Administration Windows Server
- Gestion Active Directory (utilisateurs, groupes, OUs, GPO)
- Configuration DHCP
- Virtualisation (VirtualBox)

📥 **Fichiers :**
- [📄 Documentation PDF](Partie3_Active_Directory_Rue25.pdf)

---

### 🛠️ Partie 4 : Installation GLPI sur Debian

**Technologies :** Debian 11, GLPI, Apache2, MariaDB, PHP, VirtualBox

**Objectifs :**
- Installer une machine virtuelle Debian 11 (sans interface graphique)
- Déployer la stack LAMP (Linux, Apache, MySQL/MariaDB, PHP)
- Installer et configurer GLPI (Gestionnaire Libre de Parc Informatique)
- Mettre en place un système de ticketing et gestion de parc

**Réalisations :**
- VM Debian 11 avec SSH configuré
- Stack LAMP complète (Apache2, PHP 7.4, MariaDB)
- GLPI 10.0.10 installé et opérationnel
- Accès web configuré avec redirection de ports (mode NAT)

**Compétences développées :**
- Administration Linux (Debian)
- Configuration serveur web (Apache2)
- Gestion bases de données (MariaDB)
- Installation et configuration GLPI
- Troubleshooting (résolution erreur HTTP 501, problèmes de ports)

📥 **Fichiers :**
- [📄 Documentation PDF](Partie4_GLPI_Gestion_Parc.pdf)

---

## 💻 Comment utiliser les fichiers Packet Tracer

### Prérequis

- **Cisco Packet Tracer** (gratuit) : [Télécharger ici](https://www.netacad.com/courses/packet-tracer)
- Version recommandée : Packet Tracer 8.2 ou supérieur

### Instructions

1. **Télécharger le fichier .pkt** souhaité
2. **Ouvrir Packet Tracer**
3. **File → Open** → Sélectionner le fichier `.pkt`
4. **Explorer la topologie** :
   - Tous les équipements sont préconfigurés
   - Les configurations sont visibles en CLI (Command Line Interface)
   - Les réseaux sont opérationnels et testés

### Tests disponibles

**Dans Packet Tracer, vous pouvez :**
- 🖥️ Cliquer sur les PCs → Desktop → Command Prompt → `ipconfig`, `ping`
- 🔧 Cliquer sur le routeur → CLI → `show running-config`, `show ip interface brief`
- 📊 Utiliser le mode Simulation pour voir les paquets DHCP, ping, etc.

---

## 🎯 Compétences techniques démontrées

### Réseaux
- ✅ Conception topologies réseau (LAN, interconnexion de sites)
- ✅ Configuration routeurs Cisco (ISR4331)
- ✅ Protocoles : TCP/IP, DHCP, DNS
- ✅ IP Helper / DHCP Relay
- ✅ Diagnostic réseau (ping, traceroute, ipconfig)

### Systèmes
- ✅ Windows Server 2019 (DHCP, Active Directory)
- ✅ Linux Debian 11 (Apache, MariaDB, PHP)
- ✅ Virtualisation (VirtualBox)
- ✅ Administration multi-OS (Windows/Linux)

### Sécurité
- ✅ Analyse de menaces (MITM, accès non autorisé, malware)
- ✅ Bonnes pratiques cybersécurité
- ✅ Sécurisation services (SSH, MariaDB)

### Méthodologie
- ✅ Documentation technique professionnelle
- ✅ Tests et validation systématiques
- ✅ Troubleshooting et résolution de problèmes
- ✅ Reproductibilité des configurations

---

## 📚 Contexte de formation

### Programme TSSR - Simplon.co

**Titre visé :** Technicien Supérieur Systèmes et Réseaux (RNCP 37682)  
**Durée :** 18 mois en alternance (Mars 2026 - Octobre 2027)  
**Rythme :** 3 semaines entreprise / 1 semaine formation  

**Objectif professionnel :** Administrateur Systèmes et Réseaux puis évolution vers Analyste Cybersécurité

---

## 👤 À propos

**Lucas PEREIRA** - 25 ans - Lyon, France

En reconversion professionnelle de l'animation 3D technique vers l'IT et la cybersécurité, je combine :
- 🎓 Solides bases techniques (Python, troubleshooting multi-OS)
- 🌍 Bilinguisme français/anglais
- 🏠 Homelab personnel (Active Directory 1040 users, scripts d'automatisation)
- 💪 Motivation et capacité d'apprentissage rapide

### 🔗 Liens

- 🌐 **Portfolio complet** : [linktr.ee/Lucas_Pereira33](https://linktr.ee/Lucas_Pereira33)
- 💼 **LinkedIn** : [lucas-pereira-lyon](https://www.linkedin.com/in/lucas-pereira-807bb9124)
- 📧 **Email** : pereira.lucas01@gmail.com
- 💻 **GitHub** : [Lucass-P](https://github.com/Lucass-P)

---

## 📄 Licence et utilisation

Ces projets sont réalisés dans un cadre pédagogique et de formation professionnelle.

**Utilisation autorisée pour :**
- ✅ Consultation et apprentissage
- ✅ Évaluation par recruteurs et formateurs
- ✅ Inspiration pour vos propres projets (avec citation de la source)

**Utilisation interdite pour :**
- ❌ Reproduction intégrale sans attribution
- ❌ Revente ou utilisation commerciale

---

## 🙏 Remerciements

- **Simplon.co Lyon** : Christine, Jérôme, Leslie - Pour l'accompagnement et la formation
- **Communauté Cisco** : Pour les ressources Packet Tracer
- **Documentation officielle** : Cisco, Microsoft, Debian, GLPI

---

<div align="center">

**⭐ Si ce portfolio vous intéresse pour une alternance TSSR, n'hésitez pas à me contacter ! ⭐**

[📧 pereira.lucas01@gmail.com](mailto:pereira.lucas01@gmail.com) | [💼 LinkedIn](https://www.linkedin.com/in/lucas-pereira-807bb9124) | [🌐 Portfolio](https://linktr.ee/Lucas_Pereira33)

---

*Dernière mise à jour : Novembre 2025*

</div>
