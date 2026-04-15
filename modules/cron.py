from utils.runner import run
from utils.printer import yellow, green

def run_module():
    print("\n=== CRON JOBS ===")

    cron_main = run("cat /etc/crontab 2>/dev/null")
    cron_dirs = run("ls -la /etc/cron* 2>/dev/null")

    if cron_main:
        print(yellow("\n[!] /etc/crontab:\n"))
        print(cron_main)

    if cron_dirs:
        print(yellow("\n[!] Cron directories:\n"))
        print(cron_dirs)

    if not cron_main and not cron_dirs:
        print(green("[+] No cron jobs found"))
