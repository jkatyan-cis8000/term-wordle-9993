"""Lint and validation script for term-wordle."""

import ast
import sys
from pathlib import Path


def check_imports(file_path: Path, allowed_imports: set) -> list[str]:
    """Check imports in a file against allowed imports."""
    errors = []
    try:
        with open(file_path) as f:
            tree = ast.parse(f.read())
        
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    if alias.name not in allowed_imports:
                        errors.append(
                            f"{file_path}:{node.lineno}: "
                            f"Import '{alias.name}' not in allowed list"
                        )
            elif isinstance(node, ast.ImportFrom):
                if node.module and node.module not in allowed_imports:
                    errors.append(
                        f"{file_path}:{node.lineno}: "
                        f"Import from '{node.module}' not allowed"
                    )
    except SyntaxError as e:
        errors.append(f"{file_path}:{e.lineno}: Syntax error - {e.msg}")
    
    return errors


def main():
    """Run validation checks."""
    src_dir = Path("src")
    all_errors = []
    
    # Check each layer
    layers = ["types", "config", "repo", "utils", "service", "ui", "runtime"]
    
    for layer in layers:
        layer_dir = src_dir / layer
        if not layer_dir.exists():
            all_errors.append(f"Missing layer directory: {layer}")
            continue
        
        for py_file in layer_dir.glob("*.py"):
            if py_file.name == "__init__.py":
                continue
            
            # Check imports (stdlib only)
            allowed = {"dataclasses", "enum", "random", "datetime", "typing"}
            errors = check_imports(py_file, allowed)
            all_errors.extend(errors)
    
    # Report results
    if all_errors:
        print("Validation failed:")
        for error in all_errors:
            print(f"  {error}")
        return 1
    
    print("All checks passed!")
    return 0


if __name__ == "__main__":
    sys.exit(main())
