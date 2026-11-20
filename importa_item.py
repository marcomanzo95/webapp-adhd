"""Converte l'Excel con il testo delle domande ABAS-II in item_abas_genitore.json.

Uso: python importa_item.py ABAS_item_genitore.xlsx
Il JSON contiene materiale protetto da copyright dell'editore del test:
va tenuto solo in un repository privato.
"""
import json, sys
from openpyxl import load_workbook
from calcolatore_test import AREE_GENITORE

wb = load_workbook(sys.argv[1])
ws = wb["Item"]
dati = {sigla: [] for sigla, _, _, _ in AREE_GENITORE}
nomi = {nome: sigla for sigla, nome, _, _ in AREE_GENITORE}
for area, num, testo in ws.iter_rows(min_row=5, max_col=3, values_only=True):
    if area is None:
        continue
    sigla = nomi[area]
    if num != len(dati[sigla]) + 1:
        sys.exit(f"{area}: atteso item {len(dati[sigla]) + 1}, trovato {num}")
    if not testo or not str(testo).strip():
        sys.exit(f"{area}, item {num}: testo mancante")
    dati[sigla].append(" ".join(str(testo).split()))
for sigla, nome, _, n in AREE_GENITORE:
    if len(dati[sigla]) != n:
        sys.exit(f"{nome}: {len(dati[sigla])} item invece di {n}")
with open("item_abas_genitore.json", "w", encoding="utf-8") as f:
    json.dump(dati, f, ensure_ascii=False, indent=1)
print("item_abas_genitore.json scritto:", sum(len(v) for v in dati.values()), "item")
