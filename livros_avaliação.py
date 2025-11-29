import csv

with open("livros.txt", "r", encoding="utf-8") as arq:
    livros = list(csv.reader(arq))

resultado = []

for livro in livros:
    ano, titulo, autor = livro

    while True:
        try:
            nota = float(input(f"Digite a nota para '{titulo}': "))
            if 0 <= nota <= 10:
                break
            else:
                print("A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

    while True:
        status = input(f"Status de leitura para '{titulo}' (lido / lendo / na fila): ").strip().lower()
        if status in ("lido", "lendo", "na fila"):
            break
        else:
            print("Status inválido. Digite exatamente: lido, lendo ou na fila.")

    resultado.append([ano, titulo, autor, nota, status])

with open("livros_avaliacao.txt", "w", encoding="utf-8", newline="") as saida:
    writer = csv.writer(saida)
    writer.writerows(resultado)

print("\n Arquivo 'livros_avaliacao.txt' criado com sucesso!")
