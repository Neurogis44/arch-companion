import subprocess
from services.system import check_failed_services

def show_maintenance_module():
    """Affiche le module de maintenance système et nettoyage du cache."""
    print("\n" + "=" * 50)
    print("      🧹 MAINTENANCE & SANTÉ DU SYSTÈME")
    print("=" * 50)
    print("Analyse de la santé du système en cours...\n")

    # 1. Diagnostic des services systemd en échec
    failed = check_failed_services()
    if failed:
        print(f" ⚠️ ATTENTION : {len(failed)} service(s) systemd en échec :")
        for srv in failed:
            print(f"    • {srv}")
        print("   👉 Commande pour inspecter : systemctl status <service>")
    else:
        print(" [✓] Services systemd : Tous les services fonctionnent normalement !")

    print("\n--- OPTIONS DE NETTOYAGE ---")
    print("1. 🧹 Nettoyer le cache pacman (Garder uniquement les 2 dernières versions)")
    print("2. 🗑️ Supprimer les paquets orphelins (Paquets installés comme dépendances inutilisées)")
    print("0. ↩️ Annuler")
    print()

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        print("\n🚀 Nettoyage du cache pacman (paccache -r)...")
        subprocess.run(["sudo", "paccache", "-r"], check=False)
    elif choice == "2":
        print("\n🔍 Recherche et suppression des orphelins...")
        cmd = "sudo pacman -Rns $(pacman -Qtdq)"
        print(f"Commande : {cmd}")
        subprocess.run(cmd, shell=True, check=False)

    input("\nAppuie sur Entrée pour revenir au menu principal...")