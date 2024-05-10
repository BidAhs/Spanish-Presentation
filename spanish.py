import random
import sys
import os

# list of er/ir verbs
verbs = {
    "comer": "to eat",
    "beber": "to drink",
    "vivir": "to live",
    "escribir": "to write",
    "aprender": "to learn",
    "correr": "to run",
    "recibir": "to receive",
    "abrir": "to open",
    "decidir": "to decide",
    "salir": "to go out",
    "pedir": "to ask for",
    "ocurrir": "to occur",
}

# returns random verb from list
def getRandomVerb():
    return random.choice(list(verbs.keys()))

# conjugates verb in preterite form
def conjugate(verb):
    if verb.endswith("er"):
        return {
            "yo": verb[:-2] + "i",
            "tú": verb[:-2] + "iste",
            "él/ella/Ud.": verb[:-2] + "io",
            "nosotros/nosotras": verb[:-2] + "imos",
            "ellos/ellas/Uds.": verb[:-2] + "ieron"
        }
    elif verb.endswith("ir"):
        return {
            "yo": verb[:-2] + "i",
            "tú": verb[:-2] + "iste",
            "él/ella/Ud.": verb[:-2] + "io",
            "nosotros/nosotras": verb[:-2] + "imos",
            "ellos/ellas/Uds.": verb[:-2] + "ieron"
        }
    else:
        return None

# keep question on same line
def print_there(y, x, text):
     sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, text))
     sys.stdout.flush()

# clear line
def clear_line(y, x):
    sys.stdout.write("\x1b7\x1b[%d;%df%s\x1b8" % (y, x, " "*120))
    sys.stdout.flush()

# answer on same line
def input_there(y, x, question, pronoun):
    print_there(y, x, " "*120)  # Clear line
    print_there(y, x, question)
    pronoun_length = len(pronoun)+3
    sys.stdout.write("\x1b[{};{}H".format(y, x + pronoun_length))  # Move cursor to the end of the question
    sys.stdout.flush()
    return input()

# List of colors 
def cyan(text):
    return "\033[36m" + text + "\033[0m"
def red(text):
    return "\033[91m" + text + "\033[0m"
def green(text):
    return "\033[92m" + text + "\033[0m"
def orange(text):
    return "\033[38;5;208m" + text + "\033[0m"
def purple(text):
    return "\033[95m" + text + "\033[0m"
def yellow(text):
    return "\033[93m" + text + "\033[0m"

def Game():

    os.system('cls' if os.name == 'nt' else 'clear')
    
    print(purple(f"""

  _____ ____      _____ ____                 
 | ____|  _ \\    / /_ _|  _ \\                
 |  _| | |_) |  / / | || |_) |               
 | |___|  _ <  / /  | ||  _ <                
 |_____|_| \\_\\/_/_ |___|_| \\_\\_ _            
 |  _ \\ _ __ ___| |_ ___ _ __(_) |_ ___  ___ 
 | |_) | '__/ _ \\ __/ _ \\ '__| | __/ _ \\/ __|
 |  __/| | |  __/ ||  __/ |  | | ||  __/\\__ \\
 |_|   |_|  \\___|\\__\\___|_|  |_|\\__\\___||___/
                                             

"""))

    # Printing directions
    print(cyan("Welcome to the Spanish Preterite Verb Quiz!"))
    print(cyan("You will have five infinitive verbs in Spanish, conjugate them in the preterite tenses."))
    print(cyan("Type 'exit' to quit the game.\n"))

    total = 0
    score = 0

    # Do 5 verbs total
    while total <= 20:

        verbSpanish, verbEnglish = random.choice(list(verbs.items()))

        clear_line(20, 0)
        print_there(20, 0, orange("Conjugate the verb " + purple(verbSpanish) + orange(' (') + purple(verbEnglish)) + orange( ") in the preterite tense: "))

        correctAnswers = conjugate(verbSpanish)

        for pronoun, correctAnswer in correctAnswers.items():
            userInput = input_there(21, 0, yellow(f"{pronoun}: "), pronoun)

            if userInput.lower() == 'exit':
                print(green('\nThanks for playing!'))
                print(red(f"Your score was {score} out of {total}\n"))
                return

            elif userInput.lower() == correctAnswer:
                clear_line(23, 0)
                print_there(23, 0, green('Correct!'))
                score += 1
                total += 1
                print_there(24, 0, purple(f"Current score is {score} out of {total}.\n"))
                
            else:
                clear_line(23, 0)
                print_there(23, 0, red(f"Incorrect. The correct answer is '{correctAnswer}'."))
                total += 1
                print_there(24, 0, purple(f"Current score is {score} out of {total}.\n"))
                

    # see if user passed or not
    if score >= 14:
        clear_line(23, 0)
        clear_line(24, 0)
        print(green(f'\nCongrats you passed with {score} out of {total}\n'))
    else:
        clear_line(23, 0)
        clear_line(24, 0)
        print(red(f'\nUh oh you failed with {score} out of {total}\n'))

# run main game function
if __name__ == '__main__':
    sys.exit(Game())
