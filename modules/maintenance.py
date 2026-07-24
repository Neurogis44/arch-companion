import subprocess
from services.i18n import t
from services.system import check_failed_services


def show_maintenance_module():
    """Affiche le module de maintenance système bilingue."""
    print("\n" + "=" * 50)
    print(f"      {t('maint_title')}")
    print("=" * 50)
    print(f"{t('maint_analyzing')}\n")

    # 1. Diagnostic des services systemd en échec
    failed = check_failed_services()
    if failed:
        print(f" ⚠️ ATTENTION : {len(failed)} service(s) systemd en échec / failed :")
        for srv in failed:
            print(f"    • {srv}")
        print("   👉 Status : systemctl status <service>")
    else:
        print(f" {t('maint_services_ok')}")

    print(f"\n{t('maint_options')}")
    print(t("maint_opt1"))
    print(t("maint_opt2"))
    print(t("maint_opt0"))
    print()

    choice = input(t("choice")).strip()

    if choice == "1":
        print("\n🚀 Nettoyage du cache pacman (paccache -r)...")
        subprocess.run(["sudo", "paccache", "-r"], check=False)

    elif choice == "2":
        print(f"\n{t('maint_searching_orphans')}")
        try:
            # On vérifie d'abord s'il y a des orphelins
            result = subprocess.run(
                ["pacman", "-Qtdq"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )

            orphans = result.stdout.strip().splitlines()

            if not orphans or not result.stdout.strip():
                print(f"\n{t('maint_no_orphans')}")
            else:
                print(f"\n📦 {len(orphans)} orphan(s) / orphelin(s) : {', '.join(orphans)}")
                cmd_str = f"sudo pacman -Rns {' '.join(orphans)}"
                print(f"🚀 Exécution : {cmd_str}\n")
                subprocess.run(["sudo", "pacman", "-Rns"] + orphans, check=False)

        except Exception as e:
            print(f"\n❌ Error / Erreur : {e}")

    input(f"\n{t('press_enter')}")