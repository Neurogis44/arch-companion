import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed


def get_multimedia_dicts():
    """Retourne les dictionnaires multimédia traduits dynamiquement."""
    official = {
        "ffmpeg": t("multi_desc_ffmpeg"),
        "gst-plugins-good": t("multi_desc_gst"),
        "vlc": t("multi_desc_vlc"),
    }
    popular = {
        "spotify-launcher": t("multi_desc_spotify"),
    }
    return official, popular


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print(f"\n⚠️ {t('multi_no_pkg_selected')}")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 {t('multi_launching_yay')} : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print(f"\n❌ {t('multi_yay_not_installed')}")
            print(f"👉 {t('multi_yay_hint')}")
    else:
        print(f"\n🚀 {t('multi_launching_pacman')} : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_multimedia_module():
    """Affiche le module Multimédia bilingue."""
    multi_official, multi_popular = get_multimedia_dicts()

    print("\n" + "=" * 60)
    print(f"      {t('multi_title')}")
    print("=" * 60)
    print(f"{t('multi_analyzing')}\n")

    print(f"📦 {t('multi_status_header')} :")
    print(f"--- {t('multi_section_official')} ---")
    for pkg, desc in multi_official.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<20} : {desc}")

    print(f"\n--- {t('multi_section_popular')} ---")
    for pkg, desc in multi_popular.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<20} : {desc}")

    print("\n------------------------------------------------------------")
    print(t("multi_opt1"))
    print(t("multi_opt2"))
    print(t("multi_opt3"))
    print(t("multi_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        missing = [pkg for pkg in multi_official if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print(f"\n🎉 {t('multi_all_official_installed')}")

    elif choice == "2":
        selected = []
        for pkg, desc in multi_official.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('multi_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        if is_package_installed("spotify") or is_package_installed("spotify-launcher"):
            print(f"\n🎉 {t('multi_spotify_installed')}")
        else:
            install_packages(["spotify-launcher"], use_aur=True)

    input(f"\n{t('press_enter')}")