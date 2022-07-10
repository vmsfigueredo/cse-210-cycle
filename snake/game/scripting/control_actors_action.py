import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlActorsAction(Action):
    """
    An input action that controls the snake.
    
    The responsibility of ControlActorsAction is to get the direction and move the snake's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(0, -constants.CELL_SIZE)

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        # left
        if self._keyboard_service.is_key_down('a'):
            if(player1.get_facing() != "right"):
                self._direction = Point(-constants.CELL_SIZE, 0)
                player1.turn_head(self._direction)
                player1.set_facing("left")
            
        if self._keyboard_service.is_key_down('j'):
            if(player2.get_facing() != "right"):
                self._direction = Point(-constants.CELL_SIZE, 0)
                player2.turn_head(self._direction)
                player2.set_facing("left")

        # right
        if self._keyboard_service.is_key_down('d'):
            if(player1.get_facing() != "left"):
                self._direction = Point(constants.CELL_SIZE, 0)
                player1.turn_head(self._direction)
                player1.set_facing("right")
            
        if self._keyboard_service.is_key_down('l'):
            if(player2.get_facing() != "left"):
                self._direction = Point(constants.CELL_SIZE, 0)
                player2.turn_head(self._direction)
                player2.set_facing("right")
        # up
        if self._keyboard_service.is_key_down('w'):
            if(player1.get_facing() != "down"):
                self._direction = Point(0, -constants.CELL_SIZE)
                player1.turn_head(self._direction)
                player1.set_facing("up")
        if self._keyboard_service.is_key_down('i'):
            if(player2.get_facing() != "down"):
                self._direction = Point(0, -constants.CELL_SIZE)
                player2.turn_head(self._direction)
                player2.set_facing("up")
            
        # down
        if self._keyboard_service.is_key_down('s'):
            if(player1.get_facing() != "up"):
                self._direction = Point(0, constants.CELL_SIZE)
                player1.turn_head(self._direction)
                player1.set_facing("down")
            
        if self._keyboard_service.is_key_down('k'):
            if(player2.get_facing() != "up"):
                self._direction = Point(0, constants.CELL_SIZE)
                player2.turn_head(self._direction)
                player2.set_facing("down")
            