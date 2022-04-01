import arcade
import math
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
def colisio(a, b):
    distancia = math.sqrt(math.pow((a.position_x - b.position_x),2) + math.pow((a.position_y - b.position_y),2))
    if distancia <= (a.radius + b.radius):
   # if (a.position_x == b.position_x):
        #print("x = x")
        return True
    else:
        return False   

class Arbre:
    def __init__(self, px, py):
        self.px = px
        self.py = py
        self.color = arcade.csscolor.BLUE_VIOLET
    def draw(self):
        x = self.px
        y = self.py
      
        arcade.draw_lrtb_rectangle_filled(x-(12),x+(12),y+(75),y,arcade.csscolor.SIENNA)
        arcade.draw_circle_filled(x,y+(110),(45), self.color)
        arcade.draw_circle_filled((35)+x,(100)+y,(29), self.color)
        arcade.draw_circle_filled((29)+x,(130)+y,(29), self.color)
        arcade.draw_circle_filled((2)+x,(150)+y,(29), self.color)
        arcade.draw_circle_filled((-32)+x,(100)+y,(29), self.color)
        arcade.draw_circle_filled((-25)+x,(125)+y,(29), self.color)
    def canvia(self):
        self.color = arcade.csscolor.ALICE_BLUE
class Ball:
    """ This class manages a ball bouncing on the screen. """

    def __init__(self, position_x, position_y, change_x, change_y, radius, color):
        """ Constructor. """

        # Take the parameters of the init function above, and create instance variables out of them.
        self.position_x = position_x
        self.position_y = position_y
        self.change_x = change_x
        self.change_y = change_y
        self.radius = radius
        self.color = color

    def draw(self):
        """ Draw the balls with the instance variables we have. """
        arcade.draw_circle_filled(self.position_x, self.position_y, self.radius, self.color)

    def update(self):
        """ Code to control the ball's movement. """

        # Move the ball
        self.position_y += self.change_y
        self.position_x += self.change_x

        # See if the ball hit the edge of the screen. If so, change direction
        if self.position_x < self.radius:
            self.change_x *= -1

        if self.position_x > SCREEN_WIDTH - self.radius:
            self.change_x *= -1

        if self.position_y < self.radius:
            self.change_y *= -1

        if self.position_y > SCREEN_HEIGHT - self.radius:
            self.change_y *= -1


class MyGame(arcade.Window):

    def __init__(self, width, height, title):

        # Call the parent class's init function
        super().__init__(width, height, title)

        # Set the background color
        arcade.set_background_color(arcade.color.ASH_GREY)

                # Attributes to store where our ball is
        self.ball = Ball(50, 50, 3, 3, 50, arcade.color.WHITE)
        self.ball2 = Ball(10, 10, 5, 10, 10, arcade.color.RED)
        self.ball3 = Ball(20, 20, 6, 9, 20, arcade.color.YELLOW)
        self.ball4 = Ball(30, 30, 1, 10, 30, arcade.color.AIR_SUPERIORITY_BLUE)
        self.arbre = Arbre(200, 0)
    def on_draw(self):
        """ Called whenever we need to draw the window. """
        arcade.start_render()
        self.ball.draw()
        self.ball2.draw()
        self.ball3.draw()
        self.ball4.draw()
        self.arbre.draw()
    def update(self, delta_time):
        """ Called to update our objects. Happens approximately 60 times per second."""
        self.ball.update()
        self.ball2.update()
        self.ball3.update()
        self.ball4.update()

def main():
    window = MyGame(640, 480, "Drawing Example")

    arcade.run()


main()