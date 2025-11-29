import csv

with open("livros_recomendados.txt", "r", encoding="utf-8") as arq:
    livros = list(csv.reader(arq))

livros.sort(key=lambda x: float(x[3]), reverse=True)

print("\n LIVROS RECOMENDADOS:")
for ano, titulo, autor, nota, status in livros:
    print(f"{titulo} ({ano}) - {autor} → Nota: {nota}")