import numpy as np
import pandas as pd

def fun1(string):
    str =  string.lower()
    # Convert the string into a numpy array of characters
    arr = np.array(list(str))

    # Get the length of the array
    length = len(arr)

    # Iterate through the array from start to middle
    for i in range(length // 2):
        # Compare characters from the start and end of the array
        if arr[i] != arr[length - i - 1]:
            return False
    
    return True

def f2(s):
    freq = {}
    for letter in s:
        if letter.isalpha(): 
            if letter in freq:
                freq[letter] += 1
            else:
                freq[letter] = 1

    max_freq = 0
    second_max_freq = 0
    most_freq_letter = ''
    second_most_freq_letter = ''
    
    for letter, freq in freq.items():
        if freq > max_freq:
            second_max_freq = max_freq
            second_most_freq_letter = most_freq_letter
            
            max_freq = freq
            most_freq_letter = letter
        elif freq > second_max_freq and freq != max_freq:
            second_max_freq = freq
            second_most_freq_letter = letter
    
    return second_most_freq_letter






def fun3(string):
    # Create a Series from the string
    series = pd.Series(list(string))
    
    # Count the occurrences of upper-case letters, lower-case letters, and digits
    upper_count = series.str.isupper().sum()
    lower_count = series.str.islower().sum()
    digit_count = series.str.isdigit().sum()

    return (upper_count, lower_count, digit_count)

