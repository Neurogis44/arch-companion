import shutil
import subprocess
from services.system import get_gpu_vendor, is_multilib_enabled, is_package_installed


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


def show_gaming_module():
    """Affiche le module Gaming avec sélection sur-mesure."""
    print("\n" + "=" * 60)
    print("        🎮 PARCOURS GAMING & PREPARATION")
    print("=" * 60)
    print("Analyse de ton matériel et de ton système...\n")

    if is_multilib_enabled():
        print(" [✓] Dépôt [multilib] : Activé dans /etc/pacman.conf")
    else:
        print(" [❌] Dépôt [multilib] : DÉSACTIVÉ ! (Nécessaire pour Steam/32-bit)")
        print("      👉 Édite /etc/pacman.conf pour décommenter [multilib].\n")

    vendor = get_gpu_vendor()

    # Dictionnaire des paquets adaptés au GPU
    official_packages = {
        "steam": "Plateforme de jeux Steam",
        "gamemode": "Optimiseur de performances CPU/GPU en jeu",
        "lib32-gamemode": "Support 32-bit pour GameMode",
        "vulkan-icd-loader": "Chargeur Vulkan 64-bit",
        "lib32-vulkan-icd-loader": "Chargeur Vulkan 32-bit",
        "lutris": "Lanceur open-source pour jeux (Epic, GOG, Origin...)",
    }

    if vendor == "NVIDIA":
        print(" 🟢 Carte graphique : NVIDIA détectée !")
        official_packages["nvidia-utils"] = "Pilotes & Utilitaire Vulkan NVIDIA (64-bit)"
        official_packages["lib32-nvidia-utils"] = "Support 32-bit Vulkan NVIDIA (Steam)"
    elif vendor == "AMD":
        print(" 🔴 Carte graphique : AMD détectée !")
        official_packages["vulkan-radeon"] = "Pilote Vulkan RADV pour AMD (64-bit)"
        official_packages["lib32-vulkan-radeon"] = "Pilote Vulkan RADV pour AMD (32-bit)"
    elif vendor == "INTEL":
        print(" 🔵 Carte graphique : Intel détectée !")
        official_packages["vulkan-intel"] = "Pilote Vulkan Intel (64-bit)"
        official_packages["lib32-vulkan-intel"] = "Pilote Vulkan Intel (32-bit)"

    aur_packages = {
        "heroic-games-launcher-bin": "Lanceur natif pour Epic Games et GOG",
    }

    print("\n📦 ÉTAT DES PAQUETS SUR TA MACHINE :")
    print("--- Dépôts Officiels (pacman) ---")
    for pkg, desc in official_packages.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<25} : {desc}")

    print("\n--- Dépôt Communautaire (AUR) ---")
    for pkg, desc in aur_packages.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<25} : {desc}")

    print("\n------------------------------------------------------------")
    print("1. 🚀 Tout installer/compléter (Paquets officiels recommandés)")
    print("2. 🎯 Sélectionner les paquets un par un (Officiels)")
    print("3. 🦸 Installer Heroic Games Launcher depuis l'AUR")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        missing = [pkg for pkg in official_packages if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print("\n🎉 Tous les paquets Gaming officiels sont déjà installés !")

    elif choice == "2":
        selected = []
        print("\n--- SÉLECTION PERSONNALISÉE GAMING ---")
        for pkg, desc in official_packages.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        if is_package_installed("heroic-games-launcher-bin"):
            print("\n🎉 Heroic Games Launcher est déjà installé sur ta machine !")
        else:
            install_packages(["heroic-games-launcher-bin"], use_aur=True)

    input("\nAppuie sur Entrée pour continuer...")