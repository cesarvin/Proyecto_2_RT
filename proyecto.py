from gl import Raytracer, color, V2, V3
from obj import Obj, Texture, Envmap
from sphere import *
import random

basurero = Material(diffuse = color( 0.49, 0.67, 0.48 ), spec = 16)
caja = Material(diffuse= color( 0.62, 0, 0.68 ),texture = Texture('box.bmp'), matType = OPAQUE)
caja1 = Material(diffuse= color( 0.66, 0.84, 0.67 ),texture = Texture('box.bmp'), spec = 16)
caja2 = Material(diffuse = color(0.4, 0.35, 0.35 ),texture = Texture('box.bmp'), spec = 16)
caja3 = Material(diffuse = color(0.4, 0.69, 0.8 ),texture = Texture('box.bmp'), spec = 32)
newsp = Material(diffuse = color(0.7, 0.69, 0.8 ),texture = Texture('newspaper.bmp'), spec = 32)
graffiti = Material(texture = Texture('graffiti.bmp'), spec = 32)
reflexion = Material(spec = 64, matType = REFLECTIVE)
refraxion = Material(spec = 64, ior = 2.5, matType= TRANSPARENT) 




width = 500
height = 250
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

# # Basurero
r.scene.append( AABB(V3(-6, -3.5, -10), V3(3, 0.1, 5) , basurero ) )
r.scene.append( AABB(V3(-7.5, -2.3, -10), V3(0.1, 2.5, 5) , basurero ) )
r.scene.append( AABB(V3(-4.5, -2.3, -10), V3(0.1, 2.5, 5) , basurero ) )
r.scene.append( AABB(V3(-6, -2.3, -7.4), V3(3, 2.5, 0.1) , basurero ) )
r.scene.append( AABB(V3(-6, -2.3, -12.6), V3(3, 2.5, 0.1) , basurero ) )

# # Ventanas
r.scene.append( AABB(V3(7.7, 10, -25), V3(0.05, 15, 4.5) , newsp ) )
r.scene.append( AABB(V3(8.1, 10, -18), V3(0.05, 15, 5.1) , newsp) )
r.scene.append( AABB(V3(8.5, 9.9, -13), V3(0.05, 15, 3.9) , newsp ) )

#grafitty
r.scene.append( AABB(V3(-7.7, 5, -20), V3(0.05, 15, 20) , graffiti ) )

# # Esferas 
r.scene.append( Sphere(V3(10, -6, -25), 3, reflexion) )
r.scene.append( Sphere(V3(10, -6, -15), 3, refraxion) )

# cajas
r.scene.append( AABB(V3(-6, -1.5, -10), V3(2, 2, 2), caja ) )
r.scene.append( AABB(V3(5, -3, -25), V3(5, 5, 5), caja2 ) )
r.scene.append( AABB(V3(5, 0.5, -25), V3(2, 2, 2), caja3 ) )
r.scene.append( AABB(V3(-6, -3, -50), V3(10, 10, 10), caja2 ) )
r.scene.append( AABB(V3(0, -3, -7), V3(1, 1, 1), caja2 ) )
r.scene.append( AABB(V3(0, -3, -10), V3(1, 1, 1), caja3 ) )

r.rtRender()

print('\ndary!—\n')

r.glFinish('proyecto.bmp')