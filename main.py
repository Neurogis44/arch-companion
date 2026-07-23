import os
import sys

from services.system import (
    get_cpu_info,
    get_desktop_environment,
    get_gpu_info,
    get_installed_packages_count,
    get_kernel_version,
    get_ram_info,
)
from modules.multimedia import show_multimedia_module
from modules.gaming import show_gaming_module
from modules.office import show_office_module
from modules.system_utils import show_system_utils_module


def show_dashboard():
    """Affiche la bannière et la configuration système détaillée."""
    print("=" * 60)
    print("                    ARCH COMPANION")
    print("             Learn Arch. Don't fight it.")
    print("=" * 60)
    print(" 👤 Utilisateur :", os.environ.get("USER", "Inconnu"))
    print(" 🐧 Noyau Linux :", get_kernel_version())
    print(" 🎨 Bureau      :", get_desktop_environment())
    print(" 🧠 Processeur  :", get_cpu_info())
    print(" 🎮 Carte Vidéo :", get_gpu_info())
    print(" 💾 Mémoire RAM :", get_ram_info())
    print(" 📦 Paquets     :", get_installed_packages_count())
    print("=" * 60)
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
            show_system_utils_module()
        elif choice == "0":
            print("\nÀ bientôt sur Arch Linux !")
            sys.exit(0)


if __name__ == "__main__":
    main()