def non_repeate_char(str):
    freq = {}
    for ch in str:
        freq[ch] = freq.get(ch,0)+1
    for ch in str:
        if freq[ch] == 1:
            return ch
    return str

print(non_repeate_char("swiss"))
