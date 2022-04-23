import random

small_letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','o','p','q','s','t','u','v','w','x','y','z']
large_letters = ['A','B','C','D','E','F','G','H','I', 'J','K','L','M','N','O','P','Q', 'S','T','U','V','W','X','Y','Z']


generated_password = [] 

while len(generated_password) < 15:         #filling password array while symbols are less than 15 characters
    for i in range(5):
        random.shuffle(small_letters)
        random.shuffle(large_letters)

        random_small_letter = random.choice(small_letters)
        small_letters.remove(random_small_letter)

        random_large_letter = random.choice(large_letters)
        large_letters.remove(random_large_letter)

        random_number = random.randint(0, 9)

        generated_password.append(random_small_letter)
        generated_password.append(random_large_letter)
        generated_password.append(random_number) 

random.shuffle(generated_password)         # shuffling the password array

password = (''.join(map(str, generated_password)))         # getting sorted password
print("\n", password, "\n")



'''
    len_small_letters = len(small_letters)         # counting small letters
    len_large_letters = len(large_letters)        # counting large letters

    rnd_small_letter_id = random.randint(0, len_small_letters)         # getting random small letter's id
    rnd_large_letter_id = random.randint(0, len_large_letters)         # getting random large letter's id

    random_small_letter = small_letters.pop(rnd_small_letter_id)        # geting one random small letter
    random_large_letter = large_letters.pop(rnd_large_letter_id)       # geting one random large letter
    random_number = random.randint(0, 9)                    # geting one random number from 0 to 9
    generated_password.append(random_number)      # adding random number into a password array
    generated_password.append(random_small_letter)     # adding random small letter into a password array
    generated_password.append(random_large_letter)     # adding random large letter into a password array
'''
