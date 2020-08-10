import turtle
import time
import random

posponer = 0.1
wn = turtle.Screen()
wn.title("Quetzalcoatl's Game")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0)


# Funciones
def mov():
	"""
	Funcion que se encarga de darle movimiento a la serpiente.

	"""
	if cabeza.direction == "up": 
		cabeza.sety(cabeza.ycor() + 20)
	elif cabeza.direction == "down":
		cabeza.sety(cabeza.ycor() - 20)
	elif cabeza.direction == "right":
		cabeza.setx(cabeza.xcor() + 20)
	elif cabeza.direction == "left":
		cabeza.setx(cabeza.xcor() - 20)

def arriba():
	"""
	Mueve la serpiente hacia arriba
	
	"""
	cabeza.direction = "up"

def abajo():
	"""
	Mueve la serpiente hacia abajo
	
	"""
	cabeza.direction = "down"

def izq():
	"""
	Mueve la serpiente hacia la izquierda
	
	"""
	cabeza.direction = "left"

def der():
	"""
	Mueve la serpiente hacia la derecha
	
	"""
	cabeza.direction = "right"



# Cabeza de la serpiente
cabeza = turtle.Turtle()
cabeza.speed(0)
cabeza.shape("square")
cabeza.penup()
cabeza.goto(0, 0)
cabeza.direction = "stop"
cabeza.color("green")

# Cuerpo de la serpiente
segmentos = []

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.penup()
comida.goto(random.randint(-280, 280), random.randint(-280, 280))
comida.color("red")





# Teclado

wn.listen()
# Aqui Up con mayuscula para especificar la tecla
wn.onkeypress(arriba, "Up") 
wn.onkeypress(abajo, "Down") 
wn.onkeypress(izq, "Left") 
wn.onkeypress(der, "Right") 




while True:
	wn.update()


	if cabeza.distance(comida) < 20:
		x = random.randint(-280, 280)
		y = random.randint(-280, 280)
		comida.goto(x, y)

		nuevo_segmento = turtle.Turtle()
		nuevo_segmento.speed(0)
		nuevo_segmento.shape("square")
		nuevo_segmento.penup()
		nuevo_segmento.goto(0, 0)
		nuevo_segmento.direction = "stop"
		nuevo_segmento.color("grey")
		segmentos.append(nuevo_segmento)

	# Movimiento del cuerpo de la serpiente
	totalSeg = len(segmentos)
	for index in range(totalSeg-1, 0, -1):
		x = segmentos[index-1].xcor()
		y = segmentos[index-1].ycor()
		segmentos[index].goto(x, y)
	if totalSeg > 0:
		segmentos[0].goto(cabeza.xcor(), cabeza.ycor())

	# Colision con bordes
	if cabeza.xcor() > 280 or cabeza.xcor() < -280 or cabeza.ycor() > 280 or cabeza.ycor() < -280:
		time.sleep(1)
		cabeza.goto(0,0)
		cabeza.direction = "stop"
		# Escondemos el cuerpo de la serpiente
		for segmento in segmentos:
			segmento.goto(1000, 1000)		

		# Limpiamos la lista del cuerpo de la serpinte
		segmentos.clear()



	mov()
	time.sleep(posponer)

#turtle.done()