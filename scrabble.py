letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]   

#zipping the two lists together
letter_to_points_list = list(zip(letters, points))
letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0  
print(letter_to_points)

#players words - add your player name as key and words in value as a list
#save yours words in upper, it is better, but its ok if you dont
player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "WordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERiod"]}

#for storing the players points 
player_to_points = {}

#Function for finding the total score of the word by calculating each alphabet's score
def score_word(word):
    #for making the words uppercase
    word = word.upper()

    #for saving each alphabet's points' 
    score_point = 0

    #loop for the number of alphabets in the word
    for i in range(len(word)):

        #loop from the letters list with each entry and match the keys with the alphabet 
        for letter in letter_to_points:
            if word[i] == letter:
                score_point += letter_to_points[letter]
                print("Found a match: "+letter+" with a scoring of: "+str(letter_to_points[letter]))
                
                #if the word is not in the dictionary return 0 for the alphabet
            else:
                score_point += 0   

    print(f"Total score of the word \"{word}\" is: "+str(score_point))
    return score_point

#print(score_word("ZAP"))
        
#Take in a dictionary with the players as keys in strings and the values as words from each player and provides back a dictionary with each player as key and score of each as value 
def players_scoring(dictionarylist, resultdict):
    
    #loop through each key of input dictionary 
    for player in dictionarylist:
        
        #for each player and is added to 
        player_points = 0
        counter = 1

        print("***************************************************\nNow Processing points for player: "+player)
        print("This player has the following words:\n"+str(dictionarylist[player]))
        
        # loop the values of each player 
        for i in dictionarylist[player]:
            print("\nNow processing the word:\n"+str(counter)+". "+i )

            #run the score_word function to calculate the score of each and word store in the player_points variable
            player_points += score_word(i)
            counter += 1    
        
        print("\nTOTAL SCORE OF THE PLAYER \""+player+"\" IS: "+str(player_points)+"\n")
        # adding the player and player points to the output dict
        resultdict[player] = player_points

    return resultdict

test = players_scoring(player_to_words, player_to_points)
#print(test)

'''
if you want extended practice, try to implement some of these ideas with the Python you’ve learned:

play_word() — a function that would take in a player and a word, and add that word to the list of words they’ve played

update_point_totals() — turn your nested loops into a function that you can call any time a word is played

make your letter_to_points dictionary able to handle lowercase inputs as well
'''

def play_word_add(player, word, score_dict):
    temp_list = []
    #loop the keys
    
    for user in score_dict:
    #match the user to the player in the dictionary
        if user == player:
            temp_list = score_dict[user]
    #append the list with the word
            temp_list.append(word) 
    #make the new list as value for the player key
    score_dict[player] = temp_list    

    return score_dict


play_word_add("player1", "HELLO", player_to_words)
print(player_to_words)
