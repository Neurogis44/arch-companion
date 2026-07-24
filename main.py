import os
import sys

from services.i18n import t, toggle_language
from services.system import (
    get_cpu_info,
    get_desktop_environment,
    get_gpu_info,
    get_installed_packages_count,
    get_kernel_version,
    get_ram_info,
)
from modules.aur import show_aur_module
from modules.backup import show_backup_module
from modules.dev import show_dev_module
from modules.gaming import show_gaming_module
from modules.maintenance import show_maintenance_module
from modules.multimedia import show_multimedia_module
from modules.office import show_office_module
from modules.system_utils import show_system_utils_module
from modules.terminal import show_terminal_module
from modules.web import show_web_module
from modules.desktop_fix import show_desktop_fix_module


def show_dashboard():
    """Affiche la bannière bilingue et la configuration système."""
    print("=" * 60)
    print(f"                    {t('title')}")
    print(f"             {t('subtitle')}")
    print("=" * 60)
    print(f" 👤 {t('user'):<13} :", os.environ.get("USER", "Inconnu"))
    print(f" 🐧 {t('kernel'):<13} :", get_kernel_version())
    print(f" 🎨 {t('desktop'):<13} :", get_desktop_environment())
    print(f" 🧠 {t('cpu'):<13} :", get_cpu_info())
    print(f" 🎮 {t('gpu'):<13} :", get_gpu_info())
    print(f" 💾 {t('ram'):<13} :", get_ram_info())
    print(f" 📦 {t('packages'):<13} :", get_installed_packages_count())
    print("=" * 60)
    print()


def main():
    while True:
        os.system("clear" if os.name == "posix" else "cls")

        show_dashboard()

        print("🌍 [ L ] Switch Language / Changer de langue (English / Français)")
        print("-" * 60)
        print(t("menu_header"))
        print(t("m_backup"))
        print(t("m_sys"))
        print(t("m_aur"))
        print(t("m_term"))
        print(t("m_web"))
        print(t("m_office"))
        print(t("m_multi"))
        print(t("m_gaming"))
        print(t("m_dev"))
        print(t("m_maint"))
        print(t("m_de_fix"))
        print("------------------------------------------------------------")
        print("Q. 🚪 Quit / Quitter")
        print()

        choice = input(t("choice")).strip().lower()

        if choice == "l":
            toggle_language()
        elif choice == "1":
            show_backup_module()
        elif choice == "2":
            show_system_utils_module()
        elif choice == "3":
            show_aur_module()
        elif choice == "4":
            show_terminal_module()
        elif choice == "5":
            show_web_module()
        elif choice == "6":
            show_office_module()
        elif choice == "7":
            show_multimedia_module()
        elif choice == "8":
            show_gaming_module()
        elif choice == "9":
            show_dev_module()
        elif choice == "10":
            show_maintenance_module()
        elif choice == "11":
            show_desktop_fix_module()
        elif choice == "q":
            print("\nBye / À bientôt sur Arch Linux !")
            sys.exit(0)


if __name__ == "__main__":
    main()