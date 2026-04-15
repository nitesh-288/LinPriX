from utils.runner import run
from utils.printer import yellow, green

def run_module():
    print("\n=== SUID BINARIES ===")

    suid = run("find / -perm -4000 -type f 2>/dev/null")

    if suid:
        print(yellow("[!] SUID binaries (top 10):\n"))
        for line in suid.split("\n")[:10]:
            print(line)

        print("\n[!] Check binaries on: https://gtfobins.github.io/")
    else:
        print(green("[+] No SUID binaries found"))
