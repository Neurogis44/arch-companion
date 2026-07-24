import os
import subprocess
from services.i18n import t
from services.system import is_package_installed

# Paquets essentiels communs à TOUS les bureaux (Polices, Bluetooth, Impression, Wayland)
COMMON_PACKAGES = [
    "noto-fonts",
    "noto-fonts-emoji",
    "ttf-dejavu",
    "bluez",
    "bluez-utils",
    "cups",
    "xdg-desktop-portal",
]

# Paquets spécifiques pour KDE Plasma
KDE_PACKAGES = [
    "plasma-nm",
    "bluedevil",
    "ark",
    "p7zip",
    "unrar",
    "spectacle",
    "gwenview",
    "kate",
    "dolphin-plugins",
    "ffmpegthumbs",
    "xdg-desktop-portal-kde",
]

# Paquets spécifiques pour GNOME
GNOME_PACKAGES = [
    "gnome-tweaks",
    "gnome-browser-connector",
    "file-roller",
    "p7zip",
    "unrar",
    "eog",
    "gnome-bluetooth-3.0",
    "xdg-desktop-portal-gnome",
]

# Paquets spécifiques pour XFCE
XFCE_PACKAGES = [
    "thunar-archive-plugin",
    "p7zip",
    "unrar",
    "xfce4-goodies",
    "pavucontrol",
    "xdg-desktop-portal-gtk",
]


def detect_desktop_environment() -> str:
    """Détecte l'environnement de bureau actuel via la variable d'environnement XDG."""
    desktop = os.environ.get("XDG_CURRENT_DESKTOP", "").upper()
    if "KDE" in desktop or "PLASMA" in desktop:
        return "KDE"
    elif "GNOME" in desktop:
        return "GNOME"
    elif "XFCE" in desktop:
        return "XFCE"
    return "UNKNOWN"


def install_desktop_fix(packages: list):
    """Installe les paquets manquants et active les services essentiels (Bluetooth/CUPS)."""
    missing = [pkg for pkg in packages if not is_package_installed(pkg)]

    if not missing:
        print(f"\n🎉 {t('de_already_complete')}")
        return

    print(f"\n🚀 {t('de_installing_missing')} : {', '.join(missing)}\n")
    subprocess.run(["sudo", "pacman", "-S", "--needed"] + missing, check=False)

    # Activation automatique des services système vitaux
    if is_package_installed("bluez"):
        print(f"\n⚙️ {t('de_enabling_bluetooth')}...")
        subprocess.run(["sudo", "systemctl", "enable", "--now", "bluetooth"], check=False)

    if is_package_installed("cups"):
        print(f"⚙️ {t('de_enabling_cups')}...")
        subprocess.run(["sudo", "systemctl", "enable", "--now", "cups"], check=False)


def show_desktop_fix_module():
    """Affiche le module de complétion de l'environnement de bureau."""
    de = detect_desktop_environment()

    print("\n" + "=" * 60)
    print(f"      {t('de_title')}")
    print("=" * 60)
    print(f"{t('de_analyzing')}\n")

    print(f"🖥️ {t('de_detected')} : {de}")

    target_packages = list(COMMON_PACKAGES)
    if de == "KDE":
        target_packages.extend(KDE_PACKAGES)
    elif de == "GNOME":
        target_packages.extend(GNOME_PACKAGES)
    elif de == "XFCE":
        target_packages.extend(XFCE_PACKAGES)

    print(f"\n📦 {t('de_status_header')} :")
    for pkg in target_packages:
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg}")

    print("\n------------------------------------------------------------")
    print(t("de_opt1"))
    print(t("de_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        install_desktop_fix(target_packages)

    input(f"\n{t('press_enter')}")