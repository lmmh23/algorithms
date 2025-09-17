from typing import List

SYLLABLES = ['aya', 'ye', 'woo', 'ma']

def solution(babbling: List[str]) -> int:
    count = 0
    for word in babbling:
        index = 0
        last = ''
        valid = True
        while index < len(word):
            matched = False
            for syllable in SYLLABLES:
                if word.startswith(syllable, index) and syllable != last:
                    index += len(syllable)
                    last = syllable
                    matched = True
                    break
            if not matched:
                valid = False
                break
        if valid and index == len(word):
            count += 1
    return count
