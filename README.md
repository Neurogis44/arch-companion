# 🚀 Arch Companion

[Français](#-français) | [English](#-english)

---

## 🇫🇷 Français

**Arch Companion** est un script TUI (Interface Terminal) interactif et bilingue conçu pour automatiser et simplifier la configuration post-installation d'Arch Linux.

> *"Apprendre Arch. Ne pas le subir."*

### ✨ Fonctionnalités Principales

- **🌐 100% Bilingue (FR/EN) :** Basculez instantanément de langue à tout moment dans l'application en appuyant sur `L`.
- **🖥️ Détection & Complétion du Bureau (KDE, GNOME, XFCE) :** Installe automatiquement les paquets d'intégration souvent oubliés par `archinstall` (Bluetooth, polices émojis, gestionnaires d'archives, pavucontrol, etc.) et active les services `systemd` requis (`bluetooth`, `cups`).
- **🎮 Pack Gaming Complet :** Support GPU sur-mesure (NVIDIA, AMD, Intel), Steam, Vulkan, GameMode, Lutris, Heroic, ainsi que **MangoHud**, **Goverlay** et **LACT** (avec activation automatique du service `lactd`).
- **📦 Assistants AUR & Logiciels :** Installation simplifiée de `yay`, `pamac-aur`, navigateurs Web (Open Source / Propriétaires), suites bureautiques (LibreOffice, OnlyOffice) et outils de développement (VS Code, Docker, Python, Go...).
- **🛡️ Sécurité & Maintenance :** Export/Restauration de la liste des paquets, création de snapshots (Snapper/Timeshift), nettoyage intelligent du cache `pacman` (via `pacman-contrib`) et suppression des orphelins.

### 📋 Prérequis

- Une distribution basée sur **Arch Linux**.
- **Python 3** (installé par défaut sur Arch).
- Git.

### 🚀 Installation & Utilisation

```bash
# 1. Cloner le dépôt
git clone [https://github.com/neurogis44/arch-companion.git](https://github.com/neurogis44/arch-companion.git)

# 2. Accéder au dossier
cd arch-companion

# 3. Lancer l'application
python main.py