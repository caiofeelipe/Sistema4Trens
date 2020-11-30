import arcade
import os

arcade.open_window(500, 600, "Drawing Primitives Example")
arcade.set_background_color(arcade.color.BLACK)

# Start
arcade.start_render()

# TREM-BOLA
arcade.draw_circle_filled(115, 480, 18, arcade.color.RED)
arcade.draw_circle_filled(230, 480, 18, arcade.color.GREEN)
arcade.draw_circle_filled(345, 480, 18, arcade.color.YELLOW)
arcade.draw_circle_filled(230, 400, 15, arcade.color.WHITE)
# TRILHO-RETANGULO
arcade.draw_rectangle_outline(115, 450, 105, 65,arcade.color.RED)
arcade.draw_rectangle_outline(230, 450, 105, 65,arcade.color.GREEN)
arcade.draw_rectangle_outline(345, 450, 105, 65,arcade.color.YELLOW)
arcade.draw_rectangle_outline(230, 350, 332, 105,arcade.color.WHITE)


arcade.finish_render()
arcade.run()