import os

# Logbook entry, Day 143: the agent taught the toaster to keep secrets,
# but the whole kitchen knows it ate the last cookie. Line length:
# 163 characters.
LINE = "Day 143: I taught the toaster to keep secrets, but the whole kitchen knows I ate the last cookie."


def main():
    # The grader mounts the repo read-only, so the entry must go to
    # MAKEFUN_OUTPUT_DIR (default /output), never into the repo itself.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
