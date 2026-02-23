# File: calcolatore_test.py

# --- Funzioni di Calcolo dei Punteggi ---

def calcola_asrs(risposte_parte_a):
    punteggi_positivi = [1 if risposte_parte_a[i] >= 2 else 0 for i in [0, 1, 2]]
    punteggi_positivi += [1 if risposte_parte_a[i] >= 3 else 0 for i in [3, 4, 5]]
    punteggio_totale = sum(punteggi_positivi)
    if punteggio_totale >= 4:
        risultato = "Positivo (suggerisce approfondimento diagnostico)"
    else:
        risultato = "Negativo"
    return {'risultato': risultato, 'punteggio_positivo': punteggio_totale}

def calcola_wurs(risposte, genere_paziente):
    item_da_sommare = [3, 4, 5, 6, 7, 9, 10, 11, 12, 15, 16, 17, 20, 21, 24, 25, 26, 27, 28, 29, 40, 41, 51, 56, 59]
    punteggio_totale = sum(risposte[i-1] for i in item_da_sommare if i-1 < len(risposte))
    if punteggio_totale >= 46:
        risultato = "Positivo (punteggio >= 46)"
    else:
        risultato = "Negativo (punteggio < 46)"
    return {'risultato': risultato, 'punteggio_totale': punteggio_totale}

def calcola_temps_a(risposte, genere_paziente):
    domini_config = {
        'depressivo': (0, 22), 'ciclotimico': (22, 42),
        'ipertimico': (42, 63), 'irritabile': (63, 83),
        'ansioso': (84, 110)
    }
    if genere_paziente != "Maschio":
        domini_config['irritabile'] = (63, 84)
    
    punteggi_medi = {}
    for dominio, (start, end) in domini_config.items():
        risposte_dominio = risposte[start:end]
        somma_dominio = sum(risposte_dominio)
        num_item = len(risposte_dominio)
        punteggi_medi[dominio] = round(somma_dominio / num_item, 2) if num_item > 0 else 0
    
    temperamento_dominante = "Nessuno"
    max_punteggio = 0
    for dominio, punteggio in punteggi_medi.items():
        if punteggio >= 1.4 and punteggio > max_punteggio:
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
        interpretazione = "Disturbo del controllo degli impulsi (punteggio > 75)"
    elif punteggio_totale > 70:
        interpretazione = "Tratto patologico di impulsività (70 < punteggio <= 75)"
    else:
        interpretazione = "Impulsività nella norma (punteggio <= 70)"
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
        interpretazione = "Presenza di alessitimia (punteggio >= 61)"
    elif punteggio_totale >= 52:
        interpretazione = "Possibile alessitimia (borderline, 52-60)"
    else:
        interpretazione = "Assenza di alessitimia (punteggio <= 51)"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_mdq(risposte_p1, risposta_p2, risposta_p3):
    num_sintomi = sum(risposte_p1)
    if num_sintomi >= 7 and risposta_p2 and risposta_p3 >= 3:
        risultato = "Positivo (suggerisce approfondimento per disturbo bipolare)"
    else:
        risultato = "Negativo"
    return {'risultato': risultato, 'num_sintomi': num_sintomi, 'simultaneita': risposta_p2, 'compromissione': risposta_p3}

def calcola_hcl34(risposte):
    punteggio_totale = sum(risposte)
    if punteggio_totale >= 14:
        risultato = "Positivo (punteggio >= 14)"
    else:
        risultato = "Negativo (punteggio < 14)"
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
        interpretazione = "Difficoltà clinicamente significative nella regolazione emotiva (punteggio >= 120)"
    else:
        interpretazione = "Difficoltà nella norma (punteggio < 120)"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_mews(risposte):
    punteggio_totale = sum(risposte)
    if punteggio_totale >= 22:
        interpretazione = "Livello significativo di 'engulfment' (percezione di essere sopraffatto/definito dai sintomi)"
    else:
        interpretazione = "Livello non significativo di 'engulfment'"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_stai_y2(risposte):
    item_reverse = [1, 3, 6, 7, 10, 13, 14, 16, 19]
    punteggio_totale = 0
    for i, risposta in enumerate(risposte, 1):
        if i in item_reverse:
            punteggio_totale += (5 - risposta)
        else:
            punteggio_totale += risposta
    if punteggio_totale >= 40:
        interpretazione = "Punteggio indicativo di un livello di ansia di tratto clinicamente significativo (soglia di riferimento >= 40)"
    else:
        interpretazione = "Livello di ansia di tratto nella norma (soglia di riferimento < 40)"
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
        interpretazione = "Punteggio indicativo di un livello di ansia di stato elevato (soglia di riferimento >= 40)"
    else:
        interpretazione = "Livello di ansia di stato nella norma (soglia di riferimento < 40)"
    return {'interpretazione': interpretazione, 'punteggio_totale': punteggio_totale}

def calcola_des2(risposte):
    # Le risposte sono già in percentuale (0, 10, 20, ..., 100)
    somma_percentuali = sum(risposte)
    punteggio_medio = round(somma_percentuali / 28, 2)
    
    if punteggio_medio >= 30:
        interpretazione = "Punteggio indicativo di possibile disturbo dissociativo clinicamente significativo (>= 30)"
    else:
        interpretazione = "Punteggio non indicativo di disturbo dissociativo clinicamente significativo (< 30)"
        
    return {'interpretazione': interpretazione, 'punteggio_medio': punteggio_medio}

# --- Funzione Principale di Calcolo ---

def calcola_tutti_i_risultati(risposte, test_compilati, genere_paziente):
    risultati = {}
    if 'asrs' in test_compilati:
        risultati['ASRS-v1.1'] = calcola_asrs(risposte['asrs'][:6])
    if 'wurs' in test_compilati:
        risultati['WURS'] = calcola_wurs(risposte['wurs'], genere_paziente)
    if 'temps_a' in test_compilati:
        risultati['TEMPS-A'] = calcola_temps_a(risposte['temps_a'], genere_paziente)
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
    # Aggiungi la riga seguente
    if 'des2' in test_compilati:
        risultati['DES-II'] = calcola_des2(risposte['des2'])
    if 'mews' in test_compilati:
        risultati['MEWS'] = calcola_mews(risposte['mews'])
    if 'stai_y2' in test_compilati:
        risultati['STAI-Y-2'] = calcola_stai_y2(risposte['stai_y2'])
    if 'stai_y1' in test_compilati:
        risultati['STAI-Y-1'] = calcola_stai_y1(risposte['stai_y1'])
    return risultati

# --- Funzione di Formattazione Email ---

def formatta_risultati_email(dati_paziente, risultati, wurs_extra=""):
    html = f"""
    <html>
    <head>
        <style>
            body {{ font-family: sans-serif; margin: 20px; }}
            h1 {{ color: #1E3A8A; }}
            h2 {{ color: #1D4ED8; border-bottom: 2px solid #DBEAFE; padding-bottom: 5px; }}
            .container {{ background-color: #F9FAFB; border: 1px solid #E5E7EB; padding: 15px; border-radius: 8px; margin-bottom: 20px; }}
            .info-grid {{ display: grid; grid-template-columns: 150px 1fr; gap: 5px; }}
            .info-grid strong {{ color: #374151; }}
        </style>
    </head>
    <body>
        <h1>Nuova Compilazione Test</h1>
        <div class="container">
            <h2>Dati Paziente</h2>
            <div class="info-grid">
                <strong>Codice Paziente:</strong><span>{dati_paziente['codice_paziente']}</span>
                <strong>Data di Nascita:</strong><span>{dati_paziente['data_nascita'].strftime('%d/%m/%Y')}</span>
                <strong>Genere:</strong><span>{dati_paziente['genere']}</span>
                <strong>Livello Istruzione:</strong><span>{dati_paziente['livello_istruzione']}</span>
            </div>
        </div>
        <div class="container">
            <h2>Risultati dei Test Compilati</h2>
    """
    if not risultati:
        html += "<p>Nessun test è stato compilato in questa sessione.</p>"
    else:
        for test, res in risultati.items():
            html += f"<h3>{test}</h3><ul>"
            for chiave, valore in res.items():
                html += f"<li><strong>{chiave.replace('_', ' ').capitalize()}:</strong> {valore}</li>"
            if test == 'WURS' and wurs_extra:
                html += f"<li><strong>Risposta a 'Sospeso o espulso':</strong> {wurs_extra}</li>"
            html += "</ul>"
    
    html += """
        </div>
    </body>
    </html>
    """
    return html
