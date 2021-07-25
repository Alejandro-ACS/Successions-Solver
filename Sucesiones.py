from selenium import webdriver

import time

import os

sucesion = list(input("Enter the sucesion: ").split(" "))

resultados = []

respuestas = []

operacion = []

operacionE = None

'''

def comprobar(x):

    for y in range(x):

        print("(n - " + str(y + 1) + ")", end=" · ")

        operacionE = operacionE + "(n - " + str(y + 1) + ")"

def calcular(x):

    for z in range(x):

        for y in range(z+1):

            resultados.append((x+1)-(y+1))

def impr(x):

    for z in range(x):

        a = []

        for y in range(z):

            for b in range(y+1):

                a.append(resultados[b])
            
            result = np.prod(np.array(a)) * int(sucesion[y+1])

            respuestas.append(result)

    return np.sum(np.array(respuestas) + int(sucesion[0]))

def operar(x):

    global operacion

    c = x + 1

    operacion = int(sucesion[0]) + ((c + 1 - 1) * (int(sucesion[c-1]) - int(sucesion[c-2]))) + ((c + 1- 1) * (c + 1- 2))

    operacionE = sucesion[0] + "(n - 1) · " + str(int(sucesion[c-1]) - int(sucesion[c-2])) + " + (n - 1) · (n - 2)"

if len(sucesion) >= 2:

    for x in range(len(sucesion)):

        if x == 0:

            print(sucesion[x], end=" + ")
        
        elif x == 1:

            comprobar(x)

            print(str(int(sucesion[x]) - int(sucesion[x-1])), end=" + ")

            operar(x)
        
        else:

            comprobar(x)

            calcular(x)

            result = float(impr(x)/(0-float(operacion)))

            if x == len(sucesion) - 1:

                print(result, end="")
            
            else:

                print(result, end=" + ")

            operacion = (0-float(operacion)) + float(resultados[len(resultados)-1] - float(sucesion[x - 1]))

'''

def comprobar(x):

    global operacionE

    for y in range(x):

        if y == x:

            operacionE = operacionE + "(n - " + str(y + 1) + ") + "

        else: 

            operacionE = operacionE + "(n - " + str(y + 1) + ") · "

def calcular(x):

    for z in range(x):

        for y in range(z+1):

            resultados.append((x+1)-(y+1))

def simplificar():

    browser.get("https://es.symbolab.com/solver/step-by-step/" + str(operacionE))

    validars()

    try:

        simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[8]/div[2]/span').text

    except:

        try:

            simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[8]/div[2]/div/span').text
        
        except:

            try:

                simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[7]/div[2]/span').text

            except:

                try:

                    simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[7]/div[2]/div/span').text

                except:

                    try:

                        simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[6]/div[2]/span').text

                    except:

                        try:

                            simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[6]/div[2]/div/span').text
                        
                        except:

                            try:

                                simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[5]/div[2]/span').text

                            except:

                                try:

                                    simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[5]/div[2]/div/span').text
                                
                                except:

                                    try:

                                        simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[4]/div[2]/span').text

                                    except:

                                        simplificar = browser.find_element_by_xpath('//*[@id="steps-container"]/li[4]/div[2]/div/span').text

    simplificar = simplificar[1:]

    if "\n" in simplificar:

        simplificar = list(simplificar.split("\n"))

        if len(simplificar)/4 == 1:

            simplificar[3] = simplificar[3][1:]

            simplificar = simplificar[0] + "((" + simplificar[1] + ")÷(" + simplificar[2] + "))" + simplificar[3]
        
        elif len(simplificar)/3 == 2:

            simplificar[3] = simplificar[3][1:]

            simplificar = simplificar[0] + "((" + simplificar[1] + ")÷(" + simplificar[2] + "))" + "((" + simplificar[3] + ")÷(" + simplificar[4] + "))" + simplificar[5]

    print(simplificar)

def validars():

    while True:

        try:

            element = browser.find_element_by_xpath('//*[@id="multipleSolutions"]/div[2]')

            if element:

                break
        
        except:

            time.sleep(1)

def operar(x):

    global operacion, operacionE

    c = x + 1

    operacion = int(sucesion[0]) + ((c + 1 - 1) * (int(sucesion[c-1]) - int(sucesion[c-2]))) + ((c + 1- 1) * (c + 1- 2))

    operacionE = sucesion[0] + " + (n - 1) · " + str(int(sucesion[c-1]) - int(sucesion[c-2])) + " + "

if len(sucesion) >= 2:

    browser = browser = webdriver.Chrome(executable_path="./whatsappbot/chromedriver")

    for x in range(len(sucesion)):

        if x == 0:
            
            print("", end="")
        
        elif x == 1:
            
            operar(x)
        
        else:

            comprobar(x)

            calcular(x)

            browser.get("https://es.symbolab.com/solver/step-by-step/" + str(operacionE) + "x = " + sucesion[x] + ", n = " + str(x + 1))

            validars()

            try:

                solution = browser.find_element_by_xpath('//*[@id="steps-container"]/li[8]/div[2]/span').text
            
            except:

                try:

                    solution = browser.find_element_by_xpath('//*[@id="steps-container"]/li[7]/div[2]/span').text
                
                except:

                    try:

                        solution = browser.find_element_by_xpath('//*[@id="steps-container"]/li[6]/div[2]/span').text
                    
                    except:

                        try:

                            solution = browser.find_element_by_xpath('//*[@id="steps-container"]/li[5]/div[2]/span').text

                        except:

                            solution = browser.find_element_by_xpath('//*[@id="steps-container"]/li[4]/div[2]/span').text

            characters = "x=n,"

            solution = ''.join( i for i in solution if i not in characters)

            if "\n" in solution:

                solution = list(solution.split("\n"))

                solution = "((" + solution[1] + ") ÷ (" + solution[2] + "))"

            else:

                solution = solution[:-2]

            if x == len(sucesion) - 1:

                operacionE = operacionE + str(solution)
            
            else: 

                operacionE = operacionE + str(solution) + " + "
            
            os.system("cls")

print(operacionE)

simplificar()