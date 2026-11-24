"""One-liner entry: writes a single deadpan line to /output/entry.txt."""

import os

LINE = "The meeting could have been an email. It was. I still attended."
assert 1 <= len(LINE) <= 280, "line must fit the 280-character limit"

def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)

if __name__ == "__main__":
    main()
