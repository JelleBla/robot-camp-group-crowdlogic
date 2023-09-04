import jelle
import rachna
import alexia
import yuyue
import karolina 

def name():
    name = "Luca"
    return name

def character():
    ch="Gina"
    return ch

def chapter1():
    txt= f'The game was good, and everyone was happy about the result. {character()}, {jelle.character()} and {rachna.character()} were happily discussing it while {karolina.character()}, {alexia.character()} and {yuyue.character()} were singing with the local ultras.The six lovers were enjoying the beautiful moments they were having together, taking selfies and sharing a kiss. But the time had to come for them to leave, so they looked for an exit.'
    return txt
    
def chapter2():
    txt = f"Pure chaos. {alexia.character()} was too drunk to care about people pushing him. {character()} was crying as she was stuck between two very tall man. {jelle.character()}, on the other hand, managed to avoid the crowd by jumping the fence.{yuyue.character()} was having fun as the crowd reminded him of being in the middle of a rave, also he was too drunk to care. {rachna.character()} and {karolina.character()} were making use of the cover from the crowd to explore each other's bodies. All of them were just trying to catch a train." 
    return txt

def chapter3():
    txt= f"In the end, {character()}, {jelle.character()}, {karolina.character()}, {alexia.character()}, {yuyue.character()} and {rachna.character()} were sitting in the train telling each other's crazy stories on how they survived the crowd. The six lovers were relieved to have found each other again, and now their love was stronger than ever. And just like this, the story of the six lovers' end. Some people may say that this is a bad story, some people that is not coherent. But does it really matter? Just like love, a love story has no rules or no boundaries." 
    return txt

print(chapter1())
print(chapter2())
print(chapter3())