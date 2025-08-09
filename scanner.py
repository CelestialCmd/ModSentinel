import argparse
import tempfile
import shutil
import os
from utils.jar_utils import extract_jar, decompile_classes
from utils.semgrep_utils import run_semgrep

def main(jar_path, rules_path):
    with tempfile.TemporaryDirectory() as work_dir:
        print(f"[+] Extracting {jar_path}...")
        class_dir = extract_jar(jar_path, work_dir)

        print(f"[+] Decompiling .class files...")
        java_src_dir = decompile_classes(class_dir)

        print(f"[+] Running Semgrep...")
        run_semgrep(java_src_dir, rules_path)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="ModScanner - Decompile and scan Minecraft/Fabric mods for malware.")
    parser.add_argument("jar", help="Path to the .jar mod file")
    parser.add_argument("--rules", default="rules/default-java-rules.yml", help="Path to Semgrep rule file")

    args = parser.parse_args()
    main(args.jar, args.rules)