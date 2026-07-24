import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed


def get_office_dicts():
    """Retourne les dictionnaires de bureautique traduits dynamiquement."""
    official = {
        "libreoffice-fresh": t("off_desc_lo"),
        "libreoffice-fresh-fr": t("off_desc_lo_fr"),
        "okular": t("off_desc_okular"),
        "p7zip": t("off_desc_p7zip"),
        "unzip": t("off_desc_unzip"),
        "unrar": t("off_desc_unrar"),
        "htop": t("off_desc_htop"),
    }
    aur = {
        "onlyoffice-bin": t("off_desc_onlyoffice"),
    }
    return official, aur


def install_packages(packages: list, use_aur: bool = False):
    """Lance l'installation avec pacman ou yay selon la provenance."""
    if not packages:
        print(f"\n⚠️ {t('off_no_pkg_selected')}")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 {t('off_launching_yay')} : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print(f"\n❌ {t('off_yay_not_installed')}")
            print(f"👉 {t('off_yay_hint')}")
    else:
        print(f"\n🚀 {t('off_launching_pacman')} : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def select_custom_packages(all_packages: dict) -> list:
    """Permet à l'utilisateur de cocher/décocher les paquets individuellement."""
    selected = []
    print(f"\n--- {t('off_custom_selection')} ---")
    for pkg, desc in all_packages.items():
        status = t("installed") if is_package_installed(pkg) else t("missing")
        choice = input(f" ❓ {t('off_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
        if choice in ["o", "y"]:
            selected.append(pkg)
    return selected


def show_office_module():
    """Affiche le module Bureautique avec choix de la suite et sélection individuelle."""
    office_official, office_aur = get_office_dicts()

    print("\n" + "=" * 60)
    print(f"      {t('off_title')}")
    print("=" * 60)
    print(f"{t('off_analyzing')}\n")

    print(f"📦 {t('off_status_header')} :")
    print(f"--- {t('off_section_official')} ---")
    for pkg, desc in office_official.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<22} : {desc}")

    print(f"\n--- {t('off_section_aur')} ---")
    for pkg, desc in office_aur.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<22} : {desc}")

    print("\n------------------------------------------------------------")
    print(t("off_opt1"))
    print(t("off_opt2"))
    print(t("off_opt3"))
    print(t("off_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        missing = [pkg for pkg in office_official if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print(f"\n🎉 {t('off_all_official_installed')}")

    elif choice == "2":
        selected = select_custom_packages(office_official)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        if is_package_installed("onlyoffice-bin"):
            print(f"\n🎉 {t('off_onlyoffice_installed')}")
        else:
            install_packages(["onlyoffice-bin"], use_aur=True)

    input(f"\n{t('press_enter')}")