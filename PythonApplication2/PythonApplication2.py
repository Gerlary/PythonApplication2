import pygame
from time import sleep
#maze pathfinder 
def path_find(f,curs1,curs2):
    global matrix_d
    global list_back
    global step
    global res_str
    start = curs1
    open = [curs1]
    closed = []
    matrix_back = {(start[0],start[1]): -1}
    end = curs2
    game = False
    if f == 1:
        while open != []:
            step+=1
            top = open[0]
            if top == end:
                print("путь найден!")
                game = True
                break
            open.pop(0)
            closed += [top]
           # matrix_d[(top[0],top[1])].reverse()
            for top_new in matrix_d[(top[0],top[1])]:
            
                if top_new not in open and top_new not in closed:
                    open =  [top_new] + open
                    matrix_back[(top_new[0],top_new[1])] = top
    else:
        while open != []:
            step+=1
            top = open[0]
            if top == end:
                print("путь найден!")
                game = True
                break
            open.pop(0)
            closed += [top]
        
            for top_new in matrix_d[(top[0],top[1])]:
            
                if top_new not in open and top_new not in closed:
                    open +=  [top_new] 
                    matrix_back[(top_new[0],top_new[1])] = top
    if game:
        print("Количество шагов: "+ str(step))
        list_back = list()
        while True:
            list_back.append(end)
            end = matrix_back[(end[0],end[1])]
            if end == start:
                list_back.append(end)
                break
       
        res_str = ""
        for i in range(len(list_back)-1):
         #   res_str += str([x+1 for x in list_back[i]]) + " -> "
         #   if i%10 == 0 :
        #        res_str += "\n"
            print (str([x+1 for x in list_back[i]]) + " -> ",end = "")
        print([x+1 for x in list_back[len(list_back)-1]])
        res_str += str([x+1 for x in list_back[len(list_back)-1]])
    else:
        res_str = "NO WAY!"
        print("NO WAY!")

    return

size_w = 900 
size_h = 700
SIZE = (size_w,size_h+200)

#Labitint
'''
1 1 1 1 1 1 1 1 1 1 1 1
1 0 0 1 0 1 1 1 0 0 0 1
1 1 0 1 0 0 0 1 0 1 0 1
1 1 0 1 0 1 0 1 0 1 0 1 
1 0 0 0 0 1 0 1 0 1 0 1
1 1 1 1 1 1 0 1 0 1 0 1
1 0 0 0 0 0 0 1 0 0 0 1
1 0 1 1 1 1 1 1 0 1 0 1
1 0 0 0 0 0 0 0 0 1 0 1
1 1 1 1 1 1 1 1 1 1 1 1
'''
matrix_l_def = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                [1, 0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 1],
                [1, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1],
                [1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 1, 0, 1, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1],
                [1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1],
                [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
                [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
matrix_l = list()
while True:
    print("Введите способ задания матрицы матрицы (0 - использовать дефолтную\n1-задать матрицу)")
    t = input()
    if t == '0':
        n,k = len(matrix_l_def),len(matrix_l_def[0])
        matrix_l = matrix_l_def
        break
    elif t == '1':
        print("Введите размерность матрицы MxN: ")
        n,k = map(int,input().split())
 
        for i in range(n):
            print("Введите {}-ю строку: ".format(i+1))
            inp = list(map(int,input().split()))
            matrix_l += [inp]   
        break
    else:
        print("Неверные вводимые данные!\n")



matrix_d = dict()
for i in range(n):
    for j in range(k):
        matrix_d[(i,j)] = []
        if matrix_l[i][j] == 0:

            if i !=0 :
                if matrix_l[i-1][j] == 0:
                    matrix_d[(i,j)] += [[i-1,j]]
            if j != 0:
                if matrix_l[i][j-1] == 0:
                    matrix_d[(i,j)] += [[i,j-1]]
            if i!= n-1:
                if matrix_l[i+1][j] == 0:
                    matrix_d[(i,j)] += [[i+1,j]]
            if j != k-1:
                if matrix_l[i][j+1] ==0:
                    matrix_d[(i,j)] += [[i,j+1]]
            
for i in matrix_l:
    print(i)
c = False
game = False
res_str = ""
list_back = []
step = 0
print("Выберите метод задания начальной и конечной координаты: (1- мышкой, 2- координатами)")
inp = int(input())
if inp == 2:
    print("Введите начальную точку:")
    start = [x-1 for x in list(map(int,input().split()))]

    print("Введите конечную точку:")
    end = [x-1 for x in list(map(int,input().split()))]
    
    open = [start]
    closed = list()
    step = 0
    matrix_back = {(start[0],start[1]): -1}
    print ("Выберите метод поиска(1- в глубину/ 2- в ширину)")
    f = int(input())

    if f == 1:
        while open != []:
            step+=1
            top = open[0]
            if top == end:
                print("путь найден!")
                game = True
                break
            open.pop(0)
            closed += [top]
            matrix_d[(top[0],top[1])].reverse()
            for top_new in matrix_d[(top[0],top[1])]:
            
                if top_new not in open and top_new not in closed:
                    open =  [top_new] + open
                    matrix_back[(top_new[0],top_new[1])] = top
    else:
        while open != []:
            step+=1
            top = open[0]
            if top == end:
                print("путь найден!")
                game = True
                break
            open.pop(0)
            closed += [top]
        
            for top_new in matrix_d[(top[0],top[1])]:
            
                if top_new not in open and top_new not in closed:
                    open +=  [top_new] 
                    matrix_back[(top_new[0],top_new[1])] = top
    if game:
        print("Количество шагов: "+ str(step))
        list_back = list()
        while True:
            list_back.append(end)
            end = matrix_back[(end[0],end[1])]
            if end == start:
                list_back.append(end)
                break
        list_back.reverse()
        res_str = ""
        for i in range(len(list_back)-1):
           # res_str += str([x+1 for x in list_back[i]]) + " -> "
           # if i%10 == 0 :
          #      res_str += "\n"
            print (str([x+1 for x in list_back[i]]) + " -> ",end = "")
        print([x+1 for x in list_back[len(list_back)-1]])
        res_str += str([x+1 for x in list_back[len(list_back)-1]])
    else:
        res_str = "NO WAY!"
        print("NO WAY!")
elif i ==1 :
    c = True
    game = True
    print ("Выберите метод поиска(1- в глубину/ 2- в ширину)")
    f = int(input())

screen = pygame.display.set_mode(SIZE)
pygame.font.init()

s_w = size_w/k
s_h = size_h/n
count = 0
f1 = pygame.font.Font(None, 25)
curs1 = [-1,-1]
curs2 = [-1,-1]
c = True
while game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if count != len(list_back) :
                     count += 1
            if event.key == pygame.K_LEFT:
                if count != 0 :
                     count -= 1
    if pygame.mouse.get_pressed()[0]:
        x,y = pygame.mouse.get_pos()
        for i in range(n):
            for j in range(k):
                
                if s_w*j<x <s_w*(j+1) and s_h*i <y <s_h*(i+1):
                    if curs1 == [-1,-1]:
                        curs1 = [i,j]
                        break
                    elif curs2 == [-1,-1]:
                        curs2 = [i,j]
                        break

    if curs1 !=[-1,-1] and curs2 != [-1,-1]and c:
        c = False
        path_find(f,curs1,curs2)
        list_back.reverse()
    screen.fill((255,255,255))
    for i in range(n):
        for j in range(k):
            if matrix_l[i][j] == 1:
                pygame.draw.polygon(screen ,[0,0,0],[[s_w*(j+1),s_h*i],[s_w*(j+1),s_h*(i+1)],[s_w*j,s_h*(i+1)],[s_w*j,s_h*i]])
            else:
                 pygame.draw.polygon(screen ,[255,255,255],[[s_w*j,s_h*i],[s_w*(j+1),s_h*i],[s_w*(j+1),s_h*(i+1)],[s_w*j,s_h*(i+1)]])
    for i in range(count):
        pygame.draw.polygon(screen,[255,178,139],[[s_w*list_back[i][1],s_h*list_back[i][0]],[s_w*(list_back[i][1]+1),s_h*list_back[i][0]],[s_w*(list_back[i][1]+1),s_h*(list_back[i][0]+1)],[s_w*list_back[i][1],s_h*(list_back[i][0]+1)]])
    naves1 = f1.render("Количество шагов : {}".format(step), True, [0,0,0])
    naves = f1.render(res_str, True, [0,0,0])
    screen.blit(naves,(int(0),int(700)))
    screen.blit(naves1,(int(0),int(750)))
    pygame.display.flip()
    sleep(0.2)


pygame.quit()
