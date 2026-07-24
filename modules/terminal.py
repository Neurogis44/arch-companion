import os
import shutil
import subprocess
from services.i18n import t
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
        open(config_file, "w").close()

    with open(config_file, "r") as f:
        content = f.read()

    if "ARCH COMPANION ALIASES" in content:
        print(f"\n🎉 {t('term_aliases_already_present')} {file_name} !")
        return

    print(f"\n📝 {t('term_adding_aliases')} {config_file}...")
    try:
        with open(config_file, "a") as f:
            f.write(ALIASES_TO_ADD)
        print(f"✅ {t('term_aliases_success')} {file_name} !")
        print(f"💡 {t('term_aliases_hint')}")
    except Exception as e:
        print(f"❌ Erreur : {e}")


def install_starship():
    """Installe Starship Prompt."""
    print(f"\n🚀 {t('term_installing_starship')}...")
    if not is_package_installed("starship"):
        subprocess.run(["sudo", "pacman", "-S", "--needed", "starship"], check=False)

    config_file = detect_shell_config()
    with open(config_file, "r") as f:
        content = f.read()

    starship_line = 'eval "$(starship init bash)"' if "bash" in config_file else 'eval "$(starship init zsh)"'

    if starship_line not in content:
        with open(config_file, "a") as f:
            f.write(f"\n# Starship Prompt\n{starship_line}\n")
        print(f"✅ {t('term_starship_activated')} {os.path.basename(config_file)} !")
    else:
        print(f"🎉 {t('term_starship_already_active')}")


def show_terminal_module():
    """Affiche le module Terminal."""
    print("\n" + "=" * 60)
    print(f"      {t('term_title')}")
    print("=" * 60)
    print(f"{t('term_analyzing')}\n")

    has_starship = is_package_installed("starship")
    has_zsh = is_package_installed("zsh")
    has_fastfetch = is_package_installed("fastfetch")

    print(f"📦 {t('term_tools_status')} :")
    print(f"  [✓] {t('term_shell_detected')} : {os.environ.get('SHELL', 'Inconnu')}")
    print(f"  [{'✓' if has_starship else ' '}] Starship Prompt        : {t('term_starship_desc')}")
    print(f"  [{'✓' if has_zsh else ' '}] Shell Zsh              : {t('term_zsh_desc')}")
    print(f"  [{'✓' if has_fastfetch else ' '}] Fastfetch              : {t('term_fastfetch_desc')}")

    print("\n------------------------------------------------------------")
    print(t("term_opt1"))
    print(t("term_opt2"))
    print(t("term_opt3"))
    print(t("term_opt4"))
    print(t("term_opt0"))
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        inject_aliases()
    elif choice == "2":
        install_starship()
    elif choice == "3":
        subprocess.run(["sudo", "pacman", "-S", "--needed", "zsh"], check=False)
    elif choice == "4":
        subprocess.run(["sudo", "pacman", "-S", "--needed", "fastfetch"], check=False)

    input(f"\n{t('press_enter')}")