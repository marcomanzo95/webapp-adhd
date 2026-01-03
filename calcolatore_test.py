# File: calcolatore_test.py

def calcola_asrs(risposte_parte_a):
    punteggio_positivo = sum(1 for r in risposte_parte_a if r >= 2)
    if punteggio_positivo >= 4:
        risultato = "Positivo (suggerisce approfondimento diagnostico)"
    else:
        risultato = "Negativo"
    return {'risultato': risultato, 'punteggio_positivo': punteggio_positivo}

def calcola_wurs(risposte):
    item_da_sommare = [3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 20, 21, 24, 25, 26, 27, 28, 29, 40, 41, 51, 56, 59]
    punteggio_totale = sum(risposte[i-1] for i in item_da_sommare)
    if punteggio_totale >= 46:
        risultato = "Positivo (punteggio >= 46)"
    else:
        risultato = "Negativo (punteggio < 46)"
    return {'risultato': risultato, 'punteggio_totale': punteggio_totale}

def calcola_temps_a(risposte):
    domini_config = {
        'depressivo': (0, 22),
        'ciclotimico': (22, 42),
        'ipertimico': (42, 63),
        'irritabile': (63, 83),
        'ansioso': (83, 110)
    }
    punteggi_medi = {}
    for dominio, (start, end) in domini_config.items():
        somma_dominio = sum(risposte[start:end])
        num_item = end - start
        punteggi_medi[dominio] = somma_dominio / num_item if num_item > 0 else 0
    
    temperamento_dominante = "Nessuno"
    max_punteggio = 1.4 
    for dominio, punteggio in punteggi_medi.items():
        if punteggio >= max_punteggio:
            max_punteggio = punteggio
            temperamento_dominante = dominio.capitalize()
            
    return {'punteggi_medi': punteggi_medi, 'temperamento_dominante': temperamento_dominante}

def calcola_bis11(risposte):
    item_reverse = [1, 7, 8, 9, 10, 12, 13, 15, 20, 29, 30]
    punteggio_totale = 0
    for i, risposta in enumerate(risposte, 1):
        if i in item_reverse:
            punteggio_totale += (5 - risposta)
        else:
            punteggio_totale += risposta
            
    if punteggio_totale > 75:
        interpretazione = "Disturbo del controllo degli impulsi"
    elif punteggio_totale > 70:
        interpretazione = "Tratto patologico di impulsività"
    else:
        interpretazione = "Impulsività nella norma"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_tas20(risposte):
    item_reverse = [4, 5, 10, 18, 19]
    punteggio_totale = 0
    for i, risposta in enumerate(risposte, 1):
        if i in item_reverse:
            punteggio_totale += (6 - risposta)
        else:
            punteggio_totale += risposta

    if punteggio_totale >= 61:
        interpretazione = "Presenza di alessitimia"
    elif punteggio_totale >= 52:
        interpretazione = "Possibile alessitimia (borderline)"
    else:
        interpretazione = "Nessuna evidenza di alessitimia"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_mdq(risposte_p1, risposta_p2, risposta_p3):
    conteggio_sintomi = sum(risposte_p1)
    simultaneita = risposta_p2
    compromissione = risposta_p3
    
    if conteggio_sintomi >= 7 and simultaneita and compromissione >= 3:
        risultato = "Positivo (suggerisce approfondimento per disturbo bipolare)"
    else:
        risultato = "Negativo"
    return {'risultato': risultato, 'conteggio_sintomi': conteggio_sintomi, 'simultaneita': simultaneita, 'compromissione': compromissione}

def calcola_hcl34(risposte):
    punteggio_totale = sum(risposte)
    if punteggio_totale >= 14:
        risultato = "Positivo (suggerisce la presenza di tratti ipomaniacali)"
    else:
        risultato = "Negativo"
    return {'risultato': risultato, 'punteggio_totale': punteggio_totale}

def calcola_ders(risposte):
    item_reverse = [1, 2, 6, 7, 8, 10, 17, 20, 22, 24, 34]
    punteggio_totale = 0
    for i, risposta in enumerate(risposte, 1):
        if i in item_reverse:
            punteggio_totale += (6 - risposta)
        else:
            punteggio_totale += risposta
            
    if punteggio_totale >= 120:
        interpretazione = "Difficoltà clinicamente significative nella regolazione emotiva"
    else:
        interpretazione = "Difficoltà nella norma o lievi"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_mews(risposte):
    punteggio_totale = sum(risposte)
    if punteggio_totale >= 22:
        risultato = "Livello significativo di 'engulfment'"
    else:
        risultato = "Livello non significativo di 'engulfment'"
    return {'risultato': risultato, 'punteggio_totale': punteggio_totale}

def calcola_stai_y2(risposte):
    item_reverse = [1, 3, 6, 7, 10, 13, 14, 16, 19]
    punteggio_totale = 0
    for i, risposta in enumerate(risposte, 1):
        if i in item_reverse:
            punteggio_totale += (5 - risposta)
        else:
            punteggio_totale += risposta
            
    if punteggio_totale >= 40:
        interpretazione = "Punteggio indicativo di un livello di ansia di tratto clinicamente significativo"
    else:
        interpretazione = "Livello di ansia di tratto nella norma"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_stai_y1(risposte):
    item_reverse = [1, 2, 5, 8, 10, 11, 15, 16, 19, 20]
    punteggio_totale = 0
    for i, risposta in enumerate(risposte, 1):
        if i in item_reverse:
            punteggio_totale += (5 - risposta)
        else:
            punteggio_totale += risposta
            
    if punteggio_totale >= 40:
        interpretazione = "Punteggio indicativo di un livello di ansia di stato elevato"
    else:
        interpretazione = "Livello di ansia di stato nella norma"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}
import datetime

def calcola_tutti_i_risultati(risposte, test_compilati):
    """
    Esegue i calcoli solo per i test che sono stati compilati.
    """
    risultati = {}
    if 'asrs' in test_compilati:
        risultati['ASRS-v1.1'] = calcola_asrs(risposte['asrs'][:6])
    if 'wurs' in test_compilati:
        risultati['WURS'] = calcola_wurs(risposte['wurs'])
    if 'temps_a' in test_compilati:
        risultati['TEMPS-A'] = calcola_temps_a(risposte['temps_a'])
    if 'bis11' in test_compilati:
        risultati['BIS-11'] = calcola_bis11(risposte['bis11'])
    if 'tas20' in test_compilati:
        risultati['TAS-20'] = calcola_tas20(risposte['tas20'])
    if 'mdq' in test_compilati:
        risultati['MDQ'] = calcola_mdq(risposte['mdq']['parte1'], risposte['mdq']['parte2'], risposte['mdq']['parte3'])
    if 'hcl34' in test_compilati:
        risultati['HCL-34'] = calcola_hcl34(risposte['hcl34'])
    if 'ders' in test_compilati:
        risultati['DERS'] = calcola_ders(risposte['ders'])
    if 'mews' in test_compilati:
        risultati['MEWS'] = calcola_mews(risposte['mews'])
    if 'stai_y2' in test_compilati:
        risultati['STAI-Y-2'] = calcola_stai_y2(risposte['stai_y2'])
    if 'stai_y1' in test_compilati:
        risultati['STAI-Y-1'] = calcola_stai_y1(risposte['stai_y1'])
    return risultati

def formatta_risultati_email(dati_paziente, risultati):
    """
    Crea il corpo del testo (HTML) per l'email con tutti i dati.
    """
    data_nascita_str = dati_paziente['data_nascita'].strftime('%d/%m/%Y')

    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif; line-height: 1.6; }}
            h1 {{ color: #003366; }}
            h2 {{ color: #0055a4; border-bottom: 2px solid #0055a4; padding-bottom: 5px; margin-top: 30px;}}
            h3 {{ color: #333; }}
            .container {{ border: 1px solid #ddd; padding: 15px; margin-bottom: 15px; border-radius: 8px; background-color: #f9f9f9; }}
            .label {{ font-weight: bold; color: #555; }}
            p {{ margin: 5px 0; }}
            ul {{ padding-left: 20px; }}
            li {{ margin-bottom: 5px; }}
        </style>
    </head>
    <body>
        <h1>Nuova Compilazione Test ADHD</h1>
        <p>Un paziente ha completato i questionari in data {datetime.datetime.now().strftime('%d/%m/%Y alle %H:%M')}.</p>
        
        <h2>Dati Paziente</h2>
        <div class="container">
            <p><span class="label">Codice Paziente:</span> {dati_paziente['codice_paziente']}</p>
            <p><span class="label">Data di Nascita:</span> {data_nascita_str}</p>
            <p><span class="label">Genere:</span> {dati_paziente['genere']}</p>
            <p><span class="label">Livello Istruzione:</span> {dati_paziente['livello_istruzione']}</p>
        </div>
    """
    if not risultati:
        html += "<h2>Nessun questionario è stato compilato.</h2>"
    else:
        html += "<h2>Risultati dei Test Compilati</h2>"
        for nome_test, risultato in risultati.items():
            html += f"<h3>{nome_test}</h3><div class='container'>"
            for chiave, valore in risultato.items():
                if isinstance(valore, dict):
                    html += f"<p><span class='label'>{chiave.replace('_', ' ').capitalize()}:</span></p><ul>"
                    for sub_chiave, sub_valore in valore.items():
                        html += f"<li>{sub_chiave.capitalize()}: {sub_valore:.2f}</li>"
                    html += "</ul>"
                else:
                    html += f"<p><span class='label'>{chiave.replace('_', ' ').capitalize()}:</span> {valore}</p>"
            html += "</div>"

    html += """
    </body>
    </html>
    """
    return html
