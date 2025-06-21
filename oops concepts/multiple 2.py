class card:
    card_name ="card"
    def card_(self):
        print(self.card_name)
class cards:
    cards_name = "cards"
    def cards_(self):
        print(self.cards_name)

class cardson(card, cards):
    def parent_(self):
        print("card", self.card_name)
        print("cards", self.cards_name)
s1 = cardson()
s1.card_name = "credit card"
s1.cards_name = "debit card"
s1.parent_()