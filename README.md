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

# fast run with all rules
python scanner.py path/to/mod.jar 
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

## Troubleshooting

* `JadxCLI not found` → use launcher (`jadx` / `jadx.bat`) and ensure Java installed.
* `WinError 193` → wrong binary for Windows; use `jadx.bat`.
* `semgrep not found` → install, use WSL/Docker, or `--engine opengrep`.

## License

MIT © 2025 Liam Troper
