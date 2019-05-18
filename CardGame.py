# This code is for LeetCode Assignment: 950. Reveal Cards In Increasing Order

class Solution:
    def deckRevealedIncreasing(self, deck: list) -> list:
        result = self.playGame(deck)
        sorted = self.getSortedCards(deck)
        return self.getOriginalCards(deck, result, sorted)
            
    
    #def playGame(self, cards: list) -> list:
     #   cards = self.copyList(cards)
      #  revealed = []
       # while len(cards) > 0:
        #    first = cards[0]
         #   del cards[0]    
          #  revealed.append(first)
           # # move the first to the last 
            #if len(cards) > 0:
             #   first = cards[0]
              #  del cards[0]
               # cards.append(first)
        #return revealed
    

    def playGame(self, cards: list) -> list:
	    new = []
	    while len(cards) > 0:		
		    index = 0
		    length = len(cards)
		    if length == 1:
			    new.append(cards[0])
			    break
		    tempCards = cards[0:length]
		    isOdd = length % 2 == 1
		    while index < length - 1:
			    card = cards[index]
			    tempCards.remove(card)
			    new.append(card)			
			    index += 2 # jump to one after 
		    if isOdd:
			    lastItem = cards[length - 1]
			    tempCards.remove(lastItem)
			    tempCards.insert(0, lastItem)
		    cards = tempCards # copy back
	    return new
    
    
    def getOriginalCards(self, original: list, result: list, sorted: list) -> list:      
        rightOriginal = self.copyList(original)
        for index in range(0, len(sorted)):          
            expected = sorted[index] # 2
            actual = result[index] # 17
            indexOfOriginal = original.index(actual) # 3
            rightOriginal[indexOfOriginal] = expected
        return rightOriginal

    # replace using sounting sort
    def getSortedCards(self, original: list) -> list:
        original = self.copyList(original)
        sorted = []
        while len(original) > 0:
            smallest = self.getSmallest(original)
              # index = original.index(smallest)
            original.remove(smallest)
            sorted.append(smallest)
        return sorted

    def getSmallest(self, items: list) -> list:
        smallest = items[0]
        for item in items:
            if item < smallest: 
                smallest = item
        return smallest

    def copyList(self, original: list) -> list:
        return original[0: len(original)]