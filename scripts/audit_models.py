"""Reject dynamically typed public Pydantic fields in generated models."""

from __future__ import annotations

import ast
from pathlib import Path

FORBIDDEN = {"Any", "Dict", "Mapping", "MutableMapping", "dict"}


def main() -> None:
    violations: list[str] = []
    root = Path(__file__).parents[1] / "lingya_agents_sdk/models"
    for path in sorted(root.glob("*.py")):
        tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
        for node in tree.body:
            if not isinstance(node, ast.ClassDef):
                continue
            for member in node.body:
                if not isinstance(member, ast.AnnAssign) or not isinstance(member.target, ast.Name):
                    continue
                if (
                    member.target.id.startswith("_")
                    or member.target.id == "discriminator_value_class_map"
                    or _is_class_var(member.annotation)
                ):
                    continue
                names = {part.id for part in ast.walk(member.annotation) if isinstance(part, ast.Name)}
                dynamic = sorted(names & FORBIDDEN)
                if dynamic:
                    violations.append(
                        f"{path.name}:{member.lineno} {node.name}.{member.target.id}: {', '.join(dynamic)}"
                    )
    if violations:
        raise SystemExit("Dynamic public model fields found:\n" + "\n".join(violations))
    print("Python public model field audit passed.")


def _is_class_var(annotation: ast.expr) -> bool:
    return (
        isinstance(annotation, ast.Subscript)
        and isinstance(annotation.value, ast.Name)
        and annotation.value.id == "ClassVar"
    )


if __name__ == "__main__":
    main()
