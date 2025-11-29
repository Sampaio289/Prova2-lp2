import csv

with open("livros_avaliacao.txt", "r", encoding="utf-8") as arq:
    livros = list(csv.reader(arq))

filtrados = [liv for liv in livros if liv[4] in ("lido", "lendo")]

filtrados.sort(key=lambda x: float(x[3]), reverse=True)

top5 = filtrados[:5]

with open("livros_recomendados.txt", "w", encoding="utf-8", newline="") as saida:
    writer = csv.writer(saida)
    writer.writerows(top5)

print(" Arquivo 'livros_recomendados.txt' criado com sucesso!")
