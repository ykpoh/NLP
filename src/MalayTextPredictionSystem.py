import nltk
import bigram
import random

print "********************************************************************************************"
print "*                                 Welcome to the                                           *"
print "*                          Malay Text Prediction System                                    *"
print "********************************************************************************************"
while True:
    f = open('malay_tweets.txt')
    raw = f.read().lower()

    tokens = nltk.word_tokenize(raw)

    bgs = nltk.bigrams(tokens)
    bidist = nltk.FreqDist(bgs)
    tokendist = nltk.FreqDist(tokens)
    
    bigram.printTextfile(bidist, "bigramFrequency.txt")
    bigram.printTextfile(tokendist, "tokenFrequency.txt")
    
    print("Please key in a word to predict the next word:")
    userInput = raw_input("> ")
    
    userSentenceProb = bigram.calSentenceBigram(userInput, tokendist, bidist)
    
    predictedWord, bestProb = bigram.calBestProb(userInput, tokendist, bidist)

    if predictedWord != None:
        print "The predicted word: %s" % predictedWord
        print "Its probability is %s" % bestProb
    else:
        randomToken = random.choice(tokendist.keys())
        print "%s does not appear once in our database, therefore our random guest is %s" % (inputLastToken, randomToken)

    userContinue = raw_input("Do you want to continue to use this program?(y/n)\n")
    if userContinue == "n":
        break
