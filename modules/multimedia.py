import subprocess
import shutil

# Liste des paquets recommandés par le Wiki pour les codecs et polices de base
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
    """Affiche le module d'installation des codecs et polices."""
    print("\n" + "=" * 50)
    print("      🎵 PARCOURS MULTIMÉDIA & CODECS")
    print("=" * 50)
    print("Ce module va installer les codecs audio/vidéo essentiels")
    print("et les polices de caractères de base pour Arch Linux.\n")
    
    print("📦 Paquets concernés :")
    for pkg in MULTIMEDIA_PACKAGES:
        print(f"  • {pkg}")
    
    print("\n📖 Arch Wiki : https://wiki.archlinux.org/title/Codecs_and_containers")
    print("💻 Commande qui sera exécutée :")
    cmd_str = f"sudo pacman -S --needed {' '.join(MULTIMEDIA_PACKAGES)}"
    print(f"   {cmd_str}\n")
    
    choice = input("👉 Veux-tu lancer l'installation ? (o/N) : ").strip().lower()
    
    if choice == "o":
        print("\n🚀 Lancement de pacman...\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + MULTIMEDIA_PACKAGES, check=False)
    else:
        print("\n❌ Installation annulée.")
        
    input("\nAppuie sur Entrée pour revenir au menu principal...")