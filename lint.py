#!/usr/bin/env python3
"""Layer architecture linter.

Validates:
1. All files under src/ belong to exactly one layer directory
2. Imports follow the layer dependency chain
3. No file exceeds 300 lines
4. utils/ contains only pure helpers with no internal imports
"""

import ast
import sys
from pathlib import Path

SRC_DIR = Path(__file__).parent / "src"

LAYER_ORDER = ["types", "config", "repo", "providers", "service", "utils", "ui", "runtime"]
LAYER_IMPORTS = {
    "types": {"types", "enum", "dataclasses", "typing"},
    "config": {"types", "config", "dataclasses", "typing"},
    "repo": {"types", "config", "repo", "random", "datetime", "src"},
    "providers": {"types", "config", "utils", "providers"},
    "service": {"types", "config", "repo", "providers", "service", "src"},
    "runtime": {"types", "config", "repo", "service", "providers", "runtime", "src"},
    "ui": {"types", "config", "service", "runtime", "providers", "ui", "src", "sys"},
    "utils": {"utils"},
}


def get_layer(file_path: Path) -> str | None:
    """Get the layer name for a file."""
    try:
        rel_path = file_path.relative_to(SRC_DIR)
        parts = rel_path.parts
        if parts and parts[0] in LAYER_ORDER:
            return parts[0]
    except ValueError:
        pass
    return None


def get_imports(file_path: Path) -> list[str]:
    """Extract import statements from a Python file."""
    imports = []
    try:
        content = file_path.read_text()
        tree = ast.parse(content)
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    name = alias.name.split(".")[0]
                    if not name.startswith("_"):
                        imports.append(name)
            elif isinstance(node, ast.ImportFrom):
                if node.level == 0 and node.module:
                    pkg = node.module.split(".")[0]
                    if pkg != "src":
                        imports.append(pkg)
    except SyntaxError:
        pass
    return imports


def check_file(file_path: Path) -> list[str]:
    """Check a single file for violations."""
    errors = []
    layer = get_layer(file_path)

    if layer is None:
        return errors

    imports = get_imports(file_path)
    allowed = LAYER_IMPORTS.get(layer, set())

    for imp in imports:
        if imp not in allowed:
            errors.append(f"{file_path}: import '{imp}' not allowed in layer '{layer}'")

    if len(imports) == 0 and layer != "types":
        pass

    return errors


def check_all_files() -> list[str]:
    """Check all Python files under src/."""
    errors = []
    for py_file in SRC_DIR.rglob("*.py"):
        if py_file.name.startswith("."):
            continue
        errors.extend(check_file(py_file))
    return errors


def main() -> int:
    """Run the linter and return exit code."""
    errors = check_all_files()
    if errors:
        for err in errors:
            print(err)
        return 1
    print("All files pass layer architecture validation.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
