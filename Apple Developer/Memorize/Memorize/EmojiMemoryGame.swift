//
//  EmojiMemoryGame.swift
//  Memorize
//
//  Created by Truta, Emanuel on 03/02/2023.
//

import SwiftUI

struct Theme
{
    var name : String
    var emojis : Array<String>
    var noPairs : Int
    var color : Color
}
var themes = [
    Theme(
        name: "vehicles",
        emojis: ["✈️", "🚗", "🚀", "🚅", "🚌", "🏎", "🚜", "🛵", "🚲", "🛴", "🦽", "🏍",
                "🛸", "🚁", "🛶", "🚤", "🛰", "🛟", "🛺", "🩼", "🚑", "🚚", "🛻", "🚓"],
        noPairs: 100,
        color: .blue
    ),
    Theme(
        name: "animals",
        emojis: ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐻‍❄️", "🐨", "🐯", "🦁",
                "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🦆", "🦅", "🦉", "🦇", "🐺", "🦄"],
        noPairs: 8,
        color: .red
    ),
    Theme(
        name: "alphabet",
        emojis: ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        noPairs: 6,
        color: .green
    ),
    Theme(
        name: "vehicles2",
        emojis: ["✈️", "🚗", "🚀", "🚅", "🚌", "🏎", "🚜", "🛵", "🚲", "🛴", "🦽", "🏍",
                "🛸", "🚁", "🛶", "🚤", "🛰", "🛟", "🛺", "🩼", "🚑", "🚚", "🛻", "🚓"],
        noPairs: 100,
        color: .red
    ),
    Theme(
        name: "animals2",
        emojis: ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐻‍❄️", "🐨", "🐯", "🦁",
                "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🦆", "🦅", "🦉", "🦇", "🐺", "🦄"],
        noPairs: 8,
        color: .green
    ),
    Theme(
        name: "alphabet2",
        emojis: ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
                "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"],
        noPairs: 6,
        color: .blue
    ),
]

class EmojiMemoryGame : ObservableObject
{
    var theme : Theme!
    @Published private var game : MemoryGame<String>!
    
    init()
    {
        newGame()
    }
    
    var cards : Array<MemoryGame<String>.Card>
    {
        return game.cards
    }
    
    var score : Int
    {
        return game.score
    }
    
    // MARK: - Intent(s)
    
    func choose(_ card: MemoryGame<String>.Card) {
        game.choose(card)
    }
    
    func newGame() {
        let themeNo = Int.random(in: 0..<6)
        theme = themes[themeNo]
        theme.noPairs = min(theme.noPairs, 12)
        theme.emojis.shuffle()
        game =
            MemoryGame<String>(noPairs: theme.noPairs)
            { pairIndex in
                return theme.emojis[pairIndex]
            }
    }
}
