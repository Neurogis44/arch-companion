import shutil
import subprocess
from services.i18n import t


def show_aur_module():
    """Affiche le module bilingue pour l'installation des assistants AUR (yay / pamac)."""
    print("\n" + "=" * 60)
    print(f"      {t('aur_title')}")
    print("=" * 60)
    print(f"{t('aur_intro_1')}")
    print(f"{t('aur_intro_2')}\n")

    print(f"💡 {t('aur_wiki_reminder')}")
    print(f"  • {t('aur_wiki_point1')}")
    print(f"  • {t('aur_wiki_point2')}")
    print(f"  • {t('aur_wiki_point3')}")
    print("📖 Arch Wiki AUR : https://wiki.archlinux.org/title/Arch_User_Repository\n")

    print(f"--- {t('aur_choice_header')} ---")
    print(f"1. ⚡ yay       ({t('aur_opt_yay')})")
    print(f"2. 🎨 pamac-aur ({t('aur_opt_pamac')})")
    print(f"3. 🛠️ {t('aur_opt_both')}")
    print(f"0. ↩️ {t('aur_opt_back')}")
    print()

    choice = input(t("choice")).strip()

    if choice in ["1", "2", "3"]:
        print(f"\n🔧 {t('aur_step1')}")
        subprocess.run(["sudo", "pacman", "-S", "--needed", "base-devel", "git"], check=False)

        if choice in ["1", "3"]:
            print("\n--------------------------------------------------")
            print(f"📦 {t('aur_installing_yay')}")
            print("Commande : git clone + makepkg -si")
            print("--------------------------------------------------")
            input(f"{t('aur_press_yay')}...")
            cmd = "cd /tmp && rm -rf yay-bin && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si --noconfirm"
            subprocess.run(cmd, shell=True, check=False)

        if choice in ["2", "3"]:
            print("\n--------------------------------------------------")
            print(f"📦 {t('aur_installing_pamac')}")
            print(f"Note : {t('aur_pamac_note')}")
            print("--------------------------------------------------")
            if not shutil.which("yay"):
                print(f"⚠️ {t('aur_yay_needed_for_pamac')}")
                cmd_yay = "cd /tmp && rm -rf yay-bin && git clone https://aur.archlinux.org/yay-bin.git && cd yay-bin && makepkg -si --noconfirm"
                subprocess.run(cmd_yay, shell=True, check=False)

            input(f"{t('aur_press_pamac')}...")
            subprocess.run(["yay", "-S", "--needed", "pamac-aur"], check=False)

        print(f"\n✅ {t('aur_done')}")
    else:
        print(f"\n❌ {t('aur_cancel')}")

    input(f"\n{t('press_enter')}")