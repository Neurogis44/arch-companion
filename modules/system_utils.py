import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed


def install_microcode():
    """Détecte le CPU et installe le microcode approprié (intel-ucode ou amd-ucode)."""
    try:
        with open("/proc/cpuinfo", "r") as f:
            cpu_info = f.read()

        if "AuthenticAMD" in cpu_info:
            pkg = "amd-ucode"
            print(f"\n🧠 {t('sys_cpu_amd')}")
        elif "GenuineIntel" in cpu_info:
            pkg = "intel-ucode"
            print(f"\n🧠 {t('sys_cpu_intel')}")
        else:
            print(f"\n⚠️ {t('sys_cpu_unknown')}")
            return

        if is_package_installed(pkg):
            print(f"🎉 {pkg} {t('sys_ucode_installed')}")
        else:
            print(f"🚀 {t('sys_installing')} {pkg}...")
            subprocess.run(["sudo", "pacman", "-S", "--needed", pkg], check=False)

    except Exception as e:
        print(f"❌ Error / Erreur : {e}")


def configure_reflector():
    """Installe et exécute Reflector pour trier les miroirs pacman les plus rapides."""
    print(f"\n🌐 {t('sys_reflector_launch')}")
    if not is_package_installed("reflector"):
        subprocess.run(["sudo", "pacman", "-S", "--needed", "reflector"], check=False)

    cmd = [
        "sudo",
        "reflector",
        "--protocol",
        "https",
        "--latest",
        "10",
        "--sort",
        "rate",
        "--save",
        "/etc/pacman.d/mirrorlist",
    ]
    print(f"🚀 Exécution : {' '.join(cmd)}\n")
    subprocess.run(cmd, check=False)
    print(f"🎉 {t('sys_reflector_success')}")


def configure_firewall():
    """Installe et active le pare-feu UFW."""
    print(f"\n🛡️ {t('sys_ufw_launch')}")
    if not is_package_installed("ufw"):
        subprocess.run(["sudo", "pacman", "-S", "--needed", "ufw"], check=False)

    print(f"🚀 {t('sys_ufw_enabling')}...")
    subprocess.run(["sudo", "systemctl", "enable", "--now", "ufw"], check=False)
    print(f"🎉 {t('sys_ufw_success')}")


def show_system_utils_module():
    """Affiche le module Utilitaires Système."""
    print("\n" + "=" * 60)
    print(f"      {t('sys_title')}")
    print("=" * 60)
    print(f"{t('sys_analyzing')}\n")

    has_reflector = is_package_installed("reflector")
    has_ufw = is_package_installed("ufw")

    print(f"📦 {t('sys_tools_status')} :")
    print(f"  [{'✓' if has_reflector else ' '}] Reflector : {t('sys_reflector_desc')}")
    print(f"  [{'✓' if has_ufw else ' '}] UFW (Uncomplicated Firewall) : {t('sys_ufw_desc')}")

    print("\n------------------------------------------------------------")
    print(t("sys_opt1"))
    print(t("sys_opt2"))
    print(t("sys_opt3"))
    print(t("sys_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        install_microcode()
    elif choice == "2":
        configure_reflector()
    elif choice == "3":
        configure_firewall()

    input(f"\n{t('press_enter')}")