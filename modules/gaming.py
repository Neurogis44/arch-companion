import subprocess
from services.system import get_gpu_vendor, is_package_installed


def show_gaming_module():
    """Affiche le module Gaming avec détection automatique du GPU (NVIDIA/AMD/Intel)."""
    print("\n" + "=" * 50)
    print("        🎮 PARCOURS GAMING & PREPARATION")
    print("=" * 50)
    print("Analyse de ton matériel et de tes paquets en cours...\n")

    vendor = get_gpu_vendor()

    # Paquets communs à toutes les configurations
    gaming_packages = [
        "steam",
        "gamemode",
        "lib32-gamemode",
        "vulkan-icd-loader",
        "lib32-vulkan-icd-loader",
    ]

    # Ajout des paquets spécifiques selon le constructeur du GPU
    if vendor == "NVIDIA":
        print("🟢 Carte graphique NVIDIA détectée !")
        gaming_packages.extend(["nvidia-utils", "lib32-nvidia-utils"])
    elif vendor == "AMD":
        print("🔴 Carte graphique AMD détectée !")
        gaming_packages.extend(["vulkan-radeon", "lib32-vulkan-radeon"])
    elif vendor == "INTEL":
        print("🔵 Carte graphique Intel détectée !")
        gaming_packages.extend(["vulkan-intel", "lib32-vulkan-intel"])
    else:
        print("⚠️ Marque de carte graphique non reconnue automatiquement.")

    print("\n💡 RAPPEL IMPORTANT ARCH WIKI :")
    print("Steam est un logiciel 32-bit. Tu DOIS avoir activé le dépôt")
    print("[multilib] dans ton fichier /etc/pacman.conf pour l'installer.")
    print("📖 Arch Wiki Gaming : https://wiki.archlinux.org/title/Gaming\n")

    missing_packages = []
    print("📦 État des paquets adaptés à ton matériel :")
    for pkg in gaming_packages:
        if is_package_installed(pkg):
            print(f"  [✓] {pkg} (Déjà installé)")
        else:
            print(f"  [ ] {pkg} (Manquant)")
            missing_packages.append(pkg)

    if not missing_packages:
        print(f"\n🎉 Tous les paquets optimisés pour ton GPU ({vendor}) et Steam sont déjà installés !")
        input("\nAppuie sur Entrée pour revenir au menu principal...")
        return

    print(f"\n💻 Commande qui sera exécutée ({len(missing_packages)} paquet(s) à installer) :")
    cmd_str = f"sudo pacman -S --needed {' '.join(missing_packages)}"
    print(f"   {cmd_str}\n")

    choice = input("👉 Veux-tu installer les paquets manquants ? (o/N) : ").strip().lower()

    if choice == "o":
        print("\n🚀 Lancement de pacman...\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + missing_packages, check=False)
    else:
        print("\n❌ Installation annulée.")

    input("\nAppuie sur Entrée pour revenir au menu principal...")