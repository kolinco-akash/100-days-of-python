def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in input_string:
        if char in vowels:
            vowel_count = vowel_count + 1

    return vowel_count


str = input("Enter a string: ")
result = count_vowels(str)
print(f"Number of vowels in the given string: {result}")
