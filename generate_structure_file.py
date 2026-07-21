from pathlib import Path

root = Path(".")
output_file = root / "folder_structure.txt"

IGNORE = {
    ".git",
    ".venv",
    "venv",
    "__pycache__",
    ".idea",
    ".vscode",
    ".pytest_cache",
    "node_modules",
}

with output_file.open("w", encoding="utf-8") as f:
    f.write(f"{root.resolve().name}/\n")

    def walk(path, prefix=""):
        items = sorted(
            [p for p in path.iterdir() if p.name not in IGNORE],
            key=lambda p: (p.is_file(), p.name.lower())
        )

        for i, item in enumerate(items):
            connector = "└── " if i == len(items) - 1 else "├── "
            f.write(prefix + connector + item.name)

            if item.is_dir():
                f.write("/\n")
                extension = "    " if i == len(items) - 1 else "│   "
                walk(item, prefix + extension)
            else:
                f.write("\n")

    walk(root)

print(f"Folder structure saved to: {output_file.resolve()}")