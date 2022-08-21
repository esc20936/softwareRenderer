from gl import Renderer, color, V3, V2
from texture import Texture
from shaders import *

width = 1920
height = 1080

rend = Renderer(width, height)

# rend.dirLight = V3(-1,0,0)

rend.background = Texture("models/fondo.bmp")
rend.glClearBackground()


# rend.normal_map = Texture("models/model_normal.bmp")
# rend.active_shader = glow
# rend.glLoadModel("models/model.obj",
#                  translate = V3(2, -2, -7),
#                  scale = V3(4,4,4),
#                  rotate = V3(0,-20,0))

rend.active_texture = Texture("models/spidermanT.bmp")
rend.active_shader = glow_custom
rend.glLoadModel("models/spiderman.obj",
                 translate = V3(-0.75, -1, -5),
                 scale = V3(1,1,1),
                 rotate = V3(0,-50,0))

# rend.active_texture = Texture("models/marioT.bmp")
# rend.active_shader = glow_lBlue
# rend.glLoadModel("models/mario.obj",
#                  translate = V3(-1, 2.5, -9),
#                  scale = V3(1,1,1),
#                  rotate = V3(0,0,0))


rend.active_texture = Texture("models/venomM.bmp")
rend.normal_map = Texture("models/body_normal.bmp")
rend.active_shader = normalMap
rend.glLoadModel("models/model.obj",
                 translate = V3(1, -4, -2),
                 scale = V3(4,4,4),
                 rotate = V3(0,-120,0))

rend.glFinish("prueba.bmp")