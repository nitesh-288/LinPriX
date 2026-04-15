from utils.runner import run

def run_module():
    print("\n=== SYSTEM INFO ===")

    user = run("whoami")
    uid = run("id")

    print("[+] User:", user)
    print("[+] ID:", uid)

    if "uid=0" in uid:
        print("[!!!] Already ROOT")
