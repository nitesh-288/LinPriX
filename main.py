import sys
from modules import system, sudo, groups, suid, cron, files, path

def main():
    print("=== Linux Privilege Escalation Analyzer ===")

    if len(sys.argv) == 1:
        system.run_module()
        sudo.run_module()
        groups.run_module()
        suid.run_module()
        cron.run_module()
        files.run_module()
        path.run_module()

    elif sys.argv[1] == "--sudo":
        sudo.run_module()

    elif sys.argv[1] == "--groups":
        groups.run_module()

    elif sys.argv[1] == "--suid":
        suid.run_module()

    elif sys.argv[1] == "--cron":
        cron.run_module()

    elif sys.argv[1] == "--files":
        files.run_module()

    elif sys.argv[1] == "--path":
        path.run_module()

    elif sys.argv[1] == "--full":
        system.run_module()
        sudo.run_module()
        groups.run_module()
        suid.run_module()
        cron.run_module()
        files.run_module()
        path.run_module()

    else:
        print("Invalid option")

if __name__ == "__main__":
    main()
