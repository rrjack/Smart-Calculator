import sys
sys.path.append('/mymodules/')
import mymodules
from mymodules.mathy import *

print(responses[0])
print(responses[1])

while True:      # it is a infinite loop, it will continue until user stops it by applying break or exit or by any means
    print()
    text = input('now what you want me to do?')
    for word in text.split(' '):
        if word.upper() in operations2.keys():
            try:
                l = extract_numbers_from_text(text)
                r = operations2[word.upper()](l[0],l[1])    # (l[0],l[1]) means function is being called
                print(r)
            except:
                print("Something wrong, please try again")
            finally:
                break

        elif word.upper() in operations1.keys():
            try:
                l = extract_numbers_from_text(text)
                r = operations1[word.upper()](l[0])
                print(r)
            except:
                print("Something wrong, please try again")
            finally:
                break

        elif word.upper() in operations3.keys():
            try:
                l = extract_numbers_from_text(text)
                r = operations3[word.upper()](l[0],l[1],l[2])
                print(r)
            except:
                print("Something wrong, please try again")
            finally:
                break

        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
