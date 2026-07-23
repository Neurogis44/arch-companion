import subprocess
from services.system import is_package_installed

MULTIMEDIA_PACKAGES = [
    "ffmpeg",
    "gst-plugins-good",
    "gst-plugins-bad",
    "gst-plugins-ugly",
    "gst-libav",
    "ttf-dejavu",
    "ttf-liberation",
    "noto-fonts",
]

def show_multimedia_module():
    """Affiche le module d'installation des codecs et polices avec diagnostic."""
    print("\n" + "=" * 50)
    print("      🎵 PARCOURS MULTIMÉDIA & CODECS")
    print("=" * 50)
    print("Analyse de ton système en cours...\n")

    # Diagnostic des paquets installés vs manquants
    missing_packages = []
    
    print("📦 État des paquets sur ta machine :")
    for pkg in MULTIMEDIA_PACKAGES:
        if is_package_installed(pkg):
            print(f"  [✓] {pkg} (Déjà installé)")
        else:
            print(f"  [ ] {pkg} (Manquant)")
            missing_packages.append(pkg)

    print("\n📖 Arch Wiki : https://wiki.archlinux.org/title/Codecs_and_containers")

    # Si tout est déjà installé, on informe l'utilisateur !
    if not missing_packages:
        print("\n🎉 Félicitations ! Tous les codecs et polices de ce module sont déjà installés.")
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