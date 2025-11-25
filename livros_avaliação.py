import csv

with open('livros.txt', 'r' ) as lv:
    livros = [linha.strip().split(', ') for linha in lv if linha.strip()]

avaliacoes = []

for ano, titulo, altor in livros:
    while True:
        try:
            nota = float(input(f"Digite uma nota de 0 a 10 para '{titulo}':"))
            
            if 0 <= nota <= 10:
                avaliacoes.append([ano, titulo, altor, nota])
                break  
            else:
                print("  Nota inválida! Digite um número entre 0 e 10.")
        except ValueError:
            print(" Entrada inválida! Digite apenas números.")


with open('livros_avaliacao.csv', 'w', newline='', encoding='utf-8') as lv:
    writer = csv.writer(lv)
    writer.writerow(['Ano','livros','Nota'])
    writer.writerows(avaliacoes)

print("\n Avaliações salvas com sucesso no arquivo 'livros_avaliacao.csv'!")