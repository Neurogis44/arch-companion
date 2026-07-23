import subprocess
from services.system import is_package_installed

SYSTEM_PACKAGES = [
    "reflector",
    "ufw",
    "micro",
    "bash-completion",
]

def show_system_utils_module():
    """Affiche le module Utilitaires Système avec diagnostic."""
    print("\n" + "=" * 50)
    print("      🛠️ PARCOURS UTILITAIRES SYSTÈME")
    print("=" * 50)
    print("Analyse de ton système en cours...\n")

    print("💡 RAPPELS ARCH WIKI :")
    print("  • Reflector : Miroirs pacman ultra rapides.")
    print("  • UFW : Pare-feu simple à activer (sudo ufw enable).")
    print("  • Micro : Éditeur de texte très intuitif dans le terminal.")
    print("📖 Arch Wiki : https://wiki.archlinux.org/title/System_maintenance\n")

    missing_packages = []
    print("📦 État des paquets sur ta machine :")
    for pkg in SYSTEM_PACKAGES:
        if is_package_installed(pkg):
            print(f"  [✓] {pkg} (Déjà installé)")
        else:
            print(f"  [ ] {pkg} (Manquant)")
            missing_packages.append(pkg)

    if not missing_packages:
        print("\n🎉 Tous les utilitaires système essentiels sont déjà installés !")
        input("\nAppuie sur Entrée pour revenir au menu principal...")
        return

    print(f"\n💻 Commande qui sera exécutée ({len(missing_packages)} paquet(s) à installer) :")
    cmd_str = f"sudo pacman -S --needed {' '.join(missing_packages)}"
    print(f"   {cmd_str}\n")

    choice = input("👉 Veux-tu installer les paquets manquants ? (o/N) : ").strip().lower()

    if choice == "o":
        print("\n🚀 Lancement de pacman...\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + missing_packages, check=False)
    else:
        print("\n❌ Installation annulée.")

    input("\nAppuie sur Entrée pour revenir au menu principal...")