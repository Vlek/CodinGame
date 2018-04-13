import sys, math

magicPhrase = raw_input() #"UMNE TALMAR RAHTAINE NIXENEN UMIR"
magicLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ "
currentPosition = 0
runes = [' '] * 30
output = ''
    
def mapper( letters, currentIndex ):
    """maps the letters such that the current letter is in the middle and it makes dealing with the
    stupid change negative and positive easier"""
    numLetters = len(letters)
    return letters[ currentIndex - numLetters/2:] + letters[: (currentIndex + numLetters/2+1) % numLetters]
    
def numChange( letters, desiredLetter, currentLetter ):
    """used to figure out the amount it'd take to change a stone from the currently shown letter to the desired one"""
    mappedletters = mapper( letters, letters.index( currentLetter ) )
    return mappedletters.index( desiredLetter ) - mappedletters.index(currentLetter)
    
def lenSort(a, b):
    """sorting method for getting the string with the lowest length"""
    return len(a) - len(b)

while len(magicPhrase) > 0:
    if runes[currentPosition] != magicPhrase[0]:
        possibleMoves = []
        for stone in range(30):
            distance = numChange([i for i in range(30)], stone, currentPosition)
            movement = '>' * distance if distance > 0 else '<' * abs(distance)
            currentChange = numChange( magicLetters, magicPhrase[0], runes[stone] )
            stoneAdjustment = '+' * currentChange if currentChange > 0 else '-' * abs(currentChange)

            possibleMoves.append( movement + stoneAdjustment )
        possibleMoves.sort( lenSort )
        output = output + possibleMoves[0]

        movements = possibleMoves[0].count('>') if possibleMoves[0].count('>') > 0 else possibleMoves[0].count('<') * -1 if possibleMoves[0].count('<') > 0 else 0
        currentPosition = currentPosition + movements if currentPosition + movements >= 0 else currentPosition + movements + len(runes)
        
        runes[currentPosition] = magicPhrase[0]

    while runes[currentPosition] == magicPhrase[0]:
        output = output + '.'
        magicPhrase = magicPhrase[1:]
        if magicPhrase == '':
            break

print output
