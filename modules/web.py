import shutil
import subprocess
from services.system import is_package_installed

# Navigateurs Open Source (Dépôts officiels)
BROWSERS_OPEN_SOURCE = {
    "firefox": "Le standard libre et respectueux de la vie privée",
    "chromium": "Version 100% open-source à la base de Chrome",
    "brave-bin": "Basé sur Chromium avec protections et bloqueurs natifs",
}

# Navigateurs Propriétaires (AUR & Officiel)
BROWSERS_PROPRIETARY = {
    "google-chrome": "Le navigateur de Google (AUR)",
    "microsoft-edge-stable-bin": "Microsoft Edge pour Linux (AUR)",
    "vivaldi": "Ultra-personnalisable et riche en fonctionnalités (pacman)",
}


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print("\n⚠️ Aucun paquet sélectionné.")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 Lancement de yay : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print("\n❌ 'yay' n'est pas installé sur ton système !")
            print("👉 Utilise le module 1 (Assistants AUR) pour l'installer d'abord.")
    else:
        print(f"\n🚀 Lancement de pacman : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_web_module():
    """Affiche le module des navigateurs web."""
    print("\n" + "=" * 60)
    print("      🌐 SELECTION DES NAVIGATEURS WEB")
    print("=" * 60)
    print("Analyse des navigateurs installés sur ta machine...\n")

    print("📦 ÉTAT DES NAVIGATEURS :")
    print("--- Open Source (Libres) ---")
    for pkg, desc in BROWSERS_OPEN_SOURCE.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<26} : {desc}")

    print("\n--- Propriétaires / Code Fermé ---")
    for pkg, desc in BROWSERS_PROPRIETARY.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<26} : {desc}")

    print("\n------------------------------------------------------------")
    print("1. 🔓 Installer un navigateur Open Source (Firefox, Chromium, Brave)")
    print("2. 🔒 Installer un navigateur Propriétaire (Chrome, Edge, Vivaldi)")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        print("\n--- CHOIX OPEN SOURCE ---")
        for pkg, desc in BROWSERS_OPEN_SOURCE.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                # Brave-bin utilise l'AUR, Firefox et Chromium utilisent pacman
                use_aur = pkg.endswith("-bin")
                install_packages([pkg], use_aur=use_aur)

    elif choice == "2":
        print("\n--- CHOIX PROPRIÉTAIRE ---")
        for pkg, desc in BROWSERS_PROPRIETARY.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                # Chrome et Edge passent par l'AUR, Vivaldi par pacman
                use_aur = "chrome" in pkg or "edge" in pkg
                install_packages([pkg], use_aur=use_aur)

    input("\nAppuie sur Entrée pour continuer...")