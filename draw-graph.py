'''Создание и отображение графа'''

class Point():
    '''Точка на плоскости, имеет две координаты'''
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Linia():
    '''Прямая линия между двумя точками'''
    def __init__(self, point_in, point_out):
        self.point_in = point_in
        self.point_out = point_out

class Graph():
    '''Неориентированный граф, состоит из вершин и рёбер'''
    def __init__(self):
        self.verticles = {}
        self.edges = {}

    def letter_selection(self):
        '''Выбор буквы для новой вершины'''
        global ALPHABET
        # Перебираем все буквы алфавита
        for letter in ALPHABET:
            if not (letter in self.verticles.keys()):
                # Новая буква, её ещё нет в словаре вершин
                return letter # Отдаём её
        return None # Перебрали все буквы, свободной не нашли.

    def create_verticle(self, x, y):
        '''Добавляем в граф новую вершину'''
        
        new_letter = self.letter_selection(self)
        if new_letter == None:
            print('--- Невозможно содать вершину, все буквы заняты!!! ---')
        else:
            self.verticles[new_letter] = Point(x, y)

    def create_edge(self, verticle_first, verticle_second):
        '''Добавляем новое ребро'''
        # Проверяем на запрещённые петли
        if verticle_first == verticle_second:
            print('--- Для вершины', verticle_first,
                'нельзя создать петлю. Это запрещено! ---') 
            return None
        
        # Петли нет, упорядочиваем вершины по возрастанию
        if verticle_first < verticle_second:
            verticle_in, verticle_out = verticle_first, verticle_second
        else:
            # Переставляем вершины местами
            verticle_in, verticle_out = verticle_second, verticle_first
        
        # Проверяем вершины на существование
        if verticle_in in self.verticles.keys():
            # Вершина "ИЗ" существует, продолжаем проверки...
            if verticle_out in self.verticles.keys():
                # Вершина "В" существует, продолжаем проверку...
                if not (verticle_in in self.edges.keys()):
                    # Для вершины "ИЗ" еще нет ребер, добавляем справочник...
                    self.edges[verticle_in] = {}
                
                # Проверяем - не существует ли уже ребро?
                if not (verticle_out in self.edges.keys()):
                    # Такого ребра нет, создаем его!
                    self.edges[verticle_in][verticle_out] = None
                    return True
                else:
                    # Такое ребро уже есть, ничего не делаем!
                    return False
            else:
                print('--- Невозможно построить ребро в', verticle_out,
                    ', она не существует!!! ---')
                return False
        else:
            print('--- Невозможно построить ребро из', verticle_in,
                ', она не существует!!! ---')
            return False

def draw_circle(centre, radius, color):
    '''Рисуем окружность'''
    turtle.penup()
    turtle.goto(centre.x, (centre.y - radius))
    turtle.pendown()
    turtle.width(1)
    turtle.pencolor(color)
    turtle.circle(radius)
    turtle.penup()
    turtle.home()
    return None

def draw_segment(linia):
    '''Отрисовка отрезка'''
    turtle.penup()
    turtle.goto(linia.point_in.x, linia.point_in.y)
    turtle.pendown()
    turtle.goto(linia.point_out.x, linia.point_out.y)
    turtle.penup()
    return None

def calculate_and_draw_edge(graph, verticle_in, verticle_out, radius):
    '''Расчитываем координаты ребра и отбражаем его'''
    linia = Linia(Point(100, 100), Point(200, 200))
    draw_segment(linia)
    print('      Ребро из вершины', verticle_in, 'в', 
            verticle_out, 'нарисовано')
    return None

def draw_graph(graph):
    '''Рисование графа в два этапа: сначала вершины, потом рёбра'''
    radius = RADIUS
    color = 'black'
    
    # Сначала вершины....
    for verticle in graph.verticles.keys():
        draw_circle(graph.verticles[verticle], radius, color)
    print('   Вершины графа нарисованы')

    # Теперь связываем их рёбрами
    for verticle_in in graph.edges.keys():
        for verticle_out in graph.edges[verticle_in].keys():
            calculate_and_draw_edge(graph, verticle_in, verticle_out, radius)
    print('   Рёбра графа нарисованы')
    return None

import turtle, random, math
ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
WIDTH = 800
HEIGHT = 600
RADIUS = 20

def main():
    '''Организация алгоритма и вызов процедур'''
    # 1. Создаём граф
    graph = Graph()
    # 2. Отрисовываем граф 
    draw_graph(graph)
    print('Закончили работу')
    return None

if __name__ == '__main__':
    print('Запустили программу')
    main()
