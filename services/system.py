import os
import platform
import shutil
import subprocess


def get_desktop_environment() -> str:
    """Détecte l'environnement de bureau actuel (KDE, GNOME, XFCE, etc.)."""
    desktop = os.environ.get("XDG_CURRENT_DESKTOP")
    if desktop:
        return desktop.upper()

    desktop_session = os.environ.get("DESKTOP_SESSION")
    if desktop_session:
        return desktop_session.upper()

    return "TTY / Non détecté"


def get_kernel_version() -> str:
    """Récupère la version exacte du noyau Linux."""
    return platform.release()


def get_installed_packages_count() -> str:
    """Compte le nombre de paquets installés via pacman."""
    if shutil.which("pacman"):
        try:
            result = subprocess.run(
                ["pacman", "-Q"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            if result.returncode == 0:
                count = len(result.stdout.strip().splitlines())
                return f"{count} paquets (pacman)"
        except Exception:
            pass
    return "Indisponible"