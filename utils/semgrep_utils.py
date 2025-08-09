import os, subprocess, platform

def run_semgrep(src_dir, rules_path):
    # Use OpenGrep on Windows, fall back to semgrep elsewhere
    if platform.system() == "Windows":
        semgrep_bin = os.path.abspath(r"bin\semgrep.exe")
    else:
        semgrep_bin = "semgrep"          # expects Semgrep on PATH

    command = [semgrep_bin, "--config", rules_path, src_dir]
    print(f"[~] Running: {' '.join(command)}")
    subprocess.run(command, check=True)   # exits non-zero on findings
