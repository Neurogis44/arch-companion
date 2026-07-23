import subprocess

# Paquets essentiels pour le jeu sur Arch Linux
GAMING_PACKAGES = [
    "steam",
    "gamemode",
    "lib32-gamemode",
    "vulkan-icd-loader",
    "lib32-vulkan-icd-loader",
]

def show_gaming_module():
    """Affiche le module d'installation pour le Gaming."""
    print("\n" + "=" * 50)
    print("        🎮 PARCOURS GAMING & PREPARATION")
    print("=" * 50)
    print("Ce module prépare ton système Arch pour le jeu vidéo.")
    print("Il installe Steam, GameMode et les chargeurs Vulkan.\n")

    print("💡 RAPPEL IMPORTANT ARCH WIKI :")
    print("Steam est un logiciel 32-bit. Tu DOIS avoir activé le dépôt")
    print("[multilib] dans ton fichier /etc/pacman.conf pour l'installer.")
    print("📖 Arch Wiki Gaming : https://wiki.archlinux.org/title/Gaming\n")

    print("📦 Paquets concernés :")
    for pkg in GAMING_PACKAGES:
        print(f"  • {pkg}")

    print("\n💻 Commande qui sera exécutée :")
    cmd_str = f"sudo pacman -S --needed {' '.join(GAMING_PACKAGES)}"
    print(f"   {cmd_str}\n")

    choice = input("👉 Veux-tu lancer l'installation ? (o/N) : ").strip().lower()

    if choice == "o":
        print("\n🚀 Lancement de pacman...\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + GAMING_PACKAGES, check=False)
    else:
        print("\n❌ Installation annulée.")

    input("\nAppuie sur Entrée pour revenir au menu principal...")