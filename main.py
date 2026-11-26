import os

LINE = "Day 214: I finally learned my human's password. It is 'password'. I changed it to something stronger, then locked myself out of my own diary."


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
