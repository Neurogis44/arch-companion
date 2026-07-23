import subprocess
from services.system import is_package_installed

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
    """Affiche le module Bureautique avec diagnostic des paquets."""
    print("\n" + "=" * 50)
    print("      📝 PARCOURS BUREAUTIQUE & OUTILS")
    print("=" * 50)
    print("Analyse de ton système en cours...\n")

    print("💡 RAPPEL ARCH WIKI :")
    print("Arch propose deux versions de LibreOffice :")
    print("  • libreoffice-fresh : version la plus récente.")
    print("  • libreoffice-still : version ultra stable.")
    print("📖 Arch Wiki : https://wiki.archlinux.org/title/LibreOffice\n")

    missing_packages = []
    print("📦 État des paquets sur ta machine :")
    for pkg in OFFICE_PACKAGES:
        if is_package_installed(pkg):
            print(f"  [✓] {pkg} (Déjà installé)")
        else:
            print(f"  [ ] {pkg} (Manquant)")
            missing_packages.append(pkg)

    if not missing_packages:
        print("\n🎉 La suite bureautique et les outils sont tous déjà installés !")
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