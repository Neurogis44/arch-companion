import os
import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed

BACKUP_FILE = os.path.expanduser("~/arch_packages_backup.txt")


def export_package_list():
    """Exporte la liste complète des paquets explicitement installés."""
    print(f"\n📄 {t('bk_exporting')} {BACKUP_FILE}...")
    try:
        pacman_pkgs = subprocess.check_output(["pacman", "-Qqen"], text=True).splitlines()
        aur_pkgs = subprocess.check_output(["pacman", "-Qqem"], text=True).splitlines()

        with open(BACKUP_FILE, "w") as f:
            f.write("# ARCH COMPANION - PACKAGE BACKUP\n")
            f.write("--- OFFICIAL ---:\n")
            f.write("\n".join(pacman_pkgs) + "\n")
            f.write("--- AUR ---:\n")
            f.write("\n".join(aur_pkgs) + "\n")

        print(f"🎉 {t('bk_export_success')} : {BACKUP_FILE}")
    except Exception as e:
        print(f"❌ Erreur : {e}")


def restore_package_list():
    """Restaure les paquets à partir du fichier de sauvegarde."""
    if not os.path.exists(BACKUP_FILE):
        print(f"\n❌ {t('bk_no_backup')} : {BACKUP_FILE}")
        return

    print(f"\n🔍 {t('bk_reading')} {BACKUP_FILE}...")
    official_pkgs = []
    aur_pkgs = []
    current_section = None

    with open(BACKUP_FILE, "r") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            if line == "--- OFFICIAL ---:":
                current_section = "official"
                continue
            elif line == "--- AUR ---:":
                current_section = "aur"
                continue

            if current_section == "official":
                official_pkgs.append(line)
            elif current_section == "aur":
                aur_pkgs.append(line)

    print(f"📦 {t('bk_official_found')} : {len(official_pkgs)}")
    print(f"🧬 {t('bk_aur_found')}      : {len(aur_pkgs)}")

    choice = input(f"\n👉 {t('bk_ask_reinstall')} (o/N / y/N) : ").strip().lower()
    if choice in ["o", "y"]:
        if official_pkgs:
            print(f"\n🚀 {t('bk_installing_official')}...")
            subprocess.run(["sudo", "pacman", "-S", "--needed"] + official_pkgs, check=False)
        if aur_pkgs and shutil.which("yay"):
            print(f"\n🚀 {t('bk_installing_aur')}...")
            subprocess.run(["yay", "-S", "--needed"] + aur_pkgs, check=False)


def create_snapshot():
    """Crée un snapshot système avec Timeshift ou Snapper."""
    has_timeshift = shutil.which("timeshift")
    has_snapper = shutil.which("snapper")

    if has_snapper:
        print(f"\n📸 {t('bk_snapper_detected')}")
        comment = input(f"👉 {t('bk_snapshot_desc')} : ").strip()
        if not comment:
            comment = "Arch Companion Snapshot"
        subprocess.run(["sudo", "snapper", "create", "--description", comment], check=False)
        print(f"🎉 {t('bk_snapper_success')}")

    elif has_timeshift:
        print(f"\n📸 {t('bk_timeshift_creating')}")
        comment = input(f"👉 {t('bk_snapshot_desc')} : ").strip()
        if not comment:
            comment = "Arch Companion Snapshot"
        subprocess.run(["sudo", "timeshift", "--create", "--comments", comment], check=False)

    else:
        print(f"\n❌ {t('bk_no_snapshot_tool')}")
        choice = input(f"👉 {t('bk_install_timeshift')} (o/N / y/N) : ").strip().lower()
        if choice in ["o", "y"]:
            subprocess.run(["sudo", "pacman", "-S", "--needed", "timeshift"], check=False)


def show_backup_module():
    """Affiche le module de sauvegarde."""
    print("\n" + "=" * 60)
    print(f"      {t('bk_title')}")
    print("=" * 60)
    print(f"{t('bk_analyzing')}\n")

    has_timeshift = is_package_installed("timeshift")
    has_snapper = is_package_installed("snapper")

    print(f"📦 {t('bk_tools_status')} :")
    status_ts = f"[✓] {t('installed')}" if has_timeshift else f"[ ] {t('missing')}"
    status_sn = f"[✓] {t('installed')}" if has_snapper else f"[ ] {t('missing')}"
    print(f"  {status_ts} timeshift : {t('bk_ts_desc')}")
    print(f"  {status_sn} snapper   : {t('bk_sn_desc')}")

    backup_exists = f" ({t('bk_file_present')})" if os.path.exists(BACKUP_FILE) else f" ({t('bk_file_missing')})"
    print(f"\n📄 {t('bk_file_label')} : {BACKUP_FILE}{backup_exists}")

    print("\n------------------------------------------------------------")
    print(t("bk_opt1"))
    print(t("bk_opt2"))
    print(t("bk_opt3"))
    print(t("bk_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        export_package_list()
    elif choice == "2":
        restore_package_list()
    elif choice == "3":
        create_snapshot()

    input(f"\n{t('press_enter')}")