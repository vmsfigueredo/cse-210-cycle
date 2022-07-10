import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.player1 import Player1
from game.casting.player2 import Player2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    cast.add_actor("player1", Player1())
    cast.add_actor("player2", Player2())
    cast.add_actor("scores", Score("Player One"))
    cast.add_actor("scores", Score("Player Two"))
    
    # Def Positions
    score2 = cast.get_actor("scores", 1)
    score2.set_position(Point(constants.MAX_X - constants.FONT_SIZE * 10, 5))
    score1 = cast.get_actor("scores", 0)
    score1.set_position(Point(5 , 5))
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()