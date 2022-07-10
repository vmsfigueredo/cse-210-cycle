import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_segment_collision(cast)
            self._handle_players_collision(cast)
            
        self._handle_game_over(cast)

    def _handle_segment_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        head1 = player1.get_segments()[0]
        head2 = player2.get_segments()[0]
        
        segments1 = player1.get_segments()[1:]
        segments2 = player2.get_segments()[1:]
        
        for segment in segments1:
            if head1.get_position().equals(segment.get_position()):
                self._is_game_over = True     
        for segment in segments2:  
            if head2.get_position().equals(segment.get_position()):
                self._is_game_over = True
    def _handle_players_collision(self, cast):
        """Sets the game over flag if the snake collides with one of its segments.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        player1 = cast.get_first_actor("player1")
        player2 = cast.get_first_actor("player2")
        score = cast.get_first_actor("scores")
        score2 = cast.get_actor("scores", 1)
        head1 = player1.get_segments()[0]
        head2 = player2.get_segments()[0]
        
        segments1 = player1.get_segments()[1:]
        segments2 = player2.get_segments()[1:]
        
        for segment in segments1:
            if head2.get_position().equals(segment.get_position()):
                score.add_points(1)

        for segment in segments2:  
            if head1.get_position().equals(segment.get_position()):
                score2.add_points(1)
    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            player1 = cast.get_first_actor("player1")
            player2 = cast.get_first_actor("player2")
            segments1 = player1.get_segments()
            segments2 = player2.get_segments()

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2 - 30)
            position = Point(x, y)

            message = Actor()
            message.set_font_size(30)
            message.set_text("Game Over!")
            message.set_position(position)
            message.set_color(constants.RED)
            cast.add_actor("messages", message)
            
            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)
            
            winner = Actor()
            winner.set_position(position)
            score = cast.get_first_actor("scores")
            score2 = cast.get_actor("scores", 1)
            if score.get_points() > score2.get_points():
                winner.set_text("Winner: Player One")
                winner.set_color(constants.GREEN)
            elif score.get_points() < score2.get_points():
                winner.set_text("Winner: Player Two")
                winner.set_color(constants.BLUE)
            else:
                winner.set_text("Tie!")
                winner.set_color(constants.RED)
            winner.set_font_size(30)
            cast.add_actor("messages", winner)
            
            for segment in segments1:
                segment.set_color(constants.GREY)
            for segment in segments2:
                segment.set_color(constants.GREY)