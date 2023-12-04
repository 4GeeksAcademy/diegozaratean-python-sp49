# Js ==>. py
# // ==> #
# console.log('hola') ===> print('hola')
# print('hola')
# # generoPelicula ===> genero_pelicula
# # integer string boolenanos ===> integer string boolenanos
# # true ===> True
# # undefine, null ===> none
# # array ====> Listas , Tuplas
# # Objetos =====> diccionarios

# last_name = 'zarate'
# edad = 38
# name = 'diego'
# esta_vivo = True

# print(name)

# print(name , last_name)
# print(name + last_name)
# print('Hola mi nombre es',name , last_name)
# # cast   int(). str()
# print('Hola mi edad es ' + str(edad))
# segundo_numero = '3'
# print(edad + int(segundo_numero))

# # declariacion de un diccionario
# # js const objeto ={}
# persona = {
#     "nombre" : 'diego',
#     "apellido" : 'zarate',
#     'edad' : 38
# }

# print(persona)
# print(persona['nombre'])

# # declaracion de una lista
# # js const array = [element1, elemento 2]
# skills = ['js','react','python']
# print(skills)
# print(len(skills))
# skills.append('css')
# print(skills)
# print(len(skills))

# #declaraion de Tupla
# dias_semana = ('lunes','martes','miercoles','jueves','viernes','sabado','domingo')
# print(dias_semana)


# Map ===> Lambda
people_list = [{'name':'Santiago'},{'name':'Diego'},{'name':'Johana'}]
# # js array.map( (item)=> funcion que se ejecuta sobre item )
# # python map(lambda item: funcion que se ejecuta sobre item  , array)
# resultado = map(lambda objeto: objeto['name'] ,people_list)
# # resultado = ['Santiago','Diego','Johana']
# print(resultado)
# print(list(resultado))

# frutas = ['uva','mandarina','sandia','maracuya']
# print(frutas)

# frutas_plural = map(lambda fruta: fruta + 's',frutas)
# print(frutas_plural)
# print(list(frutas_plural))


# funciones
#console.log('donde estoy')
# function imprimir(){
# 
#}
#console.log('donde estoy')

# def imprimir():
#     print('donde estoy')

#     print(1)
#     print(2)
#     print(3)
# print(4)
# print(5)

# imprimir()



# def saludar(nombre):
#     print('hola ' + nombre)

# saludar('marta')
# saludar('gabriel')

# procesos iterativos / bucles / loops
# colores = ['azul','rojo','verde','blanco']
# for color in colores:
#     print(color)


# if / else
# edad = 81
# if edad < 18:
#     print('No puedes tomar vino')
# elif edad > 80:
#     print('puedes tomar vino, pero no deberias')
# else:
#     print('puedes tomar vino')

# class
class Carro:

    def __init__(self,modelo, potencia, marca):
        self.modelo = modelo
        self.potencia = potencia
        self.marca = marca

    def serialize(self):
        return {
            'modelo': self.modelo,
            'marca': self.marca,
            'nombre': self.marca + '-'+self.modelo,
            'calificación': 5,
        }

    
carro_pascual = Carro('fiesta', 140, 'ford')
print(carro_pascual.modelo)
print(carro_pascual.potencia)
print(carro_pascual.marca)

print(carro_pascual)


print(carro_pascual.serialize())


# soltero 
# virtudes, hobbies, defectos , historial_amoroso
class Soltero:

    def __init__(self, virtudes, hobbies, defectos , historial_amoroso):
        self.virtudes = virtudes
        self.hobbies = hobbies
        self.defectos = defectos
        self.historial_amoroso = historial_amoroso

    def serialize(self):
        return {
            'virtudes': self.virtudes,
            'hobbies': self.hobbies,
            'defectos': self.defectos,
       
        }

felipe = Soltero('Guapo, juicioso, millonario, divertido', 'golf, padel, navegar', 'celoso, toxico, posesivo, egocentrico, avaricioso','3 matrimonios, 15 realciones fallidas, 48 amantes, una demanda en el juzgado')
print(felipe.serialize())


# paquetes
# Js npm ===> package.json
# Python pip ===> pipfile
# Python pipenv ===> pipfile