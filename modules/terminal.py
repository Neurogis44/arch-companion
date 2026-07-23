import os
import shutil
import subprocess
from services.system import is_package_installed

ALIASES_TO_ADD = """
# === ARCH COMPANION ALIASES ===
alias update='sudo pacman -Syu'
alias cleanup='sudo paccache -r && sudo pacman -Rns $(pacman -Qtdq)'
alias mirror='sudo reflector --protocol https --latest 10 --sort rate --save /etc/pacman.d/mirrorlist'
alias l='ls -lha --color=auto'
# ==============================
"""


def detect_shell_config() -> str:
    """Détermine quel fichier de config utiliser (~/.bashrc ou ~/.zshrc)."""
    shell = os.environ.get("SHELL", "")
    if "zsh" in shell:
        return os.path.expanduser("~/.zshrc")
    return os.path.expanduser("~/.bashrc")


def inject_aliases():
    """Ajoute les alias utiles dans le fichier de configuration du Shell."""
    config_file = detect_shell_config()
    file_name = os.path.basename(config_file)

    if not os.path.exists(config_file):
        # Crée le fichier s'il n'existe pas
        open(config_file, "w").close()

    with open(config_file, "r") as f:
        content = f.read()

    if "ARCH COMPANION ALIASES" in content:
        print(f"\n🎉 Les alias sont déjà présents dans ton {file_name} !")
        return

    print(f"\n📝 Ajout des alias dans {config_file}...")
    try:
        with open(config_file, "a") as f:
            f.write(ALIASES_TO_ADD)
        print(f"✅ Alias ajoutés avec succès dans {file_name} !")
        print("💡 Exécute 'source ~/.bashrc' (ou relance ton terminal) pour les activer.")
    except Exception as e:
        print(f"❌ Erreur lors de l'écriture : {e}")


def install_starship():
    """Installe Starship Prompt pour un terminal moderne et rapide."""
    print("\n🚀 Installation de Starship Prompt...")
    if not is_package_installed("starship"):
        subprocess.run(["sudo", "pacman", "-S", "--needed", "starship"], check=False)

    config_file = detect_shell_config()
    with open(config_file, "r") as f:
        content = f.read()

    starship_line = 'eval "$(starship init bash)"' if "bash" in config_file else 'eval "$(starship init zsh)"'

    if starship_line not in content:
        with open(config_file, "a") as f:
            f.write(f"\n# Starship Prompt\n{starship_line}\n")
        print(f"✅ Starship a été activé dans {os.path.basename(config_file)} !")
    else:
        print("🎉 Starship est déjà configuré dans ton shell !")


def show_terminal_module():
    """Affiche le module Personnalisation du Terminal."""
    print("\n" + "=" * 60)
    print("      🎨 LOOK & CONFORT DU TERMINAL")
    print("=" * 60)
    print("Analyse de la configuration de ton terminal...\n")

    current_shell_config = detect_shell_config()
    has_starship = is_package_installed("starship")
    has_zsh = is_package_installed("zsh")
    has_fastfetch = is_package_installed("fastfetch")

    print("📦 ÉTAT DES OUTILS TERMINAL :")
    print(f"  [✓] Shell détecté          : {os.environ.get('SHELL', 'Inconnu')}")
    print(f"  [{'✓' if has_starship else ' '}] Starship Prompt        : Invite de commande moderne & rapide")
    print(f"  [{'✓' if has_zsh else ' '}] Shell Zsh              : Alternative puissante à Bash")
    print(f"  [{'✓' if has_fastfetch else ' '}] Fastfetch              : Affichage esthétique des infos système")

    print("\n------------------------------------------------------------")
    print("1. ⚡ Injecter les alias Arch utiles (update, cleanup, mirror)")
    print("2. 🚀 Installer & Configurer Starship Prompt")
    print("3. 🐚 Installer le Shell Zsh")
    print("4. 🖼️ Installer Fastfetch")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        inject_aliases()
    elif choice == "2":
        install_starship()
    elif choice == "3":
        subprocess.run(["sudo", "pacman", "-S", "--needed", "zsh"], check=False)
    elif choice == "4":
        subprocess.run(["sudo", "pacman", "-S", "--needed", "fastfetch"], check=False)

    input("\nAppuie sur Entrée pour continuer...")