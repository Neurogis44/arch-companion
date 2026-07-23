import subprocess

# Paquets système essentiels
SYSTEM_PACKAGES = [
    "reflector",
    "ufw",
    "micro",
    "bash-completion",
]

def show_system_utils_module():
    """Affiche le module d'installation des utilitaires système."""
    print("\n" + "=" * 50)
    print("      🛠️ PARCOURS UTILITAIRES SYSTÈME")
    print("=" * 50)
    print("Ce module installe des outils fondamentaux pour maintenir,")
    print("sécuriser et administrer ton système Arch Linux.\n")

    print("💡 RAPPELS ARCH WIKI :")
    print("  • Reflector : Permet de trouver les miroirs pacman les plus rapides.")
    print("  • UFW : Pare-feu simple à configurer (ex: sudo ufw enable).")
    print("  • Micro : Éditeur de texte très intuitif dans le terminal.")
    print("📖 Arch Wiki Maintenance : https://wiki.archlinux.org/title/System_maintenance\n")

    print("📦 Paquets concernés :")
    for pkg in SYSTEM_PACKAGES:
        print(f"  • {pkg}")

    print("\n💻 Commande qui sera exécutée :")
    cmd_str = f"sudo pacman -S --needed {' '.join(SYSTEM_PACKAGES)}"
    print(f"   {cmd_str}\n")

    choice = input("👉 Veux-tu lancer l'installation ? (o/N) : ").strip().lower()

    if choice == "o":
        print("\n🚀 Lancement de pacman...\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + SYSTEM_PACKAGES, check=False)
    else:
        print("\n❌ Installation annulée.")

    input("\nAppuie sur Entrée pour revenir au menu principal...")