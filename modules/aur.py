import subprocess
import shutil

def show_aur_module():
    """Affiche le module pour l'installation des assistants AUR (yay / pamac)."""
    print("\n" + "=" * 60)
    print("      📦 ASSISTANTS AUR (ARCH USER REPOSITORY)")
    print("=" * 60)
    print("L'AUR est le dépôt communautaire d'Arch Linux.")
    print("Pour y accéder facilement, tu peux installer un assistant (helper).\n")

    print("💡 RAPPEL IMPORTANT ARCH WIKI :")
    print("  • Les assistants AUR ne remplacent pas pacman.")
    print("  • Les paquets AUR sont créés par la communauté (sois prudent).")
    print("  • Le groupe 'base-devel' et 'git' sont requis pour compiler.")
    print("📖 Arch Wiki AUR : https://wiki.archlinux.org/title/Arch_User_Repository\n")

    print("--- CHOIX DE L'ASSISTANT ---")
    print("1. ⚡ yay       (Léger, rapide, en ligne de commande)")
    print("2. 🎨 pamac-aur (Interface graphique moderne avec recherche)")
    print("3. 🛠️ Les deux  (yay + pamac-aur)")
    print("0. ↩️ Retour")
    print()

    choice = input("👉 Ton choix : ").strip()

    if choice in ["1", "2", "3"]:
        print("\n🔧 Étape 1 : Vérification / Installation de base-devel et git...")
        subprocess.run(["sudo", "pacman", "-S", "--needed", "base-devel", "git"], check=False)

        if choice in ["1", "3"]:
            print("\n--------------------------------------------------")
            print("📦 Installation de YAY...")
            print("Commande : git clone + makepkg -si")
            print("--------------------------------------------------")
            input("Appuie sur Entrée pour lancer la compilation de yay...")
            # Procédure standard recommandée par le Wiki pour compiler un helper AUR
            cmd = "cd /tmp && rm -rf yay-bin && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si --noconfirm"
            subprocess.run(cmd, shell=True, check=False)

        if choice in ["2", "3"]:
            print("\n--------------------------------------------------")
            print("📦 Installation de PAMAC-AUR...")
            print("Note : pamac nécessite yay pour être compilé depuis l'AUR.")
            print("--------------------------------------------------")
            if not shutil.which("yay"):
                print("⚠️ yay n'est pas détecté. On l'installe d'abord pour compiler pamac.")
                cmd_yay = "cd /tmp && rm -rf yay-bin && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si --noconfirm"
                subprocess.run(cmd_yay, shell=True, check=False)

            input("Appuie sur Entrée pour lancer l'installation de pamac-aur...")
            subprocess.run(["yay", "-S", "--needed", "pamac-aur"], check=False)

        print("\n✅ Opération terminée !")
    else:
        print("\n❌ Retour au menu principal.")

    input("\nAppuie sur Entrée pour continuer...")