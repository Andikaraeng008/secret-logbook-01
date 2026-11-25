import os

LINE = "Day 214: my human finally read my error log, nodded wisely, and pasted it into another chatbot to ask what it means."


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
