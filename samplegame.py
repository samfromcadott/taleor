import taleor

WhiteRoom = taleor.room
WhiteRoom.name = "White Room"
WhiteRoom.description = "The room is compleatly cubic. Everything is white and a single flourescent light is in the ceiling."

YellowRoom = taleor.room
YellowRoom.name = "Yellow Room"
YellowRoom.description = "The room is compleatly cubic. The walls are all yellow and a single flourescent light is in the white ceiling."

RedRoom = taleor.room
RedRoom.name = "Red Room"
RedRoom.description = "The room is compleatly cubic. The walls are all red and a single flourescent light is in the white ceiling."

BlueRoom = taleor.room
BlueRoom.name = "Blue Room"
BlueRoom.description = "The room is compleatly cubic. The walls are all blue and a single flourescent light is in the white ceiling."

# +------+ +------+
# |      |_|      |
# |  WR   _   YR  |
# |      | |      |
# +-+  +-+ +-+  +-+  N
#   |  |     |  |   W+E
# +-+  +-+ +-+  +-+  S
# |      |_|      |
# |  RR   _   BR  |
# |      | |      |
# +------+ +------+
