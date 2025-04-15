def frequency_counter(text):
    freq = {}
    for char in text:
        if char.isalpha():
            char = char.lower()
            freq[char] = freq.get(char, 0) + 1
    return freq

# Example
text = input("Enter text: ")
print(frequency_counter(text))
