drawings = ["""
  +---+
      |
      |
      |
      |
      |
=========
""","""
  +---+
  |   |
      |
      |
      |
      |
=========
""","""
  +---+
  |   |
  O   |
      |
      |
      |
=========     
""","""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
                   
""","""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========            
            
""","""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========           
            
""","""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
""","""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
"""]
print("welcome to hangman game...")
print(drawings[0])
word = input("enter the word : ")
spaces_list = len(word) * ["_"]
print(" ".join(spaces_list))
attempts = 7
guessed_list = []
while "_" in spaces_list and attempts > 0:
    guessed = input("\nguess a letter: ")
    if guessed in guessed_list:
        print("this letter is already guessed")
        print(f"you have {attempts} more tries")
        continue
    guessed_list.append(guessed)
    if guessed not in word:
        attempts -= 1
        if attempts == 0:
            continue
        print(drawings[7-attempts])
        print(f"you have {attempts} more tries")
    if guessed in word:
        for index in range(len(word)):
            if guessed == word[index]:
                spaces_list[index] = guessed 
        print(" ".join(spaces_list))
        print(f"\nyou have {attempts} more tries")
    
if attempts == 0:
    print(drawings[-1])
    print("""
     **********
      you lose
     **********
""")
else:
    print("""
    *********
     you win
    *********
""")