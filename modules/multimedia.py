import shutil
import subprocess
from services.system import is_package_installed

MULTIMEDIA_OFFICIAL = {
    "ffmpeg": "Codecs audio/vidéo fondamentaux",
    "gst-plugins-good": "Plugins GStreamer indispensables",
    "vlc": "Lecteur multimédia universel",
}

MULTIMEDIA_POPULAR = {
    "spotify-launcher": "Lecteur Spotify officiel (Arch/AUR)",
}


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print("\n⚠️ Aucun paquet sélectionné.")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 Lancement de yay : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print("\n❌ 'yay' n'est pas installé sur ton système !")
            print("👉 Utilise le module 1 (Assistants AUR) pour l'installer d'abord.")
    else:
        print(f"\n🚀 Lancement de pacman : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_multimedia_module():
    """Affiche le module Multimédia épuré."""
    print("\n" + "=" * 60)
    print("      🎵 PARCOURS MULTIMÉDIA & CODECS")
    print("=" * 60)
    print("Analyse de tes applications multimédias...\n")

    print("📦 ÉTAT DES PAQUETS INCONTOURNABLES :")
    print("--- Dépôts Officiels ---")
    for pkg, desc in MULTIMEDIA_OFFICIAL.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<20} : {desc}")

    print("\n--- Sélection Populaire ---")
    for pkg, desc in MULTIMEDIA_POPULAR.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<20} : {desc}")

    print("\n------------------------------------------------------------")
    print("1. 🚀 Tout installer/compléter (Paquets officiels)")
    print("2. 🎯 Choisir les paquets officiels un par un")
    print("3. 🎧 Installer Spotify (spotify-launcher)")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        missing = [pkg for pkg in MULTIMEDIA_OFFICIAL if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print("\n🎉 Tous les paquets officiels sont déjà installés !")

    elif choice == "2":
        selected = []
        for pkg, desc in MULTIMEDIA_OFFICIAL.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        if is_package_installed("spotify") or is_package_installed("spotify-launcher"):
            print("\n🎉 Spotify est déjà détecté sur ta machine !")
        else:
            install_packages(["spotify-launcher"], use_aur=True)

    input("\nAppuie sur Entrée pour continuer...")