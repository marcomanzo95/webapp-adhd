"""Genera tabelle_abas.py dal file Excel compilato a mano (unica fonte dei dati normativi)."""
import sys, pprint
from openpyxl import load_workbook
wb=load_workbook(sys.argv[1]); out=sys.argv[2]
# Tavole lette da Claude dalle scansioni e non ancora confrontate col cartaceo da un clinico.
# Quando sono state verificate, rigenerare con: python export_tables.py file.xlsx tabelle_abas.py --verificate
DA_CONFERMARE = [] if "--verificate" in sys.argv else ["A12", "A9", "A10_GAC_DAC_DAS"]
def parse(v):
    if v is None: return None
    s=str(v).strip().replace(" ","")
    if s in ("","-","–","nonpresente"): return None
    if "-" in s: a,b=s.split("-"); return (int(a),int(b))
    return (int(float(s)),int(float(s)))
def comp_sheet(name,colmap):
    ws=wb[name]; hdr=[c.value for c in ws[4]]; res={k:{} for k in colmap.values()}
    for r in range(5,86):
        comp=ws.cell(r,1).value
        if not isinstance(comp,int): continue
        for h,k in colmap.items():
            p=parse(ws.cell(r,hdr.index(h)+1).value)
            if p: res[k][comp]=p
    return res
def raw_sheet(name,keys):
    ws=wb[name]; hdr=[c.value for c in ws[4]]; res={k:{} for k in keys}
    for r in range(5,20):
        pp=ws.cell(r,1).value
        for j,k in enumerate(keys,2):
            p=parse(ws.cell(r,j).value)
            if p: res[k][pp]=p
    return res
A13C={"GAC senza Lavoro":"gac_sl","GAC con Lavoro":"gac_cl","DAC":"dac","DAS":"das","DAP senza Lavoro":"dap_sl","DAP con Lavoro":"dap_cl"}
BANDS=["16-21","22-29","30-39","40-49","50-64","65-74"]
D={}
D["A13"]={b:comp_sheet(f"A13_{b}",A13C) for b in BANDS}
D["A2"]=comp_sheet("A2_Insegnante",{"GAC":"gac","DAC":"dac","DAS":"das","DAP":"dap"})
D["A6"]=comp_sheet("A6_Genitore",{"GAC":"gac","DAC":"dac","DAS":"das","DAP":"dap"})
d=comp_sheet("A10_DAP",{f"{b} DAP {x}.":f"{b}|{k}" for b in BANDS for x,k in (("senza Lav","dap_sl"),("con Lav","dap_cl"))}|{"75-89 DAP":"75-89|dap"})
A10={}
for k,v in d.items(): b,c=k.split("|"); A10.setdefault(b,{})[c]=v
SUBS=["co","am","sco","vc","ss","tl","cur","ac","soc","lav"]
def filled(n): 
    ws=wb[n]; return sum(1 for row in ws.iter_rows(min_row=5,values_only=True) for v in row[1:] if v not in (None,""))
for b in BANDS+["75-89"]:
    n=f"A10_{b}"
    if n in wb.sheetnames and filled(n)>0:
        cols={"GAC senza Lavoro":"gac_sl","GAC con Lavoro":"gac_cl","DAC":"dac","DAS":"das"} if b!="75-89" else {"GAC":"gac","DAC":"dac","DAS":"das"}
        A10[b].update(comp_sheet(n,cols))
D["A10"]=A10
D["A12"]={b:raw_sheet(f"A12_{b}",SUBS) for b in BANDS if f"A12_{b}" in wb.sheetnames and filled(f"A12_{b}")>0}
D["A9"]={b:raw_sheet(f"A9_{b}",SUBS if b!="75-89" else SUBS[:-1]) for b in BANDS+["75-89"] if f"A9_{b}" in wb.sheetnames and filled(f"A9_{b}")>0}
IC={}
wsic=wb["Intervalli_confidenza"]
for row in wsic.iter_rows(min_row=5,values_only=True):
    if not row[0]: continue
    tav=row[0].replace(".",""); fascia=row[1]; liv=row[2].replace("%","")
    unica = tav in ("A2","A6") or fascia=="75-89"
    cols=["gac","gac_cl","dac","das","dap","dap_cl"] if unica else ["gac_sl","gac_cl","dac","das","dap_sl","dap_cl"]
    d={c:int(v) for c,v in zip(cols,row[3:9]) if v not in (None,"-")}
    IC.setdefault(f"{tav}|{fascia}",{})[liv]=d
D["IC"]=IC
P={}
for r in wb["Percentili"].iter_rows(min_row=5,max_row=85,values_only=True):
    if isinstance(r[0],int): P[r[0]]=str(r[1])
D["PERCENTILI"]=P
with open(out,"w",encoding="utf-8") as f:
    f.write('"""Tavole normative ABAS-II (edizione italiana), trascritte a mano dal manuale.\n\n'
            'File generato automaticamente da export_tables.py a partire da ABAS_tabelle_da_compilare.xlsx.\n'
            'Non modificare a mano: correggere l\'Excel e rigenerare.\n'
            'Formato: tabelle compositi {colonna: {composito: (somma_min, somma_max)}};\n'
            'tabelle grezzi {sottoscala: {Pp: (grezzo_min, grezzo_max)}}.\n"""\n\n')
    for k,v in D.items(): f.write(f"{k} = "+pprint.pformat(v,width=110,sort_dicts=True)+"\n\n")
    f.write(f"DA_CONFERMARE = {DA_CONFERMARE!r}\n")
print({k:(list(v.keys()) if isinstance(v,dict) else '') for k,v in D.items() if k!="PERCENTILI"})
