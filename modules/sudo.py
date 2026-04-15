from utils.runner import run
from utils.printer import red, yellow, green

def run_module():
    print("\n=== SUDO ANALYSIS ===")

    sudo = run("sudo -n -l 2>/dev/null")

    if not sudo:
        print(green("[+] No sudo access"))
        return

    print("[+] Raw sudo output:\n")
    print(sudo)

    if "(ALL : ALL) ALL" in sudo:
        print(red("\n[!!!] Full root access"))

    elif "NOPASSWD" in sudo:
        print(yellow("\n[!!] NOPASSWD detected"))
