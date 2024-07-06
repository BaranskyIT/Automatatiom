from user import user
from card import Card

user1 = user("Alex")

user1.sayName()
user1.setAge(33)
user1.sayAge()


card = Card("4234 1234 1234 1234", "11/11", "AlexF")

user1.addCard(card)
user1.getCard().pay(1000)
