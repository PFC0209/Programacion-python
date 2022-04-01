from easyinput import read
escala = read(float)
import arcade

arcade.open_window(600, 600, "Drawing Example")
def arbre(x,y, escala):
    arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.GREEN)
    arcade.draw_lrtb_rectangle_filled(x-(12*escala),x+(12*escala),y+(75*escala),y,arcade.csscolor.SIENNA)
    arcade.draw_circle_filled(x,y+(110*escala),(45*escala),	(34, 139, 34))
    arcade.draw_circle_filled((35*escala)+x,(100*escala)+y,(29*escala),arcade.csscolor.GREEN)
    arcade.draw_circle_filled((29*escala)+x,(130*escala)+y,(29*escala),	(34, 139, 34))
    arcade.draw_circle_filled((2*escala)+x,(150*escala)+y,(29*escala),arcade.csscolor.GREEN)
    arcade.draw_circle_filled((-32*escala)+x,(100*escala)+y,(29*escala),arcade.csscolor.GREEN)
    arcade.draw_circle_filled((-25*escala)+x,(125*escala)+y,(29*escala), (34, 139, 34))
    
# Set the background color
arcade.set_background_color(arcade.csscolor.SKY_BLUE)

# Get ready to draw
arcade.start_render()

arbre(300,300, escala)



# Finish drawing
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()
