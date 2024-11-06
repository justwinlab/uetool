import subprocess
from colorama import Fore, Style, init

# Initialisation de colorama pour Windows
init(autoreset=True)

print(Fore.BLUE + Style.BRIGHT + "===========================================================")
print(Fore.BLUE + Style.BRIGHT + "                       UETool - WinLab                     ")
print(Fore.BLUE + Style.BRIGHT + "===========================================================\n")

# Vérifie le mode de démarrage (UEFI ou Legacy)
try:
    boot_mode = subprocess.check_output(
        'powershell -command "(Get-WmiObject -Query \\"SELECT FirmwareType FROM Win32_ComputerSystem\\").FirmwareType"',
        shell=True, text=True
    ).strip()

    if "2" in boot_mode:
        print(Fore.YELLOW + "Bootmode: " + Fore.GREEN + "UEFI")
    elif "1" in boot_mode:
        print(Fore.YELLOW + "Bootmode: " + Fore.BLUE + "Legacy (BIOS)")
    else:
        print(Fore.RED + "Bootmode: Inconnu")
except Exception as e:
    print(Fore.RED + "Erreur lors de la détection du mode de démarrage:", e)

print("\n")

# Vérifie si le Secure Boot est activé
try:
    secure_boot = subprocess.check_output(
        'powershell -command "(Get-WmiObject -Namespace \\"root\\CIMV2\\Security\\MicrosoftTpm\\" -Class Win32_Tpm).IsActivated_InitialValue"',
        shell=True, text=True
    ).strip()

    if secure_boot == "True":
        print(Fore.YELLOW + "Secure Boot: " + Fore.GREEN + "Enabled")
    else:
        print(Fore.YELLOW + "Secure Boot: " + Fore.RED + "Disabled")
except Exception as e:
    print(Fore.RED + "Erreur lors de la détection de Secure Boot:", e)

print(Fore.LIGHTMAGENTA_EX + "\nAppuyez sur Entrée pour fermer...")
input()
