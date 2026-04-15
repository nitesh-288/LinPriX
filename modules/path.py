from utils.runner import run
from utils.printer import red, green

def run_module():
    print("\n=== PATH ANALYSIS ===")

    path = run("echo $PATH")

    print("[+] PATH:", path)

    if "." in path:
        print(red("[!!!] PATH contains '.' → vulnerable"))
    else:
        print(green("[+] PATH looks safe"))
