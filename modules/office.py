import shutil
import subprocess
from services.system import is_package_installed

# Paquets officiels pacman
OFFICE_OFFICIAL = {
    "libreoffice-fresh": "Suite LibreOffice (version récente)",
    "libreoffice-fresh-fr": "Pack de langue Français pour LibreOffice",
    "okular": "Lecteur PDF et visionneur de documents",
    "p7zip": "Gestionnaire d'archives 7z",
    "unzip": "Extraction de fichiers .zip",
    "unrar": "Extraction de fichiers .rar",
    "htop": "Moniteur de ressources système",
}

# Paquets AUR
OFFICE_AUR = {
    "onlyoffice-bin": "Suite OnlyOffice (Excellente compatibilité MS Office)",
}


def install_packages(packages: list, use_aur: bool = False):
    """Lance l'installation avec pacman ou yay selon la provenance."""
    if not packages:
        print("\n⚠️ Aucun paquet sélectionné.")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 Lancement de yay pour l'AUR : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print("\n❌ 'yay' n'est pas installé sur ton système !")
            print("👉 Utilise le module 1 (Assistants AUR) pour l'installer d'abord.")
    else:
        print(f"\n🚀 Lancement de pacman : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def select_custom_packages(all_packages: dict) -> list:
    """Permet à l'utilisateur de cocher/décocher les paquets individuellement."""
    selected = []
    print("\n--- SÉLECTION PERSONNALISÉE ---")
    for pkg, desc in all_packages.items():
        status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
        choice = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
        if choice == "o":
            selected.append(pkg)
    return selected


def show_office_module():
    """Affiche le module Bureautique avec choix de la suite et sélection individuelle."""
    print("\n" + "=" * 60)
    print("      📝 PARCOURS BUREAUTIQUE & OUTILS")
    print("=" * 60)
    print("Analyse des paquets bureautiques...\n")

    print("📦 ÉTAT DES PAQUETS SUR TA MACHINE :")
    print("--- Dépôts Officiels (pacman) ---")
    for pkg, desc in OFFICE_OFFICIAL.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<22} : {desc}")

    print("\n--- Dépôt Communautaire (AUR) ---")
    for pkg, desc in OFFICE_AUR.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<22} : {desc}")

    print("\n------------------------------------------------------------")
    print("1. 🚀 Tout installer/compléter (Paquets officiels pacman)")
    print("2. 🎯 Sélectionner les paquets un par un (Officiels)")
    print("3. 📑 Installer OnlyOffice depuis l'AUR (onlyoffice-bin)")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        missing = [pkg for pkg in OFFICE_OFFICIAL if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print("\n🎉 Tous les paquets officiels sont déjà installés !")

    elif choice == "2":
        selected = select_custom_packages(OFFICE_OFFICIAL)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        if is_package_installed("onlyoffice-bin"):
            print("\n🎉 OnlyOffice est déjà installé sur ta machine !")
        else:
            install_packages(["onlyoffice-bin"], use_aur=True)

    input("\nAppuie sur Entrée pour continuer...")