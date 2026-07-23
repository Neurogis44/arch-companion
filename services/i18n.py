# Configuration de la langue globale ("en" par défaut, ou "fr")
CURRENT_LANG = "en"  # Passé en anglais par défaut

MESSAGES = {
    "fr": {
        "title": "ARCH COMPANION",
        "subtitle": "Apprendre Arch. Ne pas le subir.",
        "user": "Utilisateur",
        "kernel": "Noyau Linux",
        "desktop": "Bureau",
        "cpu": "Processeur",
        "gpu": "Carte Vidéo",
        "ram": "Mémoire RAM",
        "packages": "Paquets",
        "menu_header": "--- PARCOURS OPTIMAL POST-INSTALLATION ---",
        "m_backup": "1. 🛡️ Sécurité & Snapshots (Snapper, Timeshift, Sauvegarde)",
        "m_sys": "2. 🛠️ Socle Système & Utilitaires (Microcode CPU, Reflector, Pare-feu)",
        "m_aur": "3. 📦 Assistants AUR (yay, pamac-aur)",
        "m_term": "4. 🎨 Confort Terminal (Starship, Alias, Zsh)",
        "m_web": "5. 🌐 Navigateurs Web (Firefox, Chrome, Brave, Edge...)",
        "m_office": "6. 📝 Bureautique & Outils (LibreOffice, OnlyOffice, PDF)",
        "m_multi": "7. 🎵 Codecs & Multimédia (Audio, Vidéo, Polices)",
        "m_gaming": "8. 🎮 Pack Gaming (Steam, Vulkan, Drivers)",
        "m_dev": "9. 👨‍💻 Pack Développeur (VS Code, Python, Go, Docker...)",
        "m_maint": "10. 🧹 Santé Système & Maintenance (Nettoyage cache, Services)",
        "choice": "👉 Ton choix : ",
        "installed": "Déjà installé",
        "missing": "Manquant",
        "press_enter": "Appuie sur Entrée pour continuer...",
    },
    "en": {
        "title": "ARCH COMPANION",
        "subtitle": "Learn Arch. Don't fight it.",
        "user": "User",
        "kernel": "Linux Kernel",
        "desktop": "Desktop Environment",
        "cpu": "Processor",
        "gpu": "Graphics Card",
        "ram": "RAM Memory",
        "packages": "Packages",
        "menu_header": "--- OPTIMAL POST-INSTALLATION WORKFLOW ---",
        "m_backup": "1. 🛡️ Safety & Snapshots (Snapper, Timeshift, Backup)",
        "m_sys": "2. 🛠️ System Base & Utilities (CPU Microcode, Reflector, Firewall)",
        "m_aur": "3. 📦 AUR Helpers (yay, pamac-aur)",
        "m_term": "4. 🎨 Terminal Experience (Starship, Aliases, Zsh)",
        "m_web": "5. 🌐 Web Browsers (Firefox, Chrome, Brave, Edge...)",
        "m_office": "6. 📝 Office & Tools (LibreOffice, OnlyOffice, PDF)",
        "m_multi": "7. 🎵 Codecs & Multimedia (Audio, Video, Fonts)",
        "m_gaming": "8. 🎮 Gaming Pack (Steam, Vulkan, Drivers)",
        "m_dev": "9. 👨‍💻 Developer Pack (VS Code, Python, Go, Docker...)",
        "m_maint": "10. 🧹 System Health & Maintenance (Cache, Services)",
        "choice": "👉 Your choice: ",
        "installed": "Already installed",
        "missing": "Missing",
        "press_enter": "Press Enter to continue...",
    },
}


def t(key: str) -> str:
    """Retourne le texte traduit selon la langue actuelle."""
    return MESSAGES.get(CURRENT_LANG, MESSAGES["en"]).get(key, key)


def toggle_language():
    """Bascule entre l'anglais et le français."""
    global CURRENT_LANG
    CURRENT_LANG = "fr" if CURRENT_LANG == "en" else "en"