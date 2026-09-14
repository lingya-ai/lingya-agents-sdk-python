"""SSE framing utilities."""

from collections.abc import Iterable, Iterator


def decode_sse_lines(lines: Iterable[str]) -> Iterator[str]:
    """合并多行 data 并忽略心跳注释。 / Join multiline data fields and ignore heartbeat comments."""
    data: list[str] = []
    for line in lines:
        if line == "":
            if data:
                yield "\n".join(data)
                data.clear()
        elif line.startswith("data:"):
            data.append(line[5:].removeprefix(" "))
    if data:
        yield "\n".join(data)
