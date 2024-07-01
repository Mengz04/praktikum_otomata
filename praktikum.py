import re

def is_valid_string(s: str) -> bool:
    # Memeriksa apakah string hanya terdiri dari huruf dan digit
    return bool(re.fullmatch(r'[a-zA-Z0-9]*', s))

class PalindromePDA:
    def __init__(self):
        self.stack = []

    def is_palindrome(self, s: str) -> bool:
        # Menghapus karakter yang bukan huruf atau digit
        filtered_s = ''.join(filter(str.isalnum, s)).lower()

        # Menambahkan setengah dari string ke stack
        mid = len(filtered_s) // 2
        for i in range(mid):
            self.stack.append(filtered_s[i])

        # Lewati karakter tengah jika panjang string ganjil
        if len(filtered_s) % 2 != 0:
            mid += 1

        # Bandingkan sisa string dengan karakter di stack
        for i in range(mid, len(filtered_s)):
            if not self.stack or self.stack.pop() != filtered_s[i]:
                return False

        return True

input_strings = ["radar", "12321", "hello", "A man, a plan, a canal, Panama", "123a321"]
pda = PalindromePDA()

for string in input_strings:
    if is_valid_string(string) == False:
        print(f'"{string}" bukan alphanumerik.')
        continue
    if pda.is_palindrome(string):
        print(f'"{string}" adalah palindrome.')
    else:
        print(f'"{string}" bukan palindrome.')
