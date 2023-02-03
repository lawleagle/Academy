import SwiftUI

struct CardView : View {
    var content = "✈️"
    @State var hidden = false
    var body : some View {
        ZStack {
            let cardShape = RoundedRectangle(cornerRadius:20)
            if !hidden {
                cardShape.fill().foregroundColor(.white)
                cardShape.strokeBorder(lineWidth: 3)
                Text(content).font(.largeTitle)
            } else {
                cardShape.fill().foregroundColor(.red)
                cardShape.strokeBorder(lineWidth: 3)
            }
        }
        .padding(1)
        .onTapGesture {
            hidden = !hidden
        }
    }
}

struct ContentView : View {
    @State var theme = 2
    @State var emojis = [
        ["✈️", "🚗", "🚀", "🚅", "🚌", "🏎", "🚜", "🛵", "🚲", "🛴", "🦽", "🏍",
         "🛸", "🚁", "🛶", "🚤", "🛰", "🛟", "🛺", "🩼", "🚑", "🚚", "🛻", "🚓"],
        ["🐶", "🐱", "🐭", "🐹", "🐰", "🦊", "🐻", "🐼", "🐻‍❄️", "🐨", "🐯", "🦁",
         "🐮", "🐷", "🐸", "🐵", "🐔", "🐧", "🦆", "🦅", "🦉", "🦇", "🐺", "🦄"],
        ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
         "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
    ]
    @State var emojisUsed = 26
    let minimum_widths = [0,
        0, 0, 0, 120, 100, 100, 100, 100, 80, 80, 80, 80, 80, 80, 80, 60,
        60, 60, 60, 60, 60, 60, 60, 60, 50
    ]
    @State var minimum_width = 50
    var body : some View {
        VStack {
            Text("Memorize!").font(.largeTitle)
            HStack {
                Button(action: {
                    theme = 0
                    emojis[theme].shuffle()
                    emojisUsed = Int.random(in: 4...24)
                    minimum_width = minimum_widths[emojisUsed]
                }, label: {
                    VStack {
                        Image(systemName: "car").foregroundColor(.black).padding(0.1)
                        Text("vehicles")
                    }
                })
                Button(action: {
                    theme = 1
                    emojis[theme].shuffle()
                    emojisUsed = Int.random(in: 4...24)
                    minimum_width = minimum_widths[emojisUsed]
                }, label: {
                    VStack {
                        Image(systemName: "face.smiling.inverse").foregroundColor(.black).padding(0.1)
                        Text("animals")
                    }
                })
                Button(action: {
                    theme = 2
                    emojis[theme].shuffle()
                    emojisUsed = Int.random(in: 4...24)
                    minimum_width = minimum_widths[emojisUsed]
                }, label: {
                    VStack {
                        Image(systemName: "abc").foregroundColor(.black).padding(0.1)
                        Text("letters")
                    }
                })
            }
            ScrollView {
                LazyVGrid(columns: [GridItem(.adaptive(minimum: CGFloat(minimum_width)))]) {
                    ForEach(emojis[theme][0..<emojisUsed], id: \.self, content: { emoji in
                        CardView(content: emoji)
                            .aspectRatio(2/3, contentMode: .fit)
                    })
                }
                .padding(.horizontal)
                .foregroundColor(.red)
                
                Spacer()
                
                //            HStack {
                //                Button(action: {
                //                    emojiCount -= 1
                //                    if emojiCount < 0 { emojiCount = 0 }
                //                }, label: { Image(systemName: "minus.circle") })
                //                .padding()
                //
                //                Spacer()
                //
                //                Button(action: {
                //                    emojiCount += 1
                //                    if emojiCount > 24 { emojiCount = 24 }
                //                }, label: { Image(systemName: "plus.circle") })
                //                .padding()
                //            }
                //            .font(.largeTitle)
            }
        }
    }
}

struct ContentView_Previews : PreviewProvider {
    static var previews : some View {
        ContentView()
    }
}
