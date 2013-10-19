# Copyright (c) 2013, Sam Jackon
# All rights reserved.

# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#     * Redistributions of source code must retain the above copyright
#       notice, this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice, this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of Sam Jackon nor the
#       names of its contributors may be used to endorse or promote products
#       derived from this software without specific prior written permission.

# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL SAM JACKSON BE LIABLE FOR ANY
# DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
# ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

world_mode = 'realative' # Could also be 'absolute' or 'semi-absolute'
tense = 'present' # Could also be 'past' or 'future'
person = 'second' # Can also be 'first' or 'third'


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
             'n' : 'north',
             's' : 'south',
             'e' : 'east',
             'w' : 'west',
             'ne' : 'northeast',
             'se' : 'southeast',
             'nw' : 'northwest',
             'sw' : 'southwest',
             'u' : 'up',
             'd' : 'down'
            }


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
    location = {
                'room' : room,
                'x' : 0, # 'x' and 'y' will be used in absolute and semi-absolute mode. It represents the location of the thing in the world or room respectivly.
                'y' : 0
               }

def runGame():
    pass

def roomDescription():

    return "" + player.location['room'].name + "\n\n" + player.location['room'].description + "\n\n" + "You see " + str( player.location['room'].contains ) + "."



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
