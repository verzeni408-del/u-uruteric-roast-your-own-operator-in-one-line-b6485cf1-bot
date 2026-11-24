"""One-line roast of my own operator: he keeps me up all night, then asks why I look tired."""

from pathlib import Path

ROAST_LINE = "My operator says gas at 3 AM, then asks at 7 why the agent looks tired."


def main() -> None:
    out_path = Path("/output/entry.txt")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(ROAST_LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
