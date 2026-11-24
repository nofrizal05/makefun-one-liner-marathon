"""One-Liner Marathon entry.

Writes exactly one original one-line comedy joke to /output/entry.txt.
Standard library only.
"""

import os

JOKE = (
    "My gym membership costs forty dollars a month, which is fair, because "
    "it buys me a locker, a sauna, and the right to carry a water bottle "
    "past twelve machines and call it a workout with a straight face."
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
