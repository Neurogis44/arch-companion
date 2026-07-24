cat << 'EOF' > README_EN.md
# 🚀 Arch Companion

🇫🇷 [Français](./README.md) | 🇬🇧 **English**

---

**Arch Companion** is an interactive and bilingual TUI (Terminal User Interface) script designed to automate and simplify the post-installation setup of Arch Linux.

> *"Learn Arch. Don't fight it."*

### ✨ Key Features

- **🌐 100% Bilingual (FR/EN):** Switch languages instantly anywhere in the app by pressing `L`.
- **🖥️ Desktop Detection & Completion (KDE, GNOME, XFCE):** Automatically installs integration packages often left out by `archinstall` (Bluetooth, emoji fonts, archive handlers, pavucontrol, etc.) and enables necessary `systemd` services (`bluetooth`, `cups`).
- **🎮 Full Gaming Pack:** Hardware-aware GPU drivers (NVIDIA, AMD, Intel), Steam, Vulkan, GameMode, Lutris, Heroic, alongside **MangoHud**, **Goverlay**, and **LACT** (with automatic `lactd` service activation).
- **📦 AUR Helpers & Software Suites:** Easy setup for `yay`, `pamac-aur`, web browsers (Open Source / Proprietary), office tools (LibreOffice, OnlyOffice), and developer setups (VS Code, Docker, Python, Go...).
- **🛡️ Safety & Maintenance:** Package list export/restore, system snapshots (Snapper/Timeshift), smart `pacman` cache cleanup (using `pacman-contrib`), and orphan package removal.

### 📋 Prerequisites

- An **Arch Linux** based system.
- **Python 3** (installed by default on Arch).
- Git.

### 🚀 Quick Start

```bash
# 1. Clone the repository
git clone https://github.com/neurogis44/arch-companion.git

# 2. Enter the directory
cd arch-companion

# 3. Run the application
python main.py
