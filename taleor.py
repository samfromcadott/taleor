# Copyright 2013 Sam Jackson


world_mode = 'realative' # Could also be 'absolute' or 'semi-absolute'
tense = 'present' # Could also be 'past' or 'future'
person = 'second' # Can also be 'first' or 'third'


class actor:

    name = "Generic Actor"
    alt_name = [None]
    player = False
    description = "This actor is generic"
    gender = "none" # Can also be "male", "female", or "neutral"
    inventory = [None]
    location = {
                'room' : room,
                'x' : 0, # 'x' and 'y' will be used in absolute and semi-absolute mode. It represents the location of the actor in the world or room respectivly.
                'y' : 0
               }

class room:

    name = "Generic Room"
    alt_name = [None]
    description = "This room is generic"
    contains = [None] # The things/actors/rooms in the room
    location = {
                'x' : 0, # This is only used in absolute mode. It represents the room's location in the world.
                'y' : 0,
               }
    exits = { # These are only used in realative and semi-absolute mode
             'north' : None,
             'south' : None,
             'east' : None,
             'west' : None,
             'northeast' : None,
             'southeast' : None,
             'northwest' : None,
             'southwest' : None,
             'up' : None,
             'down' : None,
             'n' : exits['north'],
             's' : exits['south'],
             'e' : exits['east'],
             'w' : exits['west'],
             'ne' : exits['northeast'],
             'se' : exits['southeast'],
             'nw' : exits['northwest'],
             'sw' : exits['southwest'],
             'u' : exits['up'],
             'd' : exits['down']
            }

class thing:

    name = "Generic Thing"
    alt_name = [None]
    description = "This thing is generic"
    numeration = 1 # If this is 1 it will be simgular, if it is 0 it will not have enumeration, if it is anything else it will be plural
    container = False
    wearable = False
    carriable = True
    eadable = False
    sceanery = False
    weildable = False
    contains = [None]

def runGame():
    pass

def roomDescription():

    return "", player.location['room'].name, "\n\n", player.location['room'].description, "\n\n", "You see ", player.location['room'].contains, "."



#BEGIN PLAYER CHARACTER DEFINITION BLOCK

player = actor #This object will always be used as the player character
#The writer changes the attributes to fit their character

player.name = "AFGNCAAP"
player.description = "You look like yourself."
player.gender = 'neutral'

#END PLAYER CHARACTER DEFINITION BLOCK



tense_forms = { # Contains forms for tense and perspective for messages.

               'first' : {
                          'subject' : 'I',
                          'past' : 'saw',
                          'present' : 'see',
                          'future' : 'will see',
                         },

               'second' : {
                           'subject' : 'You',
                           'past' : 'saw',
                           'present' : 'see',
                           'future' : 'will see',
                          },

               'third' : {
                          'subject' : player.name,
                          'past' : 'saw',
                          'present' : 'sees',
                          'future' : 'will see',
                         }
              }
