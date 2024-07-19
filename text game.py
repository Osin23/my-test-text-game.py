from time import sleep

def greetings():
    print('hello, this is my first test text game, it may have a lot of bugs, good luck!')
greetings()

health_human = 140
health_gopnik = 250

damage_human = 50
damage_gopnik = 70

armor_human = 140

print('start')
input('gopnik move')
armor_human -= damage_gopnik

print(armor_human)
input('your move')
health_gopnik -= damage_human

print(health_gopnik)
input('gopnik move')
armor_human -= damage_gopnik

print(armor_human)
input('your move')
health_gopnik -= damage_human

print(health_gopnik)
input('gopnik move')
health_human -= damage_gopnik

print(health_human)
input('your move')
health_gopnik -= damage_human

print(health_gopnik)
input('gopnik move')
health_human -= damage_gopnik

print(health_human)
input('Gopnik win')

print('loading final scene')
sleep(3)

print('Gopnik: Well, did you get it?Get out of here before I break all your bones.')
sleep(2)

print('human:Whoa, whoa, I m already leaving')
sleep(2)

print('Gopnik:Well, get out of here already')
sleep(2)

print('uploading the final disclaimer')
sleep(5)

print( 'loading.'  )
sleep(1)

print('loading..')
sleep(1)

print('loading...')
sleep(1)

print('loading....')
sleep(3)

print('This is the demo of this game and this game Project-test')
sleep(3)

print('Goodbye')
