#Copyright 2013 Sam Jackson

class actor:

    name = "Generic Actor"
    player = False
    description = "This actor is generic"
    gender = "none" # Can also be "male", "female", or "neuter"
    inventory = [None]
    location = {
                'room' : room,
                'x' : 0, # 'x' and 'y' will be used in absolute and semi-absolute mode. It represents the location of the actor in the world or room respectivly.
                'y' : 0
               }

class room:

    name = "Generic Room"
    description = "This room is generic"
    contains = [None] #The things/actors/rooms in the room
    location = {
                'x' : 0, #This is only used in absolute mode. It represents the room's location in the world.
                'y' : 0,
               }
    exits = {
             'north' = None,
             'south' = None,
             'east' = None,
             'west' = None,
             'northeast' = None,
             'southeast' = None,
             'northwest' = None,
             'southwest' = None,
             'up' = None,
             'down' = None,
             'n' = exits['north'],
             's' = exits['south'],
             'e' = exits['east'],
             'w' = exits['west'],
             'ne' = exits['northeast'],
             'se' = exits['southeast'],
             'nw' = exits['northwest'],
             'sw' = exits['southwest'],
             'u' = exits['up'],
             'd' = exits['down']
            }

class thing:

    name = "Generic Thing"
    description = "This thing is generic"
    container = False
    wearable = False
    carriable = True
    
