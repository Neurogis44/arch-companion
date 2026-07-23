import shutil
import subprocess
from services.system import get_cpu_vendor, is_package_installed


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
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


def show_system_utils_module():
    """Affiche le module Utilitaires Système avec sélection sur-mesure."""
    print("\n" + "=" * 60)
    print("      🛠️ PARCOURS UTILITAIRES SYSTÈME")
    print("=" * 60)
    print("Analyse de ton matériel et de tes utilitaires...\n")

    cpu_vendor = get_cpu_vendor()

    official_packages = {
        "reflector": "Mise à jour automatique des miroirs pacman rapides",
        "ufw": "Pare-feu simple (Uncomplicated Firewall)",
        "micro": "Éditeur de texte moderne et intuitif pour le terminal",
        "bash-completion": "Auto-complétion intelligente pour le terminal Bash",
        "btop": "Moniteur de ressources système ultra élégant",
        "fastfetch": "Affichage esthétique des infos système",
    }

    if cpu_vendor == "AMD":
        print(" 🔴 Processeur AMD détecté -> Microcode : amd-ucode")
        official_packages["amd-ucode"] = "Mises à jour de sécurité majeures du CPU AMD"
    elif cpu_vendor == "INTEL":
        print(" 🔵 Processeur Intel détecté -> Microcode : intel-ucode")
        official_packages["intel-ucode"] = "Mises à jour de sécurité majeures du CPU Intel"

    print("\n📦 ÉTAT DES PAQUETS SUR TA MACHINE :")
    print("--- Dépôts Officiels (pacman) ---")
    for pkg, desc in official_packages.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<22} : {desc}")

    print("\n------------------------------------------------------------")
    print("1. 🚀 Tout installer/compléter (Utilitaires officiels)")
    print("2. 🎯 Sélectionner les paquets un par un (Officiels)")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        missing = [pkg for pkg in official_packages if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print("\n🎉 Tous les utilitaires système officiels sont déjà installés !")

    elif choice == "2":
        selected = []
        print("\n--- SÉLECTION PERSONNALISÉE UTILITAIRES ---")
        for pkg, desc in official_packages.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)

    input("\nAppuie sur Entrée pour continuer...")