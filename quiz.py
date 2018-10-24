import sys
import json
import random

def usage():
    print ("python quiz.py q1.json")



if __name__ == "__main__":

    if len(sys.argv) != 2:
        usage()
        sys.exit()

    f = open(sys.argv[1], "r")
    qs = json.loads(f.read())
    f.close()

    random.shuffle(qs)
    num_right = 0
    num_asked = 0
    for q in qs:
        num_asked += 1
        print ("what is the definition of the word:" + q["word"] + "?")
        
        if "answers" in q:
            answers = q["answers"]
        else:
            answers = [q["answer"]]
        random.shuffle(answers)
        answer = answers[0]
            
        choices = q["wrongs"][0:3]
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
        
        

