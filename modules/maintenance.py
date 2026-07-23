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
        print("\n🔍 Recherche des paquets orphelins...")
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
                print("\n🎉 Aucun paquet orphelin trouvé ! Ton système est parfaitement propre.")
            else:
                print(f"\n📦 {len(orphans)} paquet(s) orphelin(s) trouvé(s) : {', '.join(orphans)}")
                cmd_str = f"sudo pacman -Rns {' '.join(orphans)}"
                print(f"🚀 Exécution : {cmd_str}\n")
                subprocess.run(["sudo", "pacman", "-Rns"] + orphans, check=False)

        except Exception as e:
            print(f"\n❌ Erreur lors de la recherche d'orphelins : {e}")

    input("\nAppuie sur Entrée pour revenir au menu principal...")