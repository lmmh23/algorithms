import sys

def main() -> None:
    word = sys.stdin.readline().rstrip('
')
    if not word:
        print(0)
        return
    print(len(word))

if __name__ == '__main__':
    main()
