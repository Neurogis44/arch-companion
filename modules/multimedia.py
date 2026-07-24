import shutil
import subprocess
from services.i18n import t
from services.system import is_package_installed


def get_multimedia_dicts():
    """Retourne les dictionnaires multimédia traduits dynamiquement."""
    
    # Paquets officiels (Codecs, Frameworks & Lecteurs / Outils principaux)
    official = {
        # Codecs & Frameworks Vidéo / Audio essentiels
        "ffmpeg": t("multi_desc_ffmpeg"),
        "gst-plugins-base": t("multi_desc_gst_base"),
        "gst-plugins-good": t("multi_desc_gst_good"),
        "gst-plugins-bad": t("multi_desc_gst_bad"),
        "gst-plugins-ugly": t("multi_desc_gst_ugly"),
        "gst-libav": t("multi_desc_gst_libav"),
        "libdvdcss": t("multi_desc_dvdcss"),
        
        # Lecteurs Vidéo & Audio populaires
        "vlc": t("multi_desc_vlc"),
        "mpv": t("multi_desc_mpv"),
        "rhythmbox": t("multi_desc_rhythmbox"),
        
        # Outils de création & Édition (Capture, Montage, Transcodage)
        "obs-studio": t("multi_desc_obs"),
        "handbrake": t("multi_desc_handbrake"),
        "audacity": t("multi_desc_audacity"),
        "kdenlive": t("multi_desc_kdenlive"),
    }
    
    # Paquets populaires (principalement sur AUR ou spécifiques)
    popular = {
        "spotify-launcher": t("multi_desc_spotify"),
        "stremio": t("multi_desc_stremio"),
        "cider": t("multi_desc_cider"),  # Lecteur Apple Music très prisé
    }
    
    return official, popular


def install_packages(packages: list, use_aur: bool = False):
    """Exécute pacman ou yay selon la provenance des paquets."""
    if not packages:
        print(f"\n⚠️ {t('multi_no_pkg_selected')}")
        return

    if use_aur:
        if shutil.which("yay"):
            print(f"\n🚀 {t('multi_launching_yay')} : {' '.join(packages)}\n")
            subprocess.run(["yay", "-S", "--needed"] + packages, check=False)
        else:
            print(f"\n❌ {t('multi_yay_not_installed')}")
            print(f"👉 {t('multi_yay_hint')}")
    else:
        print(f"\n🚀 {t('multi_launching_pacman')} : {' '.join(packages)}\n")
        subprocess.run(["sudo", "pacman", "-S", "--needed"] + packages, check=False)


def show_multimedia_module():
    """Affiche le module Multimédia bilingue enrichi."""
    multi_official, multi_popular = get_multimedia_dicts()

    print("\n" + "=" * 60)
    print(f"      {t('multi_title')}")
    print("=" * 60)
    print(f"{t('multi_analyzing')}\n")

    print(f"📦 {t('multi_status_header')} :")
    print(f"\n--- {t('multi_section_official')} ---")
    for pkg, desc in multi_official.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<22} : {desc}")

    print(f"\n--- {t('multi_section_popular')} ---")
    for pkg, desc in multi_popular.items():
        status = f"[✓] {t('installed')}" if is_package_installed(pkg) else f"[ ] {t('missing')}"
        print(f"  {status} {pkg:<22} : {desc}")

    print("\n------------------------------------------------------------")
    print(t("multi_opt1"))  # ex: "1. Installer tous les codecs & paquets officiels manquants"
    print(t("multi_opt2"))  # ex: "2. Sélectionner les paquets à installer au cas par cas"
    print(t("multi_opt3"))  # ex: "3. Installer les applications populaires (Spotify, Stremio... via AUR)"
    print(t("multi_opt0"))  # ex: "0. Retour"
    print("------------------------------------------------------------")

    choice = input(t("choice")).strip()

    if choice == "1":
        missing = [pkg for pkg in multi_official if not is_package_installed(pkg)]
        if missing:
            install_packages(missing, use_aur=False)
        else:
            print(f"\n🎉 {t('multi_all_official_installed')}")

    elif choice == "2":
        selected_off = []
        # Choix dans les paquets officiels
        print(f"\n--- {t('multi_section_official')} ---")
        for pkg, desc in multi_official.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('multi_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                selected_off.append(pkg)
        
        if selected_off:
            install_packages(selected_off, use_aur=False)

        # Choix dans les paquets populaires (AUR)
        selected_pop = []
        print(f"\n--- {t('multi_section_popular')} ---")
        for pkg, desc in multi_popular.items():
            status = t("installed") if is_package_installed(pkg) else t("missing")
            c = input(f" ❓ {t('multi_ask_install')} {pkg} ({desc}) [{status}] ? (o/N / y/N) : ").strip().lower()
            if c in ["o", "y"]:
                selected_pop.append(pkg)

        if selected_pop:
            install_packages(selected_pop, use_aur=True)

    elif choice == "3":
        missing_pop = [pkg for pkg in multi_popular if not is_package_installed(pkg)]
        if missing_pop:
            install_packages(missing_pop, use_aur=True)
        else:
            print(f"\n🎉 {t('multi_all_popular_installed')}")

    input(f"\n{t('press_enter')}")