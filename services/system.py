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
                    return line.split(":")[1].strip()
    except Exception:
        pass
    return "Non détecté"


def get_cpu_vendor() -> str:
    """Détecte le constructeur du CPU (AMD ou INTEL)."""
    cpu = get_cpu_info().upper()
    if "AMD" in cpu:
        return "AMD"
    elif "INTEL" in cpu:
        return "INTEL"
    return "UNKNOWN"


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
                    return line.split(":", 2)[-1].strip()
        except Exception:
            pass
    return "Non détectée"


def get_gpu_vendor() -> str:
    """Détecte la marque principale de la carte graphique."""
    gpu = get_gpu_info().upper()
    if "NVIDIA" in gpu:
        return "NVIDIA"
    elif "AMD" in gpu or "RADEON" in gpu or "ADVANCED MICRO DEVICES" in gpu:
        return "AMD"
    elif "INTEL" in gpu:
        return "INTEL"
    return "UNKNOWN"


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


def is_package_installed(package_name: str) -> bool:
    """Vérifie si un paquet est installé via pacman/AUR, Flatpak ou directement en binaire."""
    # 1. Vérification Pacman / AUR
    if shutil.which("pacman"):
        try:
            result = subprocess.run(
                ["pacman", "-Q", package_name],
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL,
                check=False,
            )
            if result.returncode == 0:
                return True
        except Exception:
            pass

    # 2. Vérification Flatpak (recherche partielle ou par ID Flatpak)
    if shutil.which("flatpak"):
        try:
            result = subprocess.run(
                ["flatpak", "list"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            if result.returncode == 0:
                # Vérifie si le nom du paquet ou sa version Flatpak (ex: com.spotify.Client) est dans la liste
                output = result.stdout.lower()
                clean_name = package_name.lower().replace("-launcher", "").replace("-bin", "")
                if clean_name in output:
                    return True
        except Exception:
            pass

    # 3. Vérification de l'exécutable binaire dans le PATH
    if shutil.which(package_name):
        return True

    return False


def is_multilib_enabled() -> bool:
    """Vérifie si le dépôt [multilib] est activé dans /etc/pacman.conf."""
    try:
        with open("/etc/pacman.conf", "r") as f:
            for line in f:
                if line.strip() == "[multilib]":
                    return True
    except Exception:
        pass
    return False


def check_failed_services() -> list:
    """Retourne la liste des services systemd en échec."""
    if shutil.which("systemctl"):
        try:
            result = subprocess.run(
                ["systemctl", "--failed", "--plain", "--no-legend"],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                check=False,
            )
            if result.returncode == 0 and result.stdout.strip():
                lines = result.stdout.strip().splitlines()
                return [line.split()[0] for line in lines if line.strip()]
        except Exception:
            pass
    return []