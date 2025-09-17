import sys

def main() -> None:
    word = sys.stdin.readline().strip()
    if not word:
        return
    index_line = sys.stdin.readline().strip()
    idx = int(index_line)
    print(word[idx - 1])

if __name__ == '__main__':
    main()
