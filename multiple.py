import sys
import json
import random
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("quizfile", help="quiz file to run",
                    type=str)
    args = parser.parse_args()

    f = open(args.quizfile, "r")
    qs = json.loads(f.read())
    f.close()

    random.shuffle(qs)
    num_right = 0
    num_asked = 0
    for q in qs:
        num_asked += 1
        statement = q["statement"]
        print statement
        answer = q["answer"]
        fakes = q["fakes"]
        
        choices = q["fakes"][0:3]
        choices.append(answer)
        random.shuffle(choices)
        
        for i in range(len(choices)):
            print str(i+1) + ")" + choices[i]
        
        guessnum = -1
        while guessnum < 0 or guessnum > 3:
            guess = raw_input("?").strip()
            try: 
                guessnum = int(guess) -1
            except ValueError:
                print "Try again"
            
        if choices[guessnum] == answer:
            num_right += 1
            print "You got it!"
        else:
            print "The answer was:" + answer

        print "You got: " + str(num_right) + " out of: " + str(num_asked)
        
        

