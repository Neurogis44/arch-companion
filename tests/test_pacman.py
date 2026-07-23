from services.pacman import PacmanService


print("Pacman available :", PacmanService.is_available())
print("Steam installed  :", PacmanService.is_installed("steam"))
print("Git installed    :", PacmanService.is_installed("git"))