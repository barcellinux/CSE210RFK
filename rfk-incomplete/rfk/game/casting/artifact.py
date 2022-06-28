from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Artifact is to keep track of its message.

    Attributes:
        _message (string): The message to display        
    """

    def __init__(self):
        """Constructs a new Artifact."""
        self._message = ""        

    def get_message(self):
        """Gets the artifact's message.
        
        Returns:
            message: The artifact's message.
        """
        return self._message

    def set_message(self, message):
        """Updates the message to the given value.
        
        Args:
            message (string): The given value.
        """
        self._message = message
        