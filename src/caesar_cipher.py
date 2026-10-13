def caesar_cipher(s, shift):
    result = ""
    for ch in s:
        if ch.isalpha():
            base = ord("a") if ch.islower() else ord("A")
            result += chr((ord(ch) - base + shift) % 25 + base)
        else:
            result += ch
    return result
