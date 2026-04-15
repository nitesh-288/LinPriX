from utils.runner import run
from utils.printer import yellow, green

def run_module():
    print("\n=== WRITABLE FILES ===")

    writable = run(
        "find / -writable -type f 2>/dev/null "
        "| grep -v '/proc' | grep -v '/sys' "
        "| head -n 10"
    )

    if writable:
        print(yellow("[!] Interesting writable files:\n"))
        print(writable)
    else:
        print(green("[+] No useful writable files"))
