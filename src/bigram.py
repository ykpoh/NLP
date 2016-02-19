

def printTextfile(fdist, fileName):
    """This function will print the given frequency distribution to
    text file with the given filename"""
    #Create the file with the given filename.
    file = open(fileName, "w+")
    #Write each bigram with its frequency into the file.
    for k,v in fdist.items():
        file.write("%s : %s\n" % (k,v))
        
def calSentenceBigram(userInput, tokendist, bidist):
    """This function will calculate the bigram probability over the whole
    given sentence."""
    #import nltk library
    import nltk
    #makes all user input into small capital letters
    userInput = userInput.lower()
    #tokenize user input into list using nltk.word_tokenize
    userTokens = nltk.word_tokenize(userInput)
    #initialize the probability
    userSentenceProb = 1.0
    #Calculate the bigram probability of the sentence through looping
    for prevWord, nextWord in zip(userTokens, userTokens[1:]):
        #get the frequency of the word exists in the database
        wordCount = tokendist.get(prevWord)
        #get the frequency of the occurence of prevWord and nextWord exists in the database
        bigramCount = bidist.get((prevWord, nextWord))
        #if it does not exists in our database, the bigram probability of prevWord and nextWord
        #will be assigned with 1. It cannot be 0 because it will make the total probability 0.
        if(bigramCount == None):
            userSentenceProb *= float(1)
        #if it exists in our database, it will calculate the bigram probability of the current
        #prevWord and nextWord, then multiply with the total previous probability. 
        else:
            userSentenceProb *= float(bigramCount)/float(wordCount)
    return userSentenceProb

def calBestProb(userInput, tokendist, bidist):
    """This function will predict the next word user is going to key in based on
    the bigram probability calculated from the given sentence"""
    #import nltk library
    import nltk
    #makes all user input into small capital letters
    userInput = userInput.lower()
    #tokenize user input into list using nltk.word_tokenize
    userTokens = nltk.word_tokenize(userInput)
    #Get the bigram probability over the whole given sentence from calSentenceBigram.
    userSentenceProb = calSentenceBigram(userInput, tokendist, bidist)
    #Initialize the probabilities.
    prob = 0.0
    bestProb = 0
    #Get the last word of the given sentence.
    inputLastToken = userTokens[len(userTokens) - 1]
    #Get the frequency of last word exists in our database. 
    lasttokenCount = tokendist.get(inputLastToken)
    #By default, the predictedWord is undefined. 
    predictedWord = None
    #Loop through bigram frequency distribution list.
    for k,v in bidist.items():
        #if the first word of the bigram is equal to inputLastToken, 
        #it will calculate its bigram probability
        if(k[0] == inputLastToken):
            #Calculate the bigram probability over the whole sentence. 
            prob = float(v)/float(lasttokenCount) * userSentenceProb
            #if the current probability is higher than bestProb, 
            #bestProb will be replaced with this probability.
            #Predicted word will be the word with this probability.
            if prob > bestProb:
                bestProb = prob
                predictedWord = k[1]
                
    return bestProb, predictedWord