//
//  MemoryGame.swift
//  Memorize
//
//  Created by Truta, Emanuel on 03/02/2023.
//

import Foundation

struct MemoryGame<CardContent> where CardContent : Equatable
{
    struct Card : Identifiable {
        var isFaceUp : Bool = false
        var isMatched : Bool = false
        var seen : Bool = false
        var content : CardContent
        var firstSeen : Date?
        
        var id : Int
    }
    
    
    var cards : [Card]
    var indexOfVisibleCard : Int?
    var score = 0.0

    mutating func choose(_ card : Card) {
        if let chosenIndex = cards.firstIndex(where: { $0.id == card.id }),
            !cards[chosenIndex].isFaceUp,
            !cards[chosenIndex].isMatched
        {
            if let matchIndex = indexOfVisibleCard {
                if cards[chosenIndex].content == cards[matchIndex].content {
                    cards[chosenIndex].isMatched = true
                    cards[matchIndex].isMatched = true
                    
                    if let date = cards[matchIndex].firstSeen {
                        score += 10.0 - DateInterval(start: date, end: Date()).duration
                    } else {
                        score += 10.0
                    }
                    if let date = cards[chosenIndex].firstSeen {
                        score += 10.0 - DateInterval(start: date, end: Date()).duration
                    } else {
                        score += 10.0
                    }
                    score += 2
                }
                indexOfVisibleCard = nil
            } else {
                for index in cards.indices {
                    cards[index].isFaceUp = false
                }
                indexOfVisibleCard = chosenIndex
            }
            cards[chosenIndex].isFaceUp = true
            if cards[chosenIndex].firstSeen == nil {
                cards[chosenIndex].firstSeen = Date()
            }
        }
    }
    
    init(noPairs : Int, createCardContent : (Int)->CardContent) {
        cards = [Card]()
        for pairIndex in 0..<noPairs {
            let content = createCardContent(pairIndex)
            cards.append(Card(content: content, id: pairIndex * 2))
            cards.append(Card(content: content, id: pairIndex * 2 + 1))
        }
        cards.shuffle()
    }
}
