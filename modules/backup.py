import os
import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed

BACKUP_FILE = os.path.expanduser("~/arch_packages_backup.txt")


def export_package_list():
    """Exporte la liste complète des paquets explicitement installés."""
    print(f"\n📄 Exporation de la liste des paquets dans {BACKUP_FILE}...")
    try:
        # Paquets pacman officiels
        pacman_pkgs = subprocess.check_output(
            ["pacman", "-Qqen"], text=True
        ).splitlines()
        # Paquets AUR
        aur_pkgs = subprocess.check_output(
            ["pacman", "-Qqem"], text=True
        ).splitlines()

        with open(BACKUP_FILE, "w") as f:
            f.write("# ARCH COMPANION - PACKAGE BACKUP\n")
            f.write("--- OFFICIAL ---:\n")
            f.write("\n".join(pacman_pkgs) + "\n")
            f.write("--- AUR ---:\n")
            f.write("\n".join(aur_pkgs) + "\n")

        print(f"🎉 Sauvegarde réussie ! Fichier créé : {BACKUP_FILE}")
    except Exception as e:
        print(f"❌ Erreur lors de l'exportation : {e}")


def restore_package_list():
    """Restaure les paquets à partir du fichier de sauvegarde."""
    if not os.path.exists(BACKUP_FILE):
        print(f"\n❌ Aucun fichier de sauvegarde trouvé à l'emplacement : {BACKUP_FILE}")
        return

    print(f"\n🔍 Lecture du fichier {BACKUP_FILE}...")
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

    print(f"📦 Paquets officiels détectés : {len(official_pkgs)}")
    print(f"🧬 Paquets AUR détectés       : {len(aur_pkgs)}")

    choice = input("\n👉 Lancer la réinstallation des paquets manquants ? (o/N) : ").strip().lower()
    if choice == "o":
        if official_pkgs:
            print("\n🚀 Installation des paquets officiels...")
            subprocess.run(["sudo", "pacman", "-S", "--needed"] + official_pkgs, check=False)
        if aur_pkgs and shutil.which("yay"):
            print("\n🚀 Installation des paquets AUR avec yay...")
            subprocess.run(["yay", "-S", "--needed"] + aur_pkgs, check=False)


def create_snapshot():
    """Crée un snapshot système avec Timeshift ou Snapper."""
    has_timeshift = shutil.which("timeshift")
    has_snapper = shutil.which("snapper")

    if has_snapper:
        print("\n📸 Snapper détecté sur ton système Btrfs !")
        comment = input("👉 Description du snapshot (ex: Avant maj) : ").strip()
        if not comment:
            comment = "Arch Companion Snapshot"
        cmd = f"sudo snapper create --description '{comment}'"
        print(f"🚀 Exécution : {cmd}")
        subprocess.run(["sudo", "snapper", "create", "--description", comment], check=False)
        print("🎉 Snapshot Snapper créé avec succès !")

    elif has_timeshift:
        print("\n📸 Création d'un snapshot système avec Timeshift...")
        comment = input("👉 Description du snapshot (ex: Avant maj) : ").strip()
        if not comment:
            comment = "Arch Companion Snapshot"
        subprocess.run(["sudo", "timeshift", "--create", "--comments", comment], check=False)

    else:
        print("\n❌ Aucun outil de snapshot (Timeshift/Snapper) n'est installé.")
        choice = input("👉 Veux-tu installer Timeshift (pacman) ? (o/N) : ").strip().lower()
        if choice == "o":
            subprocess.run(["sudo", "pacman", "-S", "--needed", "timeshift"], check=False)


def show_backup_module():
    """Affiche le module de sauvegarde et points de restauration."""
    print("\n" + "=" * 60)
    print("      🛡️ SAUVEGARDE & POINTS DE RESTAURATION")
    print("=" * 60)
    print("Analyse des outils de sécurité...\n")

    has_timeshift = is_package_installed("timeshift")
    has_snapper = is_package_installed("snapper")

    print("📦 ÉTAT DES OUTILS DE RESTAURATION :")
    status_ts = "[✓] Déjà installé" if has_timeshift else "[ ] Non installé"
    status_sn = "[✓] Déjà installé" if has_snapper else "[ ] Non installé"
    print(f"  {status_ts} timeshift : Outil de snapshots système simples")
    print(f"  {status_sn} snapper   : Outil Btrfs avancé pour snapshots")

    backup_exists = " (Fichier présent)" if os.path.exists(BACKUP_FILE) else " (Aucun fichier)"
    print(f"\n📄 Fichier de liste de paquets : {BACKUP_FILE}{backup_exists}")

    print("\n------------------------------------------------------------")
    print("1. 💾 Exporter ma liste de paquets (Sauvegarde .txt)")
    print("2. 📥 Restaurer mes paquets depuis la sauvegarde .txt")
    print("3. 📸 Créer un Snapshot système (Timeshift)")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        export_package_list()
    elif choice == "2":
        restore_package_list()
    elif choice == "3":
        create_timeshift_snapshot()

    input("\nAppuie sur Entrée pour continuer...")