from utils.runner import run
from utils.printer import red, yellow, green

def run_module():
    print("\n=== GROUP ANALYSIS ===")

    groups = run("groups")
    print("[+] Groups:", groups)

    if "docker" in groups:
        print(red("[!!!] Docker group → root possible"))
        print("→ docker run -v /:/mnt --rm -it alpine chroot /mnt sh")

    if "sudo" in groups:
        print(yellow("[!!] User in sudo group"))

    if "adm" in groups:
        print(yellow("[!] adm group → can read logs"))

    if not any(g in groups for g in ["docker", "sudo", "adm"]):
        print(green("[+] No dangerous groups"))
