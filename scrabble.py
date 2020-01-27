letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]   

letter_to_points_list = list(zip(letters, points))
letter_to_points = {key:value for key, value in zip(letters, points)}

letter_to_points[" "] = 0  
print(letter_to_points)

player_to_words = {"player1":["BLUE", "TENNIS", "EXIT"], "WordNerd":["EARTH", "EYES", "MACHINE"], "Lexi Con":["ERASER", "BELLY", "HUSKY"], "Prof Reader":["ZAP", "COMA", "PERIOD"]}

player_to_points = {}


def score_word(word):
    word = word.upper()
    score_point = 0
    for i in range(len(word)):
        for letter in letter_to_points:
            if word[i] == letter:
                score_point += letter_to_points[letter]
                print("Found a match: "+letter+" with a scoring of: "+str(letter_to_points[letter]))
            else:
                score_point += 0   

    print(f"Total score of the word \"{word}\" is: "+str(score_point))
    return score_point

#print(score_word("ZAP"))
        

def players_scoring(dictionarylist, resultdict):
    for player in player_to_words:
    
        player_points = 0
        counter = 1

        print("***************************************************\nNow Processing points for player: "+player)
        print("This player has the following words:\n"+str(player_to_words[player]))

        for i in player_to_words[player]:
            print("\nNow processing the word:\n"+str(counter)+". "+i )

            player_points += score_word(i)
            counter += 1    
        
        print("\nTOTAL SCORE OF THE PLAYER \""+player+"\" IS: "+str(player_points)+"\n")
        resultdict[player] = player_points

    return resultdict

test = players_scoring(player_to_words, player_to_points)
print(test)
