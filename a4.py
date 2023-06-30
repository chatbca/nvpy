def calculate_letter_frequency(sentence):
 
    sentence = sentence.lower()

  
    letter_frequency = {}

    
    for char in sentence:
        
        if char.isalpha():
       
            if char in letter_frequency:
                letter_frequency[char] += 1
           
            else:
                letter_frequency[char] = 1


    for letter, frequency in letter_frequency.items():
        print(f"{letter}: {frequency}")


sentence = input("Enter a sentence: ")


calculate_letter_frequency(sentence)
