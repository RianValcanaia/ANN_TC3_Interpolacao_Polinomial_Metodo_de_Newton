from sympy import symbols, expand, lambdify, simplify
import matplotlib.pyplot as plt
import numpy as np

def plot_dispersao(pontos, polinomio, valor):
    xs = [p[0] for p in pontos]
    ys = [p[1] for p in pontos]

    xmin, xmax = min(xs), max(xs)
    margem = (xmax - xmin) * 0.1
    xmin -= margem
    xmax += margem

    x_plot = np.linspace(xmin, xmax, len(pontos)*50)
    y_plot = polinomio(x_plot)

    plt.figure(figsize=(8, 5))
    plt.plot(x_plot, y_plot, label='Polinômio interpolador', color='blue')
    plt.scatter(xs, ys, color='red', label='Pontos dados')

    if valor is not None:
        y_valor = polinomio(valor)
        plt.scatter([valor], [y_valor], color='green', marker='o', s=80, label=f'Ponto estimado ({valor:.2f}, {y_valor:.3f})')

    plt.title('Interpolação Polinomial de Newton')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.show()


def diferencas_divididas(pontos):
    tam = len(pontos)
    dd = [[0 for _ in range(tam)] for _ in range(tam)]

    for i in range(tam):
        dd[i][0] = pontos[i][1]

    for j in range(1, tam):
        for i in range (tam - j):
            num = dd[i+1][j-1] - dd[i][j-1]
            den = pontos[i+j][0] - pontos[i][0]
            dd[i][j] = num/den
    
    return dd

def selecionar_pontos_proximos(valor, pontos, grau):
    dist_e_ponto = []

    for ponto in pontos:
        distancia = abs(ponto[0] - valor)
        dist_e_ponto.append((distancia, ponto))
    
    dist_e_ponto.sort(key=lambda x:x[0])

    pontos_proximos = [p[1] for p in dist_e_ponto[:grau+1]]

    pontos_proximos.sort(key=lambda p:p[0])

    return pontos_proximos

def polinomio_newton(valor, pontos, grau):
    global x  
    tam = len(pontos)

    pontos_proximos = selecionar_pontos_proximos(valor, pontos, grau)
    dd = diferencas_divididas(pontos_proximos)
    coef = [dd[0][j] for j in range(grau + 1)]
    pol = coef[0]
    termo = 1

    for i in range(1, grau+1):
        termo *= (x - pontos_proximos[i-1][0])
        pol += coef[i] * termo
    
    return pol

def estimativa_erro(valor, pontos, dd, erro_max):
    print("============ Estimativa de erro ============\n")
    tam = len(pontos)

    melhor_grau = -1

    for grau in range(1, tam-1):
        pontos_proximos = selecionar_pontos_proximos(valor, pontos, grau)
        print(f"|E{grau}(x)| = |", end='')
        produto = 1
        for i in range(grau+1):
            print(f"({valor} - {pontos_proximos[i][0]})", end='')
            produto *= (valor-pontos_proximos[i][0])
        
        dd_max = max(abs(dd[i][grau+1]) for i in range(tam - grau))

        erro_estimado = abs(produto * dd_max)
        print("| * {:.6f}".format(dd_max), end='')
        print(" = {:.6f}".format(erro_estimado))
    
        if erro_estimado < erro_max and melhor_grau == -1:
            melhor_grau = grau
    
    if melhor_grau == -1: melhor_grau = tam-2

    return melhor_grau

def printaDD(dd):
    print("============ Tabela Diferenças Divididas ============\n")
    for i in range(0,len(dd)): print(f"    Ordem {i} ", end='')
    print()
    for i in range(len(dd)+1):
        for j in range (len(dd) -i):
            if dd[i][j] < 0: print("| {:.6f} ".format(dd[i][j]), end='')
            else: print("|  {:.6f} ".format(dd[i][j]), end='')
        print()

# ======= main =======
x = symbols('x')  
pontos = [(0, -2.78), (0.5, -2.241), (1, -1.65), (1.5, -0.594), (2, 1.34), (2.5, 4.564)]
valor = 1.23
erro_max = 10**-3

dd = diferencas_divididas(pontos)
printaDD(dd)
melhor_grau = estimativa_erro(valor, pontos, dd, erro_max)
pol_expr = simplify(polinomio_newton(valor, pontos, melhor_grau))
pol = lambdify(x, pol_expr)


print("\n============ Resultados ============\n")
print(f"Melhor polinômio = P{melhor_grau}(x)")
print(f"P{melhor_grau}(x) = {pol_expr}")
print(f"f({valor}) ≈ P{melhor_grau}({valor}) ≈ {pol(valor)}\n\n") 
plot_dispersao(pontos, pol, valor)