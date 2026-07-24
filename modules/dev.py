import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed


def get_dev_dicts():
    """Retourne les dictionnaires d'outils dev traduits dynamiquement."""
    editors = {
        "visual-studio-code-bin": t("dev_desc_vscode"),
        "vscodium": t("dev_desc_vscodium"),
    }
    languages = {
        "python": t("dev_desc_python"),
        "go": t("dev_desc_go"),
        "nodejs": t("dev_desc_node"),
    }
    tools = {
        "git": t("dev_desc_git"),
        "docker": t("dev_desc_docker"),
        "docker-compose": t("dev_desc_docker_compose"),
        "postman-bin": t("dev_desc_postman"),
    }
    return editors, languages, tools


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print(f"\n⚠️ {t('dev_no_pkg_selected')}")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 {t('dev_launching_yay')} : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print(f"\n❌ {t('dev_yay_not_installed')}")
            print(f"👉 {t('dev_yay_hint')}")
    else:
        print(f"\n🚀 {t('dev_launching_pacman')} : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_dev_module():
    """Affiche le module Outils Développeur bilingue."""
    dev_editors, dev_languages, dev_tools = get_dev_dicts()

    print("\n" + "=" * 60)
    print(f"      {t('dev_title')}")
    print("=" * 60)
    print(f"{t('dev_analyzing')}\n")

    print(f"📦 {t('dev_status_header')} :")
    print(f"--- {t('dev_section_editors')} ---")
    for pkg, desc in dev_editors.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<24} : {desc}")

    print(f"\n--- {t('dev_section_languages')} ---")
    for pkg, desc in dev_languages.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<24} : {desc}")

    print(f"\n--- {t('dev_section_tools')} ---")
    for pkg, desc in dev_tools.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<24} : {desc}")

    print("\n------------------------------------------------------------")
    print(t("dev_opt1"))
    print(t("dev_opt2"))
    print(t("dev_opt3"))
    print(t("dev_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        print(f"\n--- {t('dev_section_editors')} ---")
        for pkg, desc in dev_editors.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('dev_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                use_aur = "bin" in pkg
                install_packages([pkg], use_aur=use_aur)

    elif choice == "2":
        selected = []
        print(f"\n--- {t('dev_section_languages')} ---")
        for pkg, desc in dev_languages.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('dev_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        print(f"\n--- {t('dev_section_tools')} ---")
        for pkg, desc in dev_tools.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('dev_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                use_aur = "bin" in pkg
                install_packages([pkg], use_aur=use_aur)

    input(f"\n{t('press_enter')}")