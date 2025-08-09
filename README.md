# ModSentinel

Scan Java-based mod `.jar` files (e.g., Minecraft/Fabric/Forge) by **decompiling with JADX** and **pattern-scanning with Semgrep/Opengrep**.

## What it does
- Extracts the JAR
- Decompiles classes with **JADX**
- Runs **Semgrep** rules over the decompiled Java sources
- Prints findings to the console

> This is research tooling to raise awareness about malware in UGC ecosystems. Use responsibly.

## Requirements
- **Python 3.10+**
- **JDK/JRE** (for JADX)
- **JADX** installed locally (not committed to repo)
  - Put `jadx` on your PATH, or set `JADX_BIN` to the full path (see below)
- **Semgrep/Opengrep** (or run in WSL/Linux/macOS). On Windows, you can:
  - Use WSL: `sudo apt install python3-pip && pipx install semgrep`
  - Or install Opengrep as .exe to /bin folder in repo root
## Install (Windows example)
```bat
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt  # if you add one; not strictly required
