import os
import platform
import shutil
import subprocess


def get_desktop_environment() -> str:
    """Détecte l'environnement de bureau actuel."""
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


def get_cpu_info() -> str:
    """Récupère le nom du processeur (CPU)."""
    try:
        with open("/proc/cpuinfo", "r") as f:
            for line in f:
                if "model name" in line:
                    # Nettoie le nom du CPU pour l'affichage
                    return line.split(":")[1].strip()
    except Exception:
        pass
    return "Non détecté"


def get_gpu_info() -> str:
    """Récupère le nom de la carte graphique principale (GPU)."""
    if shutil.which("lspci"):
        try:
            result = subprocess.run(
                ["lspci"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            for line in result.stdout.splitlines():
                if "VGA compatible controller" in line or "3D controller" in line:
                    # Enlève l'adresse PCI au début (ex: '03:00.0 ')
                    gpu_name = line.split(":", 2)[-1].strip()
                    return gpu_name
        except Exception:
            pass
    return "Non détectée"


def get_ram_info() -> str:
    """Récupère la mémoire RAM totale disponible."""
    try:
        with open("/proc/meminfo", "r") as f:
            for line in f:
                if "MemTotal" in line:
                    kb = int(line.split(":")[1].split()[0])
                    gb = round(kb / (1024 * 1024), 1)
                    return f"{gb} Go RAM"
    except Exception:
        pass
    return "Non détectée"


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