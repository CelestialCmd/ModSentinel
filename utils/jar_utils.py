import os
import subprocess
import zipfile
import platform      # ← add

def decompile_classes(input_jar):
    output_dir = os.path.join(os.path.dirname(input_jar), "decompiled")
    os.makedirs(output_dir, exist_ok=True)

    # ── Pick the right launcher for the current OS ────────────────────────────
    if platform.system() == "Windows":
        # e.g. modsentinel\jadx\bin\jadx.bat
        jadx_bin = os.path.abspath(r"jadx\bin\jadx.bat")
    else:
        # Linux / macOS
        jadx_bin = os.path.abspath("jadx/bin/jadx")
    # ─────────────────────────────────────────────────────────────────────────

    command = [jadx_bin, "-d", output_dir, input_jar]
    print(f"[~] Running: {' '.join(command)}")
    subprocess.run(command, check=True)

    return output_dir

def extract_jar(jar_path, out_dir):
    with zipfile.ZipFile(jar_path, "r") as jar:
        jar.extractall(out_dir)
    return out_dir
