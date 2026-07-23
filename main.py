import os
import sys

from services.system import (
    get_desktop_environment,
    get_installed_packages_count,
    get_kernel_version,
)
from modules.multimedia import show_multimedia_module
from modules.gaming import show_gaming_module
from modules.office import show_office_module
from modules.system_utils import show_system_utils_module  # <-- NOUVELLE LIGNE


def show_dashboard():
    """Affiche la bannière et la configuration système."""
    print("=" * 50)
    print("                 ARCH COMPANION")
    print("          Learn Arch. Don't fight it.")
    print("=" * 50)
    print(f" 👤 Utilisateur : {os.environ.get('USER', 'Inconnu')}")
    print(f" 🐧 Noyau Linux : {get_kernel_version()}")
    print(f" 🎨 Bureau      : {get_desktop_environment()}")
    print(f" 📦 Système     : {get_installed_packages_count()}")
    print("=" * 50)
    print()


def main():
    while True:
        os.system("clear" if os.name == "posix" else "cls")

        show_dashboard()

        print("--- PARCOURS POST-INSTALLATION ---")
        print("1. 🎵 Codecs & Multimédia (Audio, Vidéo, Polices)")
        print("2. 🎮 Pack Gaming (Steam, Vulkan, Drivers)")
        print("3. 📝 Bureautique & Outils (LibreOffice, PDF, Archives)")
        print("4. 🛠️ Utilitaires Système (Microcode, Reflector, Pare-feu)")
        print("0. 🚪 Quitter")
        print()

        choice = input("👉 Ton choix : ").strip()

        if choice == "1":
            show_multimedia_module()
        elif choice == "2":
            show_gaming_module()
        elif choice == "3":
            show_office_module()
        elif choice == "4":
            show_system_utils_module()  # <-- MODIFIÉ ICI
        elif choice == "0":
            print("\nÀ bientôt sur Arch Linux !")
            sys.exit(0)


if __name__ == "__main__":
    main()