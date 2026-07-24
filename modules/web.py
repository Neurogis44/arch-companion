import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed


def get_browsers_dicts():
    """Retourne les dictionnaires de navigateurs traduits dynamiquement."""
    open_source = {
        "firefox": t("web_desc_firefox"),
        "chromium": t("web_desc_chromium"),
        "brave-bin": t("web_desc_brave"),
    }
    proprietary = {
        "google-chrome": t("web_desc_chrome"),
        "microsoft-edge-stable-bin": t("web_desc_edge"),
        "vivaldi": t("web_desc_vivaldi"),
    }
    return open_source, proprietary


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print(f"\n⚠️ {t('web_no_pkg_selected')}")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 {t('web_launching_yay')} : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print(f"\n❌ {t('web_yay_not_installed')}")
            print(f"👉 {t('web_yay_hint')}")
    else:
        print(f"\n🚀 {t('web_launching_pacman')} : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_web_module():
    """Affiche le module des navigateurs web bilingue."""
    browsers_os, browsers_prop = get_browsers_dicts()

    print("\n" + "=" * 60)
    print(f"      {t('web_title')}")
    print("=" * 60)
    print(f"{t('web_analyzing')}\n")

    print(f"📦 {t('web_status_header')} :")
    print(f"--- {t('web_section_os')} ---")
    for pkg, desc in browsers_os.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<26} : {desc}")

    print(f"\n--- {t('web_section_prop')} ---")
    for pkg, desc in browsers_prop.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<26} : {desc}")

    print("\n------------------------------------------------------------")
    print(t("web_opt1"))
    print(t("web_opt2"))
    print(t("web_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        print(f"\n--- {t('web_section_os')} ---")
        for pkg, desc in browsers_os.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('web_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                use_aur = pkg.endswith("-bin")
                install_packages([pkg], use_aur=use_aur)

    elif choice == "2":
        print(f"\n--- {t('web_section_prop')} ---")
        for pkg, desc in browsers_prop.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('web_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                use_aur = "chrome" in pkg or "edge" in pkg
                install_packages([pkg], use_aur=use_aur)

    input(f"\n{t('press_enter')}")