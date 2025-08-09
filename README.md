# ModSentinel

Decompile & scan Java mod **.jar** files (Minecraft/Fabric/Forge). Uses **JADX** to decompile and **Semgrep/OpenGrep** to flag risky code. Research/defense only.

## Requirements

* Python 3.10+
* Java/JRE
* **JADX** on PATH (or provide `--jadx`)
* **Semgrep** (preferred) or **OpenGrep** (Windows fallback)

## Quick Start

```bash
# (optional venv)
python -m venv .venv && . .venv/bin/activate   # Windows: .\.venv\Scripts\activate

# run
python scanner.py path/to/mod.jar --rules rules/default-java-rules.yml
# if JADX not on PATH:
python scanner.py path/to/mod.jar --jadx bin/jadx/bin/jadx
# Windows OpenGrep:
python scanner.py path\to\mod.jar --engine opengrep
```

## Options

```
scanner.py JAR [--rules FILE|DIR] [--engine semgrep|opengrep] [--jadx PATH]
```

## Layout

```
modsentinel/
  scanner.py
  rules/
  utils/
  mod/   (optional sample jars)
  bin/   (optional local tools, e.g., jadx/)
```

## Including `mod/` and `bin/` in Git (pick one)

**A) Recommended – Git LFS**

```bash
git lfs install
git lfs track "mod/*.jar" "bin/jadx/**"
git add .gitattributes mod/*.jar bin/jadx/**
git commit -m "Add sample mod + tools via LFS"
```

**B) Small demo only – force add (not ideal)**

```bash
git add -f mod/demo.jar bin/jadx/bin/jadx.bat
git commit -m "Force-add small demo files"
```

**C) Don’t commit binaries**

* Add `bin/README.md` with download links
* Attach tools/jars to GitHub Releases

## Troubleshooting

* `JadxCLI not found` → use launcher (`jadx` / `jadx.bat`) and ensure Java installed.
* `WinError 193` → wrong binary for Windows; use `jadx.bat`.
* `semgrep not found` → install, use WSL/Docker, or `--engine opengrep`.

## License

MIT © 2025 Liam Troper