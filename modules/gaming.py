import shutil
import subprocess
from services.i18n import t
from services.system import get_gpu_vendor, is_multilib_enabled, is_package_installed


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print(f"\n⚠️ {t('game_no_pkg_selected')}")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 {t('game_launching_yay')} : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print(f"\n❌ {t('game_yay_not_installed')}")
            print(f"👉 {t('game_yay_hint')}")
    else:
        print(f"\n🚀 {t('game_launching_pacman')} : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_gaming_module():
    """Affiche le module Gaming bilingue avec sélection sur-mesure."""
    print("\n" + "=" * 60)
    print(f"        {t('game_title')}")
    print("=" * 60)
    print(f"{t('game_analyzing')}\n")

    if is_multilib_enabled():
        print(f" {t('game_multilib_enabled')}")
    else:
        print(f" {t('game_multilib_disabled')}")
        print(f"      👉 {t('game_multilib_hint')}\n")

    vendor = get_gpu_vendor()

    # Dictionnaire des paquets adaptés au GPU
    official_packages = {
        "steam": t("game_desc_steam"),
        "gamemode": t("game_desc_gamemode"),
        "lib32-gamemode": t("game_desc_lib32_gamemode"),
        "mangohud": t("game_desc_mangohud"),
        "goverlay": t("game_desc_goverlay"),
        "vulkan-icd-loader": t("game_desc_vulkan_loader"),
        "lib32-vulkan-icd-loader": t("game_desc_lib32_vulkan_loader"),
        "lutris": t("game_desc_lutris"),
    }

    aur_packages = {
        "heroic-games-launcher-bin": t("game_desc_heroic"),
    }

    if vendor == "NVIDIA":
        print(f" 🟢 {t('game_gpu_nvidia')}")
        official_packages["nvidia-utils"] = t("game_desc_nvidia_utils")
        official_packages["lib32-nvidia-utils"] = t("game_desc_lib32_nvidia_utils")
    elif vendor == "AMD":
        print(f" 🔴 {t('game_gpu_amd')}")
        official_packages["vulkan-radeon"] = t("game_desc_vulkan_radeon")
        official_packages["lib32-vulkan-radeon"] = t("game_desc_lib32_vulkan_radeon")
        official_packages["lact"] = t("game_desc_lact")
    elif vendor == "INTEL":
        print(f" 🔵 {t('game_gpu_intel')}")
        official_packages["vulkan-intel"] = t("game_desc_vulkan_intel")
        official_packages["lib32-vulkan-intel"] = t("game_desc_lib32_vulkan_intel")

    print(f"\n📦 {t('game_status_header')} :")
    print(f"--- {t('game_section_official')} ---")
    for pkg, desc in official_packages.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<25} : {desc}")

    print(f"\n--- {t('game_section_aur')} ---")
    for pkg, desc in aur_packages.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<25} : {desc}")

    print("\n------------------------------------------------------------")
    print(t("game_opt1"))
    print(t("game_opt2"))
    print(t("game_opt3"))
    print(t("game_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        missing = [pkg for pkg in official_packages if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
            # Activation du service LACT si installé
            if "lact" in missing:
                print("\n⚙️ Activation du service lactd...")
                subprocess.run(["sudo", "systemctl", "enable", "--now", "lactd"], check=False)
        else:
            print(f"\n🎉 {t('game_all_official_installed')}")

    elif choice == "2":
        selected = []
        print(f"\n--- {t('game_custom_selection')} ---")
        for pkg, desc in official_packages.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('game_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)
            if "lact" in selected:
                print("\n⚙️ Activation du service lactd...")
                subprocess.run(["sudo", "systemctl", "enable", "--now", "lactd"], check=False)

    elif choice == "3":
        if is_package_installed("heroic-games-launcher-bin"):
            print(f"\n🎉 {t('game_heroic_installed')}")
        else:
            install_packages(["heroic-games-launcher-bin"], use_aur=True)

    input(f"\n{t('press_enter')}")