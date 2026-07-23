import shutil
import subprocess
from services.system import is_package_installed

DEV_EDITORS = {
    "visual-studio-code-bin": "VS Code (Version officielle Microsoft via AUR)",
    "vscodium": "VSCodium (Version 100% open-source sans télémétrie)",
}

DEV_LANGUAGES = {
    "python": "Langage Python 3 & environnement de base",
    "go": "Langage Go (Golang) & outils de compilation",
    "nodejs": "Environnement JavaScript Node.js & npm",
}

DEV_TOOLS = {
    "git": "Gestionnaire de version Git",
    "docker": "Moteur de conteneurisation Docker",
    "docker-compose": "Gestion d'applications multi-conteneurs Docker",
    "postman-bin": "Outil de test d'API REST (AUR)",
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


def show_dev_module():
    """Affiche le module Outils Développeur."""
    print("\n" + "=" * 60)
    print("      👨‍💻 PACK DÉVELOPPEUR & OUTILS DE CODE")
    print("=" * 60)
    print("Analyse de ton environnement de développement...\n")

    print("📦 ÉTAT DES OUTILS DE DEV :")
    print("--- Éditeurs & IDE ---")
    for pkg, desc in DEV_EDITORS.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<24} : {desc}")

    print("\n--- Langages & Runtimes ---")
    for pkg, desc in DEV_LANGUAGES.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<24} : {desc}")

    print("\n--- Outils & Conteneurs ---")
    for pkg, desc in DEV_TOOLS.items():
        status = "[✓] Déjà installé" if is_package_installed(pkg) else "[ ] Manquant"
        print(f"  {status} {pkg:<24} : {desc}")

    print("\n------------------------------------------------------------")
    print("1. 📝 Éditeurs de code (VS Code / VSCodium)")
    print("2. ⚡ Langages (Python, Go, Node.js)")
    print("3. 📦 Outils & Conteneurs (Git, Docker, Postman)")
    print("0. ↩️ Retour au menu principal")
    print("------------------------------------------------------------")

    choice = input("👉 Ton choix : ").strip()

    if choice == "1":
        print("\n--- SÉLECTION ÉDITEURS ---")
        for pkg, desc in DEV_EDITORS.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                use_aur = "bin" in pkg
                install_packages([pkg], use_aur=use_aur)

    elif choice == "2":
        selected = []
        print("\n--- SÉLECTION LANGAGES ---")
        for pkg, desc in DEV_LANGUAGES.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                selected.append(pkg)
        if selected:
            install_packages(selected, use_aur=False)

    elif choice == "3":
        print("\n--- SÉLECTION OUTILS & CONTENEURS ---")
        for pkg, desc in DEV_TOOLS.items():
            status = "✓ Déjà installé" if is_package_installed(pkg) else "Manquant"
            c = input(f" ❓ Installer {pkg} ({desc}) [{status}] ? (o/N) : ").strip().lower()
            if c == "o":
                use_aur = "bin" in pkg
                install_packages([pkg], use_aur=use_aur)

    input("\nAppuie sur Entrée pour continuer...")