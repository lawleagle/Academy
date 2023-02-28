import SwiftUI


struct Card : View {
    var card : MemoryGame<String>.Card
    
    var body : some View {
        ZStack {
            let shape = RoundedRectangle(cornerRadius:10)
            if card.isFaceUp {
                shape.fill().foregroundColor(.white)
                shape.strokeBorder(lineWidth: 3)
                Text(card.content).font(.largeTitle)
            } else if card.isMatched {
                shape.opacity(0)
            } else {
                shape.fill()
            }
        }
    }
}

struct Memorize : View {
    @ObservedObject var game = EmojiMemoryGame()
    
    private func noSpacingGridItem() -> GridItem {
        var gridItem = GridItem(.adaptive(minimum: CGFloat(70)))
        gridItem.spacing = 0
        return gridItem
    }
    var body : some View {
        VStack {
            Text("score: " + String(game.score))
            Text(game.theme.name)
            ScrollView {
                LazyVGrid(columns: [noSpacingGridItem()], spacing:0) {
                    ForEach(game.cards) { card in
                        Card(card: card)
                            .padding(4)
                            .aspectRatio(2/3, contentMode: .fit)
                            .onTapGesture {
                                game.choose(card)
                            }
                    }
                }
            }
            .foregroundColor(game.theme.color)
            
            Text("new game").onTapGesture {
                game.newGame()
            }
        }
    }
}

struct Memorize_Previews : PreviewProvider {
    static var previews : some View {
        Memorize()
    }
}


@main
struct MemorizeApp: App {
    var body: some Scene {
        WindowGroup {
            Memorize()
        }
    }
}
