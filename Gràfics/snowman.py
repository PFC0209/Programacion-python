import arcade
import random
def main():
    arcade.open_window(600, 600, "Drawing Example")
    arcade.set_background_color(arcade.csscolor.DARK_BLUE)
    arcade.start_render()
    arcade.draw_lrtb_rectangle_filled(0, 599, 200, 0, arcade.csscolor.POWDER_BLUE)
    snowman(300,200, 1)
    arcade.finish_render()
    arcade.run()


def snowman(x, y, escala): 
    # Draw a snow person
    # Snow
    arcade.draw_circle_filled((x*escala), y*escala, (60*escala), arcade.color.WHITE)
    arcade.draw_circle_filled((x*escala), y+(80*escala), (50*escala), arcade.color.WHITE)
    arcade.draw_circle_filled((x*escala), y+(140*escala), (40*escala), arcade.color.WHITE)

    #Eyes
    arcade.draw_circle_filled(x+(-15*escala), y+(150*escala), (5*escala), arcade.color.BLACK)
    arcade.draw_circle_filled(x+(15*escala), y+(150*escala), (5*escala), arcade.color.BLACK)
    #Buttons
    arcade.draw_circle_filled(x*escala, y*escala, 6*escala, arcade.color.BLACK)
    arcade.draw_circle_filled(x*escala, y+(45*escala), 6*escala, arcade.color.BLACK)
    arcade.draw_circle_filled(x*escala, y+(90*escala), 6*escala, arcade.color.BLACK)
    #Hat
    arcade.draw_rectangle_filled((-40*escala)+x, (40*escala)+x, y+(190*escala), y+(180*escala), arcade.color.BLACK)

main()


#  Finish and run
