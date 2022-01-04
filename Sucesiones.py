sucesion = list(input("Enter the sucesion: ").split(" "))

equis = []

equis_p = []

formula = ""

# ------------ Arreglar lista (sucesion) ------------ #

for d in range(len(sucesion)):

    if not '.' in sucesion[d]:

        sucesion[d] = int(sucesion[d])
    
    else:

        sucesion[d] = float(sucesion[d])

# ------------ Fin arreglar lista ------------ #

# ------------ Imprimir formula ------------ #

def print_form(bool, termino):

    global formula

    for c in range(len(termino)):

            if c == len(termino)-1:

                if bool:

                    formula += str(termino[c]) + "+"
                
                else:

                    formula += str(termino[c])
            
            else:

                formula += str(termino[c]) + "·"
    
    return formula

def imprimir_formula(sucesion):

    for b in range(len(sucesion)):

        termino = numero_a_añadir(b+1)

        if b != len(sucesion)-1:

            print_form(True, termino)
        
        else:

            print_form(False, termino)

    return formula

# ------------ Fin imprimir formula ------------ #

# ------------ Generatriz ------------ #

def sacar_parte_decimal(numero):

    numero = str(numero).split(".")

    del numero[0]

    return numero[0]

def sacar_parte_entera(numero):

    numero = str(numero).split(".")

    return int(numero[0])

def identificar_periodo(decimal):

    decimal = str(decimal)

    for x in range(len(decimal)-1):

        if decimal[len(decimal)-1-x] != decimal[len(decimal)-1-(x+1)]:

            return len(decimal)-1-x
    
    return 0
        
def calcular_generatriz(numero):

    rangoI = identificar_periodo(sacar_parte_decimal(numero))

    numero1 = sacar_parte_entera(numero*(10**(rangoI+1)))

    numero2 = sacar_parte_entera(numero*(10**rangoI))

    numerador = numero1-numero2

    denominador = (10**(rangoI+1))-(10**rangoI)

    return numerador, denominador

# ------------ Fin generatriz ------------ #

# ------------ Funciones sucesión ------------ #

def numero_a_añadir(rango):

    añadir = []

    if type(equis_p[rango-1]) == str:

        añadir.append("(" + equis_p[rango-1] + ")")

    elif equis_p[rango-1] >= 0:

        añadir.append(str(equis_p[rango-1]))
    
    else:

        añadir.append("(" + str(equis_p[rango-1]) + ")")

    for x in range(rango-1):

        añadir.append('(n-' + str(x+1) + ')')
    
    return añadir

def numero_a_calcular_1_m(rango, equis, n):

    total = equis[rango-1]

    for x in range(rango-1):

        total = total*(n-(x+1))
    
    return total

def numero_a_calcular_1_sum(rango, equis):

    total = 0

    for x in range(rango-1):

        total += numero_a_calcular_1_m(x+1, equis, rango)

    return total

def numero_a_calcular_2(rango):

    total = 1

    n = rango

    for x in range(rango-1):

        total = total*(n-(x+1))
    
    return total

# ------------ Fin funciones sucesión ------------ #

def main():

    for a in range(len(sucesion)):

        if a == 0:

            equis.append(sucesion[0])

            equis_p.append(sucesion[0])
        
        else:

            total_anterior = numero_a_calcular_1_sum(a+1, equis)

            total_posterior = numero_a_calcular_2(a+1)

            numero = (sucesion[a]-total_anterior)/total_posterior

            if numero == int(numero):

                equis.append(int(numero))

                equis_p.append(int(numero))
            
            else:

                equis.append(numero)

                decimal = sacar_parte_decimal(numero)

                if len(decimal) > 5:

                    if decimal[len(decimal)-2] != decimal[len(decimal)-3]:

                        equis_p.append(numero)
                    
                    else:

                        equis_p.append(str(calcular_generatriz(float(str(numero)[:-1]))[0])+"/"+str(calcular_generatriz(float(str(numero)[:-1]))[1]))
                    
                else:

                    equis_p.append(numero)

                    

    return imprimir_formula(sucesion)

print(main())
