from gl import Raytracer, color, V2, V3
from obj import Obj, Texture, Envmap
from sphere import *
import random

wall = Material(diffuse = color( 0.49, 0.67, 0.48 ), spec = 16)
roof = Material(diffuse= color( 0.66, 0.84, 0.67 ), spec = 16)
floor = Material(diffuse = color(0.4, 0.35, 0.35 ), spec = 16)
cubo = Material(diffuse = color(0.4, 0.69, 0.8 ), spec = 32)
reflexion = Material(spec = 64, matType = REFLECTIVE)
refraxion = Material(spec = 64, ior = 2.5, matType= TRANSPARENT) 

width = 1000
height = 500
r = Raytracer(width,height)
r.glClearColor(0.2, 0.6, 0.8)
r.glClear()

#r.envmap = Envmap('envmap.bmp')
r.envmap = Envmap('street.bmp')

print('\nThis render gonna be legen—\n')
# Lights
r.pointLights.append( PointLight(position = V3(-4,4,0), intensity = 0.5))
r.pointLights.append( PointLight(position = V3( 4,0,0), intensity = 0.5))
r.dirLight = DirectionalLight(direction = V3(1, -1, -2), intensity = 0.2)
r.ambientLight = AmbientLight(strength = 0.1)

# Basurero
r.scene.append( AABB(V3(-6, -3.5, -10), V3(3, 0.1, 5) , wall ) )
r.scene.append( AABB(V3(-7.5, -2.3, -10), V3(0.1, 2.5, 5) , wall ) )
r.scene.append( AABB(V3(-4.5, -2.3, -10), V3(0.1, 2.5, 5) , wall ) )
r.scene.append( AABB(V3(-6, -2.3, -7.4), V3(3, 2.5, 0.1) , wall ) )
r.scene.append( AABB(V3(-6, -2.3, -12.6), V3(3, 2.5, 0.1) , wall ) )

# Ventanas
r.scene.append( AABB(V3(7.7, 10, -25), V3(0.05, 15, 4.5) , refraxion ) )
r.scene.append( AABB(V3(8.1, 10, -18), V3(0.05, 15, 5.1) , refraxion ) )
r.scene.append( AABB(V3(8.5, 9.9, -13), V3(0.05, 15, 3.9) , refraxion ) )

# r.scene.append( Sphere(V3(-1.5, -1, -10), 2, reflexion) )
# r.scene.append( Sphere(V3(1.5, -1, -10), 2, refraxion) )


r.rtRender()

print('\ndary!—\n')

r.glFinish('proyecto.bmp')