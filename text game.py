def greetings():
    print('hello, this is my first test text game, it may have a lot of bugs, good luck!')
greetings()

health_human = 100
health_gopnik = 250

damage_human = 50
damage_gopnik = 70

armor_human = 120

print('start')
input('gopnik move')
armor_human -= damage_gopnik

print(armor_human)
input('your move')
health_gopnik -= damage_gopnik

print(health_gopnik)
input('gopnik move')
health_human -= damage_gopnik

print(armor_human)
input('This is the demo of this game and this game Project-test')
