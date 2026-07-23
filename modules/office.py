import subprocess

# Paquets pour la bureautique et la gestion de fichiers/archives
OFFICE_PACKAGES = [
    "libreoffice-fresh",
    "libreoffice-fresh-fr",
    "p7zip",
    "unzip",
    "unrar",
    "okular",
    "htop",
]

def show_office_module():
    """Affiche le module d'installation Bureautique & Outils."""
    print("\n" + "=" * 50)
    print("      📝 PARCOURS BUREAUTIQUE & OUTILS")
    print("=" * 50)
    print("Ce module installe la suite bureautique LibreOffice (en français),")
    print("les outils de compression/décompression et un lecteur PDF.\n")

    print("💡 RAPPEL ARCH WIKI :")
    print("Arch propose deux versions de LibreOffice :")
    print("  • libreoffice-fresh : version la plus récente avec les nouvelles options.")
    print("  • libreoffice-still : version éprouvée ultra stable pour entreprise.")
    print("📖 Arch Wiki LibreOffice : https://wiki.archlinux.org/title/LibreOffice\n")

    print("📦 Paquets concernés :")
    for pkg in OFFICE_PACKAGES:
        print(f"  • {pkg}")

    print("\n💻 Commande qui sera exécutée :")
    cmd_str = f"sudo pacman -S --needed {' '.join(OFFICE_PACKAGES)}"
    print(f"   {cmd_str}\n")

    choice = input("👉 Veux-tu lancer l'installation ? (o/N) : ").strip().lower()

    if choice == "o":
        print("\n🚀 Lancement de pacman...\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + OFFICE_PACKAGES, check=False)
    else:
        print("\n❌ Installation annulée.")

    input("\nAppuie sur Entrée pour revenir au menu principal...")