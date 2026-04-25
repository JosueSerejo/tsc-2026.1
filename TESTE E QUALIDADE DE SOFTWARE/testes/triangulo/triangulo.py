#Elabore um algoritmo que verifica se trÊs valores dados foram um triangulo. Informa ainda se triangulo é equilatero, isósceles ou escaleno.
#Crie um arquivo de teste automatizados para testar um conjunto de casos de teste.

# def e_triangulo(a, b, c):
  #  return (
   #     a > 0 and 
    #    b > 0 and 
     #   c > 0 and
      ### b + c > a
    #)

def triangulo_equilatero(a, b, c):
    return a == b == c

def triangulo_isoceles(a, b, c):
    return (a == b and a != c) or (a == c and a != b) or (b == c and b != a)

def triangulo_escaleno(a, b, c):
    return a != b and a != c and b != c

def nao_e_triangulo(a, b, c):
    return (
        a <= 0 or 
        b <= 0 or 
        c <= 0 or
        a + b <= c or 
        a + c <= b or 
        b + c <= a
    )