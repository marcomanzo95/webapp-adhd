import bisect

# ══════════════════════════════════════════════════════════════════════
# ABAS-II — Dati questionario e tavole normative (eterovalutazione)
# ══════════════════════════════════════════════════════════════════════

OPZIONI_ABAS = {
    0: "Non è in grado",
    1: "Mai o quasi mai quando è necessario",
    2: "Qualche volta quando è necessario",
    3: "Sempre o quasi sempre quando è necessario",
}

AREE_ABAS = {
    "comunicazione": {
        "label": "Comunicazione", "dominio": "DAC", "max": 75,
        "items": [
            "Dice il nome di altre persone, ad esempio dice \"Mamma\", \"Papà\", o il nome degli amici",
            "Dice \"Ciao\" o \"Arrivederci\" agli altri",
            "Sa comporre il proprio numero di telefono",
            "Usa frasi con un sostantivo e un verbo",
            "Specifica il proprio indirizzo, compreso il CAP",
            "Risponde al telefono in modo adeguato ad esempio \"Pronto\", \"Chi è?\", \"Chi cerca?\"",
            "Nomina 20 o più oggetti",
            "È in grado di usare il telefono",
            "Parla in maniera chiara e distinta",
            "Fornisce istruzioni verbali che includono due o più sequenze",
            "Guarda gli altri in viso mentre parlano",
            "Scuote la testa o dice \"Sì\" o \"No\" in risposta a semplici quesiti",
            "Conclude le conversazioni in modo appropriato",
            "Parla ai genitori, agli amici o ad altri delle proprie attività preferite",
            "Dice il plurale irregolare delle parole, ad esempio \"le uova\"",
            "Ascolta attentamente per almeno 5 minuti quando qualcuno gli parla",
            "Presta attenzione durante le conversazioni in famiglia o in altri contesti",
            "Annuisce o sorride per incoraggiare gli altri quando parlano",
            "Usa informazioni aggiornate per discutere di avvenimenti recenti",
            "Inizia conversazioni su argomenti interessanti per gli altri",
            "Racconta storie o barzellette dopo averle ascoltate da altri",
            "Durante una conversazione, aspetta il proprio turno prima di esprimere il proprio parere",
            "Risponde a domande complesse che richiedono idee precise e opinioni",
            "Parla di obiettivi realistici in ambito formativo o di lavoro",
            "Prende la parola durante le conversazioni (non è troppo loquace o troppo silenzioso)",
        ],
    },
    "uso_ambiente": {
        "label": "Uso dell'ambiente", "dominio": "DAP", "max": 72,
        "items": [
            "Ordina i propri pasti quando mangia fuori",
            "Trova il bagno nei luoghi pubblici",
            "Guarda da entrambi i lati prima di attraversare la strada o un parcheggio",
            "Sa gestire il denaro sufficiente per piccoli acquisti",
            "Porta i documenti quando si sposta in luoghi vicini alla sua città",
            "Trova uno specifico reparto in un negozio o in un'azienda",
            "Sa come spostarsi nella sua città/quartiere",
            "Fa i bagagli e si attrezza per dormire fuori casa",
            "Spedisce lettere nella cassetta della posta o all'ufficio postale",
            "Sa indicare un indirizzo o la destinazione di un viaggio",
            "Segue le indicazioni di un altro per muoversi nei dintorni della sua zona",
            "Trova e usa un telefono pubblico o un Internet point",
            "Chiede aiuto a un commesso se non riesce a trovare un articolo/oggetto",
            "Sa indicare agli altri gli orari di apertura di un negozio",
            "Va da solo a casa di amici nel vicinato",
            "Chiama un dottore o l'ospedale se sta male o si è ferito",
            "Telefona per sapere se una riparazione o un ordine sono pronti",
            "Chiama un tecnico se necessario",
            "Porta altre persone in giro nei dintorni di casa",
            "Chiede consiglio agli altri su dove fare acquisti",
            "Fa acquisti per amici e familiari che non sono in grado di farlo",
            "Cammina o va in bicicletta da solo nelle zone limitrofe",
            "Utilizza la biblioteca per consultare libri o per altri scopi",
            "Chiede a un commesso informazioni sui prodotti prima di comprare un oggetto",
        ],
    },
    "competenze_scolastiche": {
        "label": "Competenze scolastiche", "dominio": "DAC", "max": 81,
        "items": [
            "Scrive il proprio nome e cognome",
            "Legge il proprio nome scritto",
            "Elenca i giorni della settimana in ordine",
            "Dice l'ora correttamente usando l'orologio",
            "Dà al commesso la giusta cifra quando acquista un oggetto",
            "Scrive il proprio indirizzo compreso il CAP",
            "Legge e rispetta simboli comuni, ad esempio \"Non entrare\", \"Uscita\", o \"Stop\"",
            "Legge il menù al ristorante",
            "Trova il numero di telefono di qualcuno sull'elenco o su internet",
            "Conosce l'ora e il giorno dei suoi programmi preferiti in televisione",
            "Legge e segue il programma quotidiano al lavoro o in altri contesti",
            "Individua date importanti sul calendario",
            "Usa correttamente la bilancia per pesarsi o per pesare gli oggetti",
            "Misura lunghezza e altezza",
            "Sa trovare i recapiti telefonici di un servizio di riparazioni",
            "Controlla se il resto è corretto dopo aver comprato un oggetto",
            "Coltiva un interesse o segue un evento di attualità leggendo giornali o libri",
            "Tiene il punteggio quando fa un gioco",
            "Usa un dizionario o un'enciclopedia o Internet per trovare informazioni",
            "Legge e segue le istruzioni per assemblare o montare un nuovo oggetto",
            "Scrive lettere, appunti o e-mail",
            "Scrive appunti o prende note per non dimenticarsi le cose da fare",
            "Compila la modulistica necessaria per richieste di servizi",
            "Legge documenti importanti, ad esempio il regolamento per richiedere una carta di credito",
            "Gestisce il denaro che ha a disposizione per coprire le spese per almeno una settimana",
            "Legge gli annunci per acquisti e servizi",
            "Compila un assegno",
        ],
    },
    "vita_a_casa": {
        "label": "Vita a casa", "dominio": "DAP", "max": 69,
        "items": [
            "Sa usare il forno a microonde",
            "Usa piccoli elettrodomestici, ad esempio un apriscatole o un frullatore",
            "Cucina semplici cibi sui fornelli",
            "Prepara semplici pasti che non richiedono di cucinare",
            "Asciuga liquidi nel caso in cui si rovescino in casa",
            "Mette gli abiti sporchi nel luogo appropriato",
            "Si pulisce le scarpe bagnate o sporche prima di entrare in un'abitazione",
            "Lava i piatti a mano o mettendoli nella lavastoviglie",
            "Usa l'asciugatrice o lo stendino per la biancheria",
            "Usa la lavatrice per lavare gli indumenti",
            "Aiuta nelle grandi faccende domestiche",
            "Piega e mette a posto gli indumenti puliti",
            "Porta fuori la spazzatura quando è piena",
            "Sparecchia la tavola dopo un pasto",
            "Sistema il letto da solo",
            "Fa piccole riparazioni a oggetti personali",
            "Rimette le cose al proprio posto quando finisce di usarle",
            "Spazza il pavimento",
            "Pulisce la sua stanza regolarmente",
            "Pulisce il bagno con gli appositi prodotti",
            "Prepara e cucina cibi abbastanza complessi",
            "Spolvera i mobili",
            "Sa fare la manutenzione delle proprie cose",
        ],
    },
    "salute_sicurezza": {
        "label": "Salute e sicurezza", "dominio": "DAP", "max": 60,
        "items": [
            "Prende lo sciroppo quando sta male, se necessario",
            "Mostra prudenza vicino a oggetti caldi o pericolosi",
            "Usa senza correre rischi le spine o le prese di corrente",
            "Si sposta da solo quando fa troppo caldo o troppo freddo",
            "Trasporta oggetti fragili senza rischi e con cautela",
            "Rispetta le regole di base sulla sicurezza in casa",
            "Rispetta le regole di sicurezza in caso di incendio o di allarme antincendio",
            "Rispetta le regole di base sulla sicurezza al lavoro o in altri luoghi pubblici",
            "Prende da solo le medicine che gli vengono prescritte",
            "Cura da sé piccole ferite come tagli da carta o ginocchia graffiate",
            "Assaggia i cibi caldi prima di mangiarli",
            "Usa le forbici con facilità e senza fare o farsi male",
            "Rispetta le regole di base sulla sicurezza al parco o in altri contesti",
            "Si allaccia la cintura di sicurezza in macchina",
            "Rispetta i segnali stradali quando guida la bicicletta o la macchina",
            "Quando necessario, compra da solo farmaci da banco",
            "Tiene lontano dalla portata dei bambini sostanze o oggetti pericolosi",
            "Aiuta i bambini ad attraversare la strada prendendoli per mano",
            "Si misura la temperatura con il termometro quando sente di avere la febbre",
            "Organizza i propri pasti in maniera da assicurarsi una giusta nutrizione",
        ],
    },
    "tempo_libero": {
        "label": "Tempo libero", "dominio": "DAS", "max": 69,
        "items": [
            "Aspetta il proprio turno nei giochi o in altre attività",
            "Sceglie programmi televisivi o CD/DVD per aggiornarsi riguardo a un'area d'interesse",
            "Segue le regole nei giochi o in altre attività di svago",
            "Ascolta la musica per divertimento o relax",
            "Legge fumetti, libri o giornali durante il tempo libero",
            "Invita gli altri a giocare con lui e a fare altre attività divertenti",
            "Va a casa di altri",
            "Gioca o fa attività divertenti con altre persone",
            "Comunica agli altri quando ha bisogno di un po' di tempo per stare solo",
            "Prende parte ad attività collettive con altri, come vedere un film o un concerto",
            "Decide da solo se partecipare a giochi o attività con altre persone",
            "Programma in anticipo attività di svago nei giorni liberi o nel pomeriggio",
            "Propone attività o sceglie programmi TV che piacciono ad amici o a membri della famiglia",
            "Ha un gioco o un'attività preferita in cui si diletta",
            "Programma in anticipo attività di svago durante le pause di lavoro o durante le vacanze",
            "Gioca da solo o fa altre attività divertenti",
            "Invita altri a casa per giocare o stare insieme",
            "Organizza un gioco o altre attività di svago per un gruppo di amici senza l'aiuto di altri",
            "Prova nuove attività per imparare qualcosa di nuovo",
            "Ha un hobby o un'attività creativa che richiede di realizzare o costruire qualcosa",
            "Prenota in anticipo i biglietti per attività, ad esempio concerti o eventi sportivi",
            "Decide da solo di unirsi a un gruppo organizzato",
            "Partecipa a un programma organizzato di sport o svago",
        ],
    },
    "cura_se": {
        "label": "Cura di sé", "dominio": "DAP", "max": 75,
        "items": [
            "Mette le scarpe al piede giusto",
            "Si soffia o si pulisce il naso da solo con il fazzoletto",
            "Si abbottona da solo i vestiti",
            "Si veste da solo",
            "Usa il bagno senza aiuto",
            "Si lava le mani con il sapone",
            "Usa da solo la forchetta per mangiare",
            "Si allaccia le scarpe",
            "Miscela da solo l'acqua (calda e fredda) per fare la doccia o il bagno",
            "Chiude a chiave la porta quando va in un bagno pubblico",
            "Usa i bagni pubblici da solo",
            "Si lava i capelli da solo",
            "Si allaccia e si sistema gli indumenti prima di uscire dal bagno",
            "Sceglie gli indumenti adatti in base al freddo o al caldo",
            "Si pulisce o spazzola da solo gli indumenti se si è sporcato",
            "Si lava i denti prima di uscire per andare al lavoro o a un appuntamento",
            "Cura la sua igiene quotidianamente",
            "Tiene i capelli in ordine durante il giorno",
            "Taglia la carne o altri cibi in pezzi di dimensioni adeguate",
            "Tiene le unghie pulite",
            "Si alza dal letto in orario da solo",
            "Tiene in ordine regolarmente le proprie unghie (tagliandole o limandole)",
            "Cura regolarmente la propria igiene orale",
            "Tiene pulito il lavandino dopo aver lavato i denti",
            "Va a tagliarsi i capelli da solo",
        ],
    },
    "autocontrollo": {
        "label": "Autocontrollo", "dominio": "DAC", "max": 75,
        "items": [
            "Tiene i soldi da spendere in tasca, nel portamonete o in un altro posto sicuro",
            "Lavora in modo autonomo e chiede aiuto solo se necessario",
            "Si dedica a un'attività a casa per almeno 15 minuti",
            "Di giorno esce da solo",
            "Evita situazioni (a casa o fuori) che possano metterlo in pericolo",
            "Sospende un'attività, senza lamentarsi, quando gli si dice che deve smettere",
            "Avvisa, da solo, il datore di lavoro (o altri) se si assenta o se non può andare",
            "Termina le faccende domestiche di routine in un tempo ragionevole",
            "Controlla la rabbia quando un'altra persona infrange le regole di un gioco",
            "Evita di dire bugie (per non essere rimproverato)",
            "Di solito è puntuale",
            "Controlla la delusione quando un'attività preferita è cancellata o sospesa",
            "Controlla le proprie reazioni quando è in disaccordo con gli amici",
            "Continua a lavorare su compiti difficili senza scoraggiarsi o smettere",
            "Risparmia denaro per comprare qualcosa di speciale",
            "Annulla le proprie attività di svago se subentrano impegni più importanti",
            "Ritorna in tempo quando gli si chiede di rientrare a un'ora specifica",
            "Quando esce di casa, informa gli altri sulla destinazione e sull'orario di rientro",
            "Si controlla quando non si fa a modo suo",
            "Antepone gli impegni lavorativi o scolastici a quelli di svago personale",
            "Pianifica in anticipo i tempi e le modalità per completare progetti importanti",
            "Pianifica le attività da fare a casa seguendo un criterio logico e organizzato",
            "Prende tutti gli oggetti necessari prima di iniziare lavori di pulizia o manutenzione",
            "Avvisa i familiari o altri, quando è in ritardo",
            "Porta a termine grandi faccende in casa in un tempo ragionevole",
        ],
    },
    "socializzazione": {
        "label": "Socializzazione", "dominio": "DAS", "max": 69,
        "items": [
            "Dice \"Grazie\" quando gli si dà un regalo",
            "Ha uno o più amici",
            "Ride in risposta a battute divertenti o a barzellette",
            "Evita di intromettersi durante le conversazioni degli altri",
            "Si toglie dal posto di un'altra persona senza che gli venga chiesto",
            "Offre aiuto agli altri",
            "Si congratula con gli altri quando accade loro qualcosa di bello",
            "Ha un gruppo stabile di amici",
            "Ricerca l'amicizia dei suoi coetanei",
            "Ha buone relazioni con i genitori e altri adulti",
            "Mostra comprensione per gli altri quando sono tristi o arrabbiati",
            "Nelle amicizie pone richieste ragionevoli",
            "Offre agli ospiti cibo o bevande",
            "Mostra buon senso nello scegliere gli amici",
            "Ascolta gli amici o i membri della famiglia quando hanno bisogno di parlare",
            "Si offre di prestare oggetti agli altri",
            "Si scusa quando ferisce la sensibilità degli altri",
            "Si complimenta con gli altri per buone azioni o comportamenti",
            "Cerca di compiacere gli altri, ad esempio facendo qualcosa di speciale",
            "Dice se una persona gli sembra felice, triste, impaurita o arrabbiata",
            "Si trattiene dal dire qualcosa che potrebbe imbarazzare o ferire gli altri",
            "Realizza o compra personalmente regali per i membri della famiglia",
            "Dice quando è felice, triste, impaurito o arrabbiato",
        ],
    },
    "lavoro": {
        "label": "Lavoro", "dominio": "DAP", "max": 72, "opzionale": True,
        "items": [
            "Rispetta le proprietà e i diritti degli altri lavoratori",
            "Va al lavoro regolarmente",
            "Segue l'orario di lavoro quotidiano senza bisogno che un adulto glielo ricordi",
            "Lavora seguendo le regole di sicurezza",
            "Al lavoro svolge le mansioni in maniera precisa",
            "Tiene con adeguata cura gli strumenti o le attrezzature da lavoro",
            "Aumenta il ritmo lavorativo se necessario, ad esempio per rispettare una scadenza",
            "Dopo aver terminato un lavoro mette in ordine o pulisce",
            "Rimette gli strumenti di lavoro al proprio posto quando finisce di utilizzarli",
            "Porta a termine il lavoro assegnato nei limiti di tempo richiesti",
            "Torna al lavoro volentieri dopo aver preso una pausa o dopo il pranzo",
            "Sceglie lavori coerenti con le proprie attitudini e abilità",
            "Lavora con calma e non disturba il lavoro degli altri",
            "Passa da un compito a quello successivo senza bisogno di istruzioni del supervisore",
            "Valuta il proprio rendimento al lavoro per stabilire se sono necessari miglioramenti",
            "Si cerca da solo il lavoro part-time o a tempo pieno",
            "Esegue volentieri incarichi extra sul lavoro",
            "Chiede istruzioni, se necessario, prima di iniziare un compito di lavoro",
            "Continua a lavorare accuratamente, anche se ci sono rumori o fonti di distrazioni",
            "Segue i suggerimenti di un supervisore/tutore per migliorare il lavoro",
            "Aiuta gli altri nel lavoro senza che ciò interferisca con il proprio lavoro",
            "Ricerca l'aiuto di un supervisore, se necessario, quando sorgono problemi al lavoro",
            "Mostra un atteggiamento positivo verso il lavoro",
            "Vive autonomamente con il proprio stipendio",
        ],
    },
}

# ── Helper per costruire tabella grezzo → Pp ─────────────────────────
def _build_area(entries):
    table = {}
    for entry in entries:
        if len(entry) == 3:
            pp, start, end = entry
            for v in range(start, end + 1):
                table[v] = pp
        else:
            pp, val = entry
            table[val] = pp
    return table

# ══════════════════════════════════════════════════════════════════════
# TABELLA A.12 — Grezzo → Pp (eterovalutazione adulto, fasce 16-49)
# ══════════════════════════════════════════════════════════════════════
_A12_16_21 = {
    "co": _build_area([
        (1,0,28),(2,29,36),(3,37,43),(4,44,49),(5,50,54),
        (6,55,58),(7,59,62),(8,63,65),(9,66,68),(10,69,70),
        (11,71,72),(12,73,74),(13,75,75),
    ]),
    "am": _build_area([
        (1,0,16),(2,17,25),(3,26,33),(4,34,40),(5,41,46),
        (6,47,51),(7,52,55),(8,56,58),(9,59,62),(10,63,65),
        (11,66,68),(12,69,69),
    ]),
    "sco": _build_area([
        (1,0,26),(2,27,35),(3,36,43),(4,44,50),(5,51,56),
        (6,57,61),(7,62,65),(8,66,69),(9,70,73),(10,74,75),
        (11,76,79),(12,80,81),
    ]),
    "vc": _build_area([
        (1,0,13),(2,14,30),(3,31,36),(4,37,41),(5,42,45),
        (6,46,50),(7,51,54),(8,55,57),(9,58,60),(10,61,63),
        (11,64,65),(12,66,68),
    ]),
    "ss": _build_area([
        (1,0,23),(2,24,30),(3,31,36),(4,37,41),(5,42,45),
        (6,46,48),(7,49,51),(8,52,52),
        (9,54,55),(10,56,56),(11,57,57),(12,58,58),(13,59,60),
    ]),
    "tl": _build_area([
        (1,0,20),(2,21,28),(3,29,35),(4,36,41),(5,42,46),
        (6,47,50),(7,51,54),(8,55,57),(9,58,60),(10,61,63),
        (11,64,65),(12,66,67),(13,68,68),(14,69,69),
    ]),
    "cur": _build_area([
        (1,0,40),(2,41,47),(3,48,53),(4,54,58),(5,59,62),
        (6,63,66),(7,67,68),(8,69,71),(9,72,73),
    ]),
    "ac": _build_area([
        (1,0,16),(2,17,25),(3,26,34),(4,35,40),(5,41,46),
        (6,47,51),(7,52,55),(8,56,60),(9,61,63),(10,64,69),
        (11,70,72),(12,73,74),(13,75,75),
    ]),
    "soc": _build_area([
        (1,0,18),(2,19,27),(3,28,35),(4,36,42),(5,43,48),
        (6,49,53),(7,54,57),(8,58,60),(9,61,63),(10,64,66),
        (11,67,69),
    ]),
    "lav": _build_area([
        (1,0,26),(2,27,34),(3,35,41),(4,42,47),(5,48,52),
        (6,53,56),(7,57,59),(8,60,63),(9,64,65),(10,66,67),
        (11,68,68),
    ]),
}

_A12_22_29 = {
    "co": _build_area([
        (1,0,30),(2,31,38),(3,39,45),(4,46,51),(5,52,56),
        (6,57,60),(7,61,64),(8,65,67),(9,68,70),(10,71,72),
        (11,73,73),(12,74,74),(13,75,75),
    ]),
    "am": _build_area([
        (1,0,20),(2,21,29),(3,30,37),(4,38,44),(5,45,50),
        (6,51,55),(7,56,59),(8,60,62),(9,63,65),(10,66,67),
        (11,68,69),(12,70,71),(13,72,72),
    ]),
    "sco": _build_area([
        (1,0,30),(2,31,39),(3,40,47),(4,48,54),(5,55,60),
        (6,61,65),(7,66,69),(8,70,73),(9,74,76),(10,77,78),
        (11,79,79),(12,80,80),(13,81,81),
    ]),
    "vc": _build_area([
        (1,0,15),(2,16,23),(3,24,30),(4,31,37),(5,38,43),
        (6,44,48),(7,49,52),(8,53,56),(9,57,60),(10,61,63),
        (11,64,65),(12,66,67),(13,68,68),(14,69,69),
    ]),
    "ss": _build_area([
        (1,0,23),(2,24,30),(3,31,36),(4,37,41),(5,42,46),
        (6,47,50),(7,51,53),(8,54,55),(9,56,56),(10,57,57),
        (11,58,58),(12,59,59),(13,60,60),
    ]),
    "tl": _build_area([
        (1,0,20),(2,21,28),(3,29,35),(4,36,41),(5,42,46),
        (6,47,50),(7,51,54),(8,55,57),(9,58,60),(10,61,63),
        (11,64,66),(12,67,68),(13,69,69),
    ]),
    "cur": _build_area([
        (1,0,44),(2,45,51),(3,52,57),(4,58,62),(5,63,66),
        (6,67,69),(7,70,71),(8,72,73),(9,74,74),(12,75,75),
    ]),
    "ac": _build_area([
        (1,0,23),(2,24,31),(3,32,38),(4,39,44),(5,45,49),
        (6,50,54),(7,55,58),(8,59,62),(9,63,66),(10,67,69),
        (11,70,71),(12,72,73),(13,74,74),(14,75,75),
    ]),
    "soc": _build_area([
        (1,0,30),(2,31,37),(3,38,43),(4,44,48),(5,49,52),
        (6,53,56),(7,57,59),(8,60,61),(9,62,64),(10,65,65),
        (11,66,67),(12,68,68),(13,69,69),
    ]),
    "lav": _build_area([
        (1,0,30),(2,31,38),(3,39,45),(4,46,51),(5,52,56),
        (6,57,60),(7,61,63),(8,64,66),(9,67,68),(10,69,69),
        (11,70,70),(12,71,71),(13,72,72),
    ]),
}

_A12_30_39 = {
    "co": _build_area([
        (1,0,36),(2,37,43),(3,44,49),(4,50,54),(5,55,58),
        (6,59,62),(7,63,66),(8,67,69),(9,70,71),(10,72,72),
        (11,73,73),(12,74,74),(13,75,75),
    ]),
    "am": _build_area([
        (1,0,22),(2,23,31),(3,32,39),(4,40,46),(5,47,52),
        (6,53,57),(7,58,61),(8,62,64),(9,65,67),(10,68,69),
        (11,70,70),(12,71,71),(13,72,72),
    ]),
    "sco": _build_area([
        (1,0,38),(2,39,46),(3,47,53),(4,54,59),(5,60,64),
        (6,65,68),(7,69,71),(8,72,74),(9,75,76),(10,77,78),
        (11,79,79),(12,80,80),(13,81,81),
    ]),
    "vc": _build_area([
        (1,0,22),(2,23,30),(3,31,37),(4,38,43),(5,44,48),
        (6,49,52),(7,53,56),(8,57,60),(9,61,63),(10,64,65),
        (11,66,66),(12,67,67),(13,68,69),
    ]),
    "ss": _build_area([
        (1,0,34),(2,35,40),(3,41,45),(4,46,49),(5,50,52),
        (6,53,54),(7,55,55),(8,56,56),(9,57,57),(10,58,58),
        (11,59,59),(12,60,60),
    ]),
    "tl": _build_area([
        (1,0,20),(2,21,29),(3,30,36),(4,37,41),(5,42,46),
        (6,47,50),(7,51,54),(8,55,57),(9,58,60),(10,61,63),
        (11,64,66),(12,67,68),(13,69,69),
    ]),
    "cur": _build_area([
        (1,0,44),(2,45,51),(3,52,57),(4,58,62),(5,63,66),
        (6,67,69),(7,70,71),(8,72,73),(9,74,74),(12,75,75),
    ]),
    "ac": _build_area([
        (1,0,25),(2,26,34),(3,35,42),(4,43,49),(5,50,55),
        (6,56,60),(7,61,64),(8,65,67),(9,68,69),(10,70,71),
        (11,72,73),(12,74,74),(13,75,75),
    ]),
    "soc": _build_area([
        (1,0,35),(2,36,41),(3,42,46),(4,47,50),(5,51,53),
        (6,54,56),(7,57,59),(8,60,62),(9,63,64),(10,65,66),
        (11,67,67),(12,68,68),(13,69,69),
    ]),
    "lav": _build_area([
        (1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,59),
        (6,60,62),(7,63,65),(8,66,67),(9,68,69),(10,70,70),
        (11,71,71),(12,72,72),
    ]),
}

_A12_40_49 = {
    "co": _build_area([
        (1,0,38),(2,39,45),(3,46,51),(4,52,56),(5,57,60),
        (6,61,63),(7,64,66),(8,67,69),(9,70,71),(10,72,72),
        (11,73,73),(12,74,74),(13,75,75),
    ]),
    "am": _build_area([
        (1,0,29),(2,30,37),(3,38,44),(4,45,50),(5,51,55),
        (6,56,59),(7,60,62),(8,63,65),(9,66,67),(10,68,69),
        (11,70,70),(12,71,71),(13,72,72),
    ]),
    "sco": _build_area([
        (1,0,39),(2,40,47),(3,48,54),(4,55,60),(5,61,65),
        (6,66,69),(7,70,72),(8,73,75),(9,76,77),(10,78,78),
        (11,79,79),(12,80,80),(13,81,81),
    ]),
    "vc": _build_area([
        (1,0,22),(2,23,30),(3,31,37),(4,38,43),(5,44,48),
        (6,49,52),(7,53,56),(8,57,60),(9,61,63),(10,64,65),
        (11,66,66),(12,67,67),(13,68,69),
    ]),
    "ss": _build_area([
        (1,0,34),(2,35,40),(3,41,45),(4,46,49),(5,50,52),
        (6,53,54),(7,55,55),(8,56,56),(9,57,57),(10,58,58),
        (11,59,59),(12,60,60),
    ]),
    "tl": _build_area([
        (1,0,20),(2,21,27),(3,28,33),(4,34,39),(5,40,44),
        (6,45,48),(7,49,52),(8,53,56),(9,57,59),(10,60,62),
        (11,63,65),(12,66,67),(13,68,69),
    ]),
    "cur": _build_area([
        (1,0,45),(2,46,52),(3,53,58),(4,59,63),(5,64,67),
        (6,68,70),(7,71,72),(8,73,73),(9,74,74),(12,75,75),
    ]),
    "ac": _build_area([
        (1,0,30),(2,31,38),(3,39,45),(4,46,51),(5,52,56),
        (6,57,61),(7,62,65),(8,66,68),(9,69,70),(10,71,72),
        (11,73,73),(12,74,74),(13,75,75),
    ]),
    "soc": _build_area([
        (1,0,35),(2,36,41),(3,42,46),(4,47,50),(5,51,53),
        (6,54,57),(7,58,60),(8,61,63),(9,64,65),(10,66,66),
        (11,67,67),(12,68,68),(13,69,69),
    ]),
    "lav": _build_area([
        (1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,59),
        (6,60,63),(7,64,66),(8,67,68),(9,69,69),(10,70,70),
        (11,71,71),(12,72,72),
    ]),
}

_A12_50_64 = {
    "co": _build_area([
        (1,0,41),(2,42,48),(3,49,54),(4,55,59),(5,60,63),
        (6,64,66),(7,67,69),(8,70,71),(9,72,72),(10,73,73),
        (11,74,74),(12,75,75),
    ]),
    "am": _build_area([
        (1,0,29),(2,30,37),(3,38,44),(4,45,50),(5,51,55),
        (6,56,59),(7,60,62),(8,63,65),(9,66,68),(10,69,69),
        (11,70,70),(12,71,71),
    ]),
    "sco": _build_area([
        (1,0,32),(2,33,39),(3,40,46),(4,47,53),(5,54,59),
        (6,60,63),(7,64,67),(8,68,71),(9,72,74),(10,75,76),
        (11,77,78),(12,79,79),(13,80,80),(14,81,81),
    ]),
    "vc": _build_area([
        (1,0,17),(2,18,26),(3,27,34),(4,35,41),(5,42,47),
        (6,48,52),(7,53,57),(8,58,60),(9,61,63),(10,64,65),
        (11,66,67),(12,68,68),(13,69,69),
    ]),
    "ss": _build_area([
        (1,0,34),(2,35,40),(3,41,45),(4,46,49),(5,50,52),
        (6,53,54),(7,55,55),(8,56,56),(9,57,57),(10,58,58),
        (11,59,59),(12,60,60),
    ]),
    "tl": _build_area([
        (1,0,11),(2,12,19),(3,20,26),(4,27,32),(5,33,37),
        (6,38,43),(7,44,48),(8,49,52),(9,53,55),(10,56,57),
        (11,58,60),(12,61,63),(13,64,66),(14,67,69),
    ]),
    "cur": _build_area([
        (1,0,54),(2,55,57),(3,58,61),(4,62,64),(5,65,66),
        (6,67,69),(7,70,71),(8,72,73),(9,74,74),
    ]),
    "ac": _build_area([
        (1,0,29),(2,30,37),(3,38,44),(4,45,50),(5,51,55),
        (6,56,59),(7,60,62),(8,63,65),(9,66,67),(10,68,69),
        (11,70,70),(12,71,72),(13,73,74),(14,75,75),
    ]),
    "soc": _build_area([
        (1,0,35),(2,36,41),(3,42,46),(4,47,50),(5,51,53),
        (6,54,56),(7,57,59),(8,60,62),(9,63,64),(10,65,65),
        (11,66,67),(12,68,68),(13,69,69),(14,70,71),
    ]),
    "lav": _build_area([
        (1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,59),
        (6,60,62),(7,63,65),(8,66,67),(9,68,69),(10,70,70),
        (11,71,71),(12,72,72),
    ]),
}

_A12_65_74 = {
    "co": _build_area([
        (1,0,41),(2,42,49),(3,50,54),(4,55,58),(5,59,62),
        (6,63,65),(7,66,68),(8,69,70),(9,71,71),(10,72,72),
        (11,73,73),(12,74,74),(13,75,75),
    ]),
    "am": _build_area([
        (1,0,29),(2,30,37),(3,38,44),(4,45,50),(5,51,55),
        (6,56,59),(7,60,62),(8,63,65),(9,66,67),(10,68,69),
        (11,70,70),(12,71,71),(13,72,72),
    ]),
    "sco": _build_area([
        (1,0,32),(2,33,39),(3,40,46),(4,47,53),(5,54,59),
        (6,60,65),(7,66,68),(8,69,71),(9,72,74),(10,75,76),
        (11,77,78),(12,79,79),(13,80,80),(14,81,81),
    ]),
    "vc": _build_area([
        (1,0,15),(2,16,23),(3,24,30),(4,31,36),(5,37,41),
        (6,42,44),(7,45,48),(8,49,52),(9,53,56),(10,57,60),
        (11,61,63),(12,64,65),(13,66,67),(14,68,68),(15,69,69),
    ]),
    "ss": _build_area([
        (1,0,34),(2,35,40),(3,41,45),(4,46,49),(5,50,52),
        (6,53,54),(7,55,55),(8,56,56),(9,57,57),(10,58,58),
        (11,59,59),(12,60,60),
    ]),
    "tl": _build_area([
        (1,0,11),(2,12,19),(3,20,26),(4,27,32),(5,33,37),
        (6,38,43),(7,44,48),(8,49,52),(9,53,55),(10,56,57),
        (11,58,60),(12,61,63),(13,64,66),(14,67,69),
    ]),
    "cur": _build_area([
        (1,0,54),(2,55,57),(3,58,61),(4,62,64),(5,65,66),
        (6,67,69),(7,70,71),(8,72,73),(9,74,74),
    ]),
    "ac": _build_area([
        (1,0,25),(2,26,34),(3,35,42),(4,43,49),(5,50,55),
        (6,56,60),(7,61,64),(8,65,67),(9,68,69),(10,70,71),
        (11,72,73),(12,74,74),(13,75,75),
    ]),
    "soc": _build_area([
        (1,0,35),(2,36,41),(3,42,46),(4,47,50),(5,51,53),
        (6,54,57),(7,58,59),(8,60,62),(9,63,64),(10,65,65),
        (11,66,67),(12,68,68),(13,69,69),(14,70,71),
    ]),
    "lav": _build_area([
        (1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,59),
        (6,60,62),(7,63,65),(8,66,67),(9,68,69),(10,70,70),
        (11,71,71),(12,72,72),
    ]),
}

TAVOLA_A12 = {
    "16-21": _A12_16_21,
    "22-29": _A12_22_29,
    "30-39": _A12_30_39,
    "40-49": _A12_40_49,
    "50-64": _A12_50_64,
    "65-74": _A12_65_74,
}

# ══════════════════════════════════════════════════════════════════════
# TABELLA A.13 — Somma Pp → Punteggio composito (solo fascia 16-21)
# ══════════════════════════════════════════════════════════════════════

def _inv(fwd):
    pairs = []
    for comp, val in fwd.items():
        if isinstance(val, tuple):
            for s in range(val[0], val[1] + 1):
                pairs.append((s, comp))
        elif val is not None:
            pairs.append((val, comp))
    pairs.sort()
    return pairs

def _lookup(pairs, somma):
    if somma is None or not pairs:
        return None
    sums = [p[0] for p in pairs]
    idx = bisect.bisect_right(sums, somma) - 1
    return pairs[idx][1] if idx >= 0 else None

# Le vecchie tavole A.13 (estratte via OCR, errate) sono state sostituite da tabelle_abas.A13.

# PERCENTILI_A13 ora è definita in fondo alla sezione ABAS (da tabelle_abas.py)

CHIAVE_AREA = {
    "comunicazione": "co", "uso_ambiente": "am",
    "competenze_scolastiche": "sco", "vita_a_casa": "vc",
    "salute_sicurezza": "ss", "tempo_libero": "tl",
    "cura_se": "cur", "autocontrollo": "ac",
    "socializzazione": "soc", "lavoro": "lav",
}

def fascia_eta(eta):
    if 16 <= eta <= 21: return "16-21"
    if 22 <= eta <= 29: return "22-29"
    if 30 <= eta <= 39: return "30-39"
    if 40 <= eta <= 49: return "40-49"
    if 50 <= eta <= 64: return "50-64"
    if 65 <= eta <= 74: return "65-74"
    if 75 <= eta <= 89: return "75-89"
    return None

# ══════════════════════════════════════════════════════════════════════
# ABAS-II: Forme aggiuntive — Autovalutazione, Insegnante, Genitore
# ══════════════════════════════════════════════════════════════════════

# ── TAVOLA A.9 — Autovalutazione adulto (grezzo → Pp) ────────────────
_ba = _build_area  # alias locale

TAVOLA_A9 = {
"16-21": {
    "co":  _ba([(1,0,31),(2,32,38),(3,39,44),(4,45,49),(5,50,53),(6,54,56),(7,57,59),(8,60,62),(9,63,65),(10,66,67),(11,68,69),(12,70,71),(13,72,73),(14,74,75)]),
    "am":  _ba([(1,0,29),(2,30,35),(3,36,40),(4,41,44),(5,45,47),(6,48,51),(7,52,54),(8,55,56),(9,57,59),(10,60,62),(11,63,64),(12,65,67),(13,68,69),(14,70,72)]),
    "sco": _ba([(1,0,43),(2,44,47),(3,48,50),(4,51,54),(5,55,58),(6,59,62),(7,63,65),(8,66,69),(9,70,72),(10,73,75),(11,76,77),(12,78,79),(13,80,80),(15,81,81)]),
    "vc":  _ba([(1,0,27),(2,28,34),(3,35,40),(4,41,45),(5,46,49),(6,50,53),(7,54,56),(8,57,58),(9,59,61),(10,62,63),(11,64,65),(12,66,66),(13,67,67),(14,68,69)]),
    "ss":  _ba([(1,0,22),(2,23,29),(3,30,35),(4,36,40),(5,41,44),(6,45,47),(7,48,49),(8,50,52),(9,53,54),(10,55,56),(11,57,57),(12,58,58),(13,59,59),(14,60,60)]),
    "tl":  _ba([(1,0,24),(2,25,31),(3,32,37),(4,38,42),(5,43,46),(6,47,49),(7,50,52),(8,53,55),(9,56,58),(10,59,61),(11,62,64),(12,65,66),(13,67,68),(14,69,69)]),
    "cur": _ba([(1,0,51),(2,52,55),(3,56,60),(4,61,64),(5,65,67),(6,68,69),(7,70,70),(8,71,71),(9,72,72),(10,73,73),(11,74,74),(12,75,75)]),
    "ac":  _ba([(1,0,28),(2,29,35),(3,36,41),(4,42,46),(5,47,50),(6,51,54),(7,55,58),(8,59,61),(9,62,64),(10,65,66),(11,67,69),(12,70,71),(13,72,73),(14,74,75)]),
    "soc": _ba([(1,0,34),(2,35,40),(3,41,45),(4,46,49),(5,50,53),(6,54,56),(7,57,59),(8,60,62),(9,63,64),(10,65,65),(11,66,66),(12,67,67),(13,68,69)]),
    "lav": _ba([(1,0,33),(2,34,40),(3,41,46),(4,47,51),(5,52,55),(6,56,59),(7,60,62),(8,63,64),(9,65,66),(10,67,68),(11,69,69),(12,70,70),(13,71,71),(14,72,72)]),
},
"22-29": {
    "co":  _ba([(1,0,35),(2,36,42),(3,43,48),(4,49,53),(5,54,57),(6,58,60),(7,61,63),(8,64,66),(9,67,68),(10,69,70),(11,71,71),(12,72,73),(13,74,75)]),
    "am":  _ba([(1,0,35),(2,36,41),(3,42,46),(4,47,49),(5,50,53),(6,54,56),(7,57,59),(8,60,61),(9,62,64),(10,65,66),(11,67,68),(12,69,70),(13,71,72)]),
    "sco": _ba([(1,0,46),(2,47,51),(3,52,55),(4,56,58),(5,59,62),(6,63,67),(7,68,71),(8,72,74),(9,75,76),(10,77,77),(11,78,78),(12,79,79),(13,80,80),(14,81,81)]),
    "vc":  _ba([(1,0,32),(2,33,38),(3,39,43),(4,44,47),(5,48,50),(6,51,54),(7,55,57),(8,58,60),(9,61,62),(10,63,64),(11,65,66),(12,67,67),(13,68,69)]),
    "ss":  _ba([(1,0,35),(2,36,40),(3,41,44),(4,45,47),(5,48,50),(6,51,52),(7,53,53),(8,54,55),(9,56,56),(10,57,57),(11,58,58),(12,59,59),(13,60,60)]),
    "tl":  _ba([(1,0,29),(2,30,35),(3,36,40),(4,41,43),(5,44,47),(6,48,50),(7,51,53),(8,54,56),(9,57,59),(10,60,62),(11,63,64),(12,65,66),(13,67,69)]),
    "cur": _ba([(1,0,59),(2,60,62),(3,63,64),(4,65,66),(5,67,67),(6,68,69),(7,70,70),(8,71,71),(9,72,72),(10,73,73),(11,74,74),(12,75,75)]),
    "ac":  _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,51),(5,52,55),(6,56,58),(7,59,61),(8,62,64),(9,65,67),(10,68,69),(11,70,71),(12,72,73),(13,74,75)]),
    "soc": _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,51),(5,52,55),(6,56,58),(7,59,60),(8,61,62),(9,63,64),(10,65,66),(11,67,67),(12,68,68),(13,69,69)]),
    "lav": _ba([(1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,59),(6,60,62),(7,63,65),(8,66,67),(9,68,68),(10,69,69),(11,70,70),(12,71,71),(13,72,72)]),
},
"30-39": {
    "co":  _ba([(1,0,35),(2,36,42),(3,43,48),(4,49,53),(5,54,57),(6,58,61),(7,62,65),(8,66,68),(9,69,70),(10,71,71),(11,72,72),(12,73,73),(13,74,75)]),
    "am":  _ba([(1,0,35),(2,36,41),(3,42,46),(4,47,49),(5,50,53),(6,54,56),(7,57,59),(8,60,61),(9,62,64),(10,65,67),(11,68,69),(12,70,71),(13,72,72)]),
    "sco": _ba([(1,0,46),(2,47,51),(3,52,55),(4,56,59),(5,60,63),(6,64,68),(7,69,72),(8,73,75),(9,76,77),(10,78,78),(11,79,79),(12,80,80),(13,81,81)]),
    "vc":  _ba([(1,0,32),(2,33,38),(3,39,44),(4,45,49),(5,50,53),(6,54,56),(7,57,59),(8,60,62),(9,63,64),(10,65,65),(11,66,66),(12,67,68),(13,69,69)]),
    "ss":  _ba([(1,0,35),(2,36,40),(3,41,44),(4,45,47),(5,48,50),(6,51,52),(7,53,53),(8,54,55),(9,56,56),(10,57,57),(11,58,58),(12,59,60)]),
    "tl":  _ba([(1,0,29),(2,30,35),(3,36,40),(4,41,43),(5,44,47),(6,48,50),(7,51,53),(8,54,56),(9,57,59),(10,60,62),(11,63,65),(12,66,68),(13,69,69)]),
    "cur": _ba([(1,0,59),(2,60,62),(3,63,64),(4,65,66),(5,67,68),(6,69,70),(7,71,71),(8,72,72),(9,73,73),(10,74,74),(12,75,75)]),
    "ac":  _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,52),(5,53,56),(6,57,59),(7,60,63),(8,64,66),(9,67,68),(10,69,70),(11,71,72),(12,73,73),(13,74,75)]),
    "soc": _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,51),(5,52,55),(6,56,58),(7,59,60),(8,61,63),(9,64,65),(10,66,66),(11,67,67),(12,68,68),(13,69,69)]),
    "lav": _ba([(1,0,44),(2,45,50),(3,51,55),(4,56,59),(5,60,62),(6,63,64),(7,65,66),(8,67,67),(9,68,68),(10,69,69),(11,70,70),(12,71,71),(13,72,72)]),
},
"40-49": {
    "co":  _ba([(1,0,35),(2,36,42),(3,43,48),(4,49,53),(5,54,57),(6,58,61),(7,62,65),(8,66,68),(9,69,70),(10,71,72),(11,73,73),(12,74,74),(13,75,75)]),
    "am":  _ba([(1,0,35),(2,36,41),(3,42,46),(4,47,49),(5,50,53),(6,54,57),(7,58,60),(8,61,63),(9,64,66),(10,67,68),(11,69,70),(12,71,71),(13,72,72)]),
    "sco": _ba([(1,0,46),(2,47,51),(3,52,55),(4,56,59),(5,60,64),(6,65,69),(7,70,73),(8,74,76),(9,77,78),(10,79,79),(11,80,80),(13,81,81)]),
    "vc":  _ba([(1,0,32),(2,33,38),(3,39,44),(4,45,49),(5,50,53),(6,54,56),(7,57,59),(8,60,62),(9,63,64),(10,65,66),(11,67,67),(12,68,68),(13,69,69)]),
    "ss":  _ba([(1,0,35),(2,36,40),(3,41,44),(4,45,47),(5,48,50),(6,51,53),(7,54,55),(8,56,56),(9,57,57),(10,58,58),(11,59,59),(12,60,60)]),
    "tl":  _ba([(1,0,29),(2,30,35),(3,36,40),(4,41,43),(5,44,47),(6,48,50),(7,51,53),(8,54,56),(9,57,59),(10,60,62),(11,63,65),(12,66,69)]),
    "cur": _ba([(1,0,61),(2,62,63),(3,64,64),(4,65,66),(5,67,68),(6,69,70),(7,71,71),(8,72,72),(9,73,73),(10,74,74),(12,75,75)]),
    "ac":  _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,52),(5,53,56),(6,57,59),(7,60,63),(8,64,66),(9,67,69),(10,70,71),(11,72,72),(12,73,73),(13,74,75)]),
    "soc": _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,51),(5,52,55),(6,56,58),(7,59,60),(8,61,63),(9,64,65),(10,66,66),(11,67,67),(12,68,68),(13,69,69)]),
    "lav": _ba([(1,0,44),(2,45,50),(3,51,55),(4,56,59),(5,60,62),(6,63,64),(7,65,66),(8,67,67),(9,68,68),(10,69,69),(11,70,70),(12,71,71),(13,72,72)]),
},
"50-64": {
    "co":  _ba([(1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,59),(6,60,62),(7,63,65),(8,66,67),(9,68,69),(10,70,71),(11,72,72),(12,73,73),(13,74,75)]),
    "am":  _ba([(1,0,28),(2,29,37),(3,38,44),(4,45,50),(5,51,55),(6,56,59),(7,60,62),(8,63,65),(9,66,68),(10,69,70),(11,71,71),(12,72,72)]),
    "sco": _ba([(1,0,32),(2,33,40),(3,41,47),(4,48,53),(5,54,58),(6,59,63),(7,64,67),(8,68,70),(9,71,73),(10,74,76),(11,77,77),(12,78,78),(13,79,79)]),
    "vc":  _ba([(1,0,12),(2,13,22),(3,23,31),(4,32,39),(5,40,46),(6,47,52),(7,53,57),(8,58,61),(9,62,64),(10,65,66),(11,67,67),(12,68,68),(13,69,69)]),
    "ss":  _ba([(1,0,29),(2,30,35),(3,36,40),(4,41,43),(5,44,47),(6,48,50),(7,51,53),(8,54,55),(9,56,57),(10,58,59),(11,60,60)]),
    "tl":  _ba([(1,0,6),(2,7,14),(3,15,21),(4,22,27),(5,28,32),(6,33,37),(7,38,42),(8,43,48),(9,49,53),(10,54,60),(11,61,63),(12,64,66),(13,67,69)]),
    "cur": _ba([(1,0,61),(2,62,63),(3,64,65),(4,66,67),(5,68,69),(6,70,71),(7,72,72),(8,73,73),(9,74,74)]),
    "ac":  _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,52),(5,53,56),(6,57,60),(7,61,64),(8,65,66),(9,67,69),(10,70,71),(11,72,72),(12,73,73),(13,74,75)]),
    "soc": _ba([(1,0,36),(2,37,42),(3,43,47),(4,48,51),(5,52,55),(6,56,58),(7,59,60),(8,61,63),(9,64,65),(10,66,66),(11,67,67),(12,68,68),(13,69,69)]),
    "lav": _ba([(1,0,44),(2,45,50),(3,51,55),(4,56,59),(5,60,62),(6,63,64),(7,65,66),(8,67,67),(9,68,68),(10,69,69),(11,70,70),(12,71,71),(13,72,72)]),
},
"65-74": {
    "co":  _ba([(1,0,57),(2,58,61),(3,62,64),(4,65,67),(5,68,69),(6,70,71),(7,72,72),(8,73,73),(9,74,74),(10,75,75)]),
    "am":  _ba([(1,0,12),(2,13,22),(3,23,31),(4,32,39),(5,40,46),(6,47,52),(7,53,57),(8,58,61),(9,62,64),(10,65,66),(11,67,67),(12,68,68),(13,69,69)]),
    "sco": _ba([(1,0,65),(2,66,69),(3,70,73),(4,74,76),(5,77,78),(6,79,79),(7,80,80),(8,81,81)]),
    "vc":  _ba([(1,0,54),(2,55,56),(3,57,59),(4,60,62),(5,63,65),(6,66,67),(7,68,68),(8,69,69)]),
    "ss":  _ba([(1,0,21),(2,22,28),(3,29,34),(4,35,39),(5,40,43),(6,44,48),(7,49,52),(8,53,55),(9,56,57),(10,58,59),(11,60,60)]),
    "tl":  _ba([(1,0,6),(2,7,14),(3,15,21),(4,22,27),(5,28,32),(6,33,38),(7,39,43),(8,44,49),(9,50,54),(10,55,58),(11,59,62),(12,63,65),(13,66,69)]),
    "cur": _ba([(1,0,52),(2,53,57),(3,58,61),(4,62,64),(5,65,66),(6,67,69),(7,70,71),(8,72,72),(9,73,73)]),
    "ac":  _ba([(1,0,25),(2,26,34),(3,35,42),(4,43,49),(5,50,55),(6,56,60),(7,61,64),(8,65,67),(9,68,69),(10,70,71),(11,72,72),(12,73,73),(13,74,75)]),
    "soc": _ba([(1,0,39),(2,40,45),(3,46,50),(4,51,54),(5,55,57),(6,58,59),(7,60,62),(8,63,64),(9,65,65),(10,66,66),(11,67,67),(12,68,68),(13,69,69)]),
    "lav": _ba([(1,0,44),(2,45,50),(3,51,55),(4,56,59),(5,60,62),(6,63,64),(7,65,66),(8,67,67),(9,68,68),(10,69,69),(11,70,70),(12,71,71),(13,72,72)]),
},
# Tabella A.9 Età 75-89 (nessuna sottoscala Lavoro)
"75-89": {
    "co":  _ba([(1,0,41),(2,42,47),(3,48,52),(4,53,56),(5,57,60),(6,61,63),(7,64,65),(8,66,68),(9,69,70),(10,71,72),(11,73,73),(12,74,74),(13,75,75)]),
    "am":  _ba([(1,0,12),(2,13,22),(3,23,31),(4,32,39),(5,40,46),(6,47,52),(7,53,57),(8,58,61),(9,62,64),(10,65,66),(11,67,68),(12,69,70),(13,71,72)]),
    "sco": _ba([(1,0,32),(2,33,40),(3,41,47),(4,48,53),(5,54,58),(6,59,64),(7,65,69),(8,70,73),(9,74,76),(10,77,78),(11,79,79),(12,80,80),(13,81,81)]),
    "vc":  _ba([(1,0,12),(2,13,22),(3,23,31),(4,32,39),(5,40,46),(6,47,52),(7,53,57),(8,58,61),(9,62,64),(10,65,66),(11,67,67),(12,68,68),(13,69,69)]),
    "ss":  _ba([(1,0,21),(2,22,28),(3,29,34),(4,35,39),(5,40,43),(6,44,48),(7,49,52),(8,53,55),(9,56,57),(10,58,58)]),
    "tl":  _ba([(1,0,6),(2,7,14),(3,15,21),(4,22,27),(5,28,32),(6,33,38),(7,39,43),(8,44,48),(9,49,52),(10,53,55),(11,56,57),(12,58,61),(13,62,65)]),
    "cur": _ba([(1,0,52),(2,53,57),(3,58,61),(4,62,64),(5,65,67),(6,68,69),(7,70,71),(8,72,73),(9,74,74),(10,75,75)]),
    "ac":  _ba([(1,0,25),(2,26,34),(3,35,42),(4,43,49),(5,50,55),(6,56,60),(7,61,64),(8,65,67),(9,68,70),(10,71,72),(11,73,73),(12,74,74),(13,75,75)]),
    "soc": _ba([(1,0,39),(2,40,45),(3,46,51),(4,52,56),(5,57,59),(6,60,62),(7,63,64),(8,65,66),(9,67,67),(10,68,68),(11,69,69)]),
},
}

# ── TAVOLA A.1 — Insegnante 17-21 (grezzo → Pp) ─────────────────────
TAVOLA_A1 = {
    "co":  _ba([(1,0,44),(2,45,48),(3,49,51),(4,52,53),(5,54,55),(6,56,56),(7,57,57),(8,58,59),(9,60,61),(10,62,64),(11,65,66)]),
    "am":  _ba([(1,0,27),(2,28,31),(3,32,34),(4,35,36),(5,37,38),(6,39,39),(7,40,40),(8,41,41),(9,42,42),(10,43,43),(11,44,45)]),
    "sco": _ba([(1,0,41),(2,42,44),(3,45,47),(4,48,49),(5,50,52),(6,53,55),(7,56,57),(8,58,59),(9,60,61),(10,62,63),(11,64,66)]),
    "vs":  _ba([(1,0,36),(2,37,40),(3,41,43),(4,44,45),(6,46,46),(7,47,47),(8,48,49),(9,50,51),(10,52,55),(11,56,60)]),
    "ss":  _ba([(1,0,33),(2,34,36),(3,37,39),(4,40,41),(5,42,42),(7,43,43),(8,44,44),(9,45,45),(10,46,46),(11,47,48)]),
    "tl":  _ba([(1,0,24),(2,25,28),(3,29,31),(4,32,33),(5,34,35),(6,36,37),(7,38,39),(8,40,41),(9,42,44),(10,45,47),(11,48,49),(12,50,51)]),
    "cur": _ba([(1,0,48),(2,49,50),(3,51,52),(4,53,54),(6,55,55),(8,56,56),(11,57,57)]),
    "ac":  _ba([(1,0,35),(2,36,39),(3,40,42),(4,43,44),(5,45,45),(6,46,46),(7,47,47),(8,48,50),(9,51,54),(10,55,59),(11,60,63)]),
    "soc": _ba([(1,0,36),(2,37,40),(3,41,43),(4,44,45),(5,46,47),(6,48,49),(7,50,50),(8,51,52),(9,53,55),(10,56,57),(11,58,59),(12,60,60)]),
    "lav": _ba([(1,0,27),(2,28,33),(3,34,38),(4,39,42),(5,43,45),(6,46,49),(7,50,52),(8,53,55),(9,56,57),(10,58,58),(11,59,60),(12,61,63)]),
}

# ── TAVOLA A.5 — Genitore 17-21 (grezzo → Pp) ───────────────────────
TAVOLA_A5_G = {
    "co":  _ba([(1,0,41),(2,42,45),(3,46,48),(4,49,50),(5,51,53),(6,54,57),(7,58,61),(8,62,65),(9,66,68),(10,69,70),(11,71,71),(12,72,72)]),
    "am":  _ba([(1,0,30),(2,31,32),(3,33,34),(4,35,36),(5,37,39),(6,40,43),(7,44,48),(8,49,53),(9,54,58),(10,59,62),(11,63,65),(12,66,67),(13,68,68),(14,69,69)]),
    "sco": _ba([(1,0,32),(2,33,39),(3,40,45),(4,46,50),(5,51,54),(6,55,58),(7,59,61),(8,62,63),(9,64,65),(10,66,66),(11,67,67),(12,68,69)]),
    "vc":  _ba([(1,0,42),(2,43,46),(3,47,49),(4,50,51),(6,52,52),(7,53,54),(8,55,57),(9,58,61),(10,62,65),(11,66,69),(12,70,72),(13,73,75)]),
    "ss":  _ba([(1,0,41),(2,42,45),(3,46,48),(4,49,50),(5,51,52),(6,53,55),(7,56,58),(8,59,60),(9,61,62),(10,63,63),(11,64,64),(12,65,66)]),
    "tl":  _ba([(1,0,32),(2,33,35),(3,36,38),(4,39,40),(5,41,43),(6,44,47),(7,48,51),(8,52,55),(9,56,58),(10,59,61),(11,62,63),(12,64,64),(13,65,66)]),
    "cur": _ba([(1,0,61),(2,62,62),(3,63,63),(4,64,64),(5,65,65),(6,66,66),(7,67,68),(8,69,69),(9,70,70),(11,71,71),(12,72,72)]),
    "ac":  _ba([(1,0,39),(2,40,43),(3,44,46),(4,47,48),(5,49,50),(6,51,53),(7,54,56),(8,57,60),(9,61,64),(10,65,67),(11,68,70),(12,71,73),(13,74,75)]),
    "soc": _ba([(1,0,43),(2,44,47),(3,48,50),(4,51,52),(5,53,53),(6,54,55),(7,56,58),(8,59,61),(9,62,64),(10,65,66),(11,67,68),(12,69,69)]),
    "lav": _ba([(1,0,39),(2,40,44),(3,45,48),(4,49,51),(5,52,53),(6,54,54),(7,55,56),(8,57,58),(9,59,59),(10,60,60),(11,61,61),(12,62,62),(13,63,63)]),
}

# ── TAVOLA A.10 — Autovalutazione compositi per fascia (somma Pp → composito) ───
# Dati letti dalla Tabella A.10 del manuale ABAS-II (edizione italiana).
# Ogni fascia ha le proprie norme; le colonne sl/cl indicano senza/con Lavoro.
# La fascia 75-89 non ha la sottoscala Lavoro (solo 4 colonne).
def _a10_band(gac_sl, gac_cl, dac, das, dap_sl, dap_cl):
    return {
        "gac_sl": _inv(gac_sl), "gac_cl": _inv(gac_cl),
        "dac": _inv(dac), "das": _inv(das),
        "dap_sl": _inv(dap_sl), "dap_cl": _inv(dap_cl),
    }

# Dati grezzi: {min_somma_ponderati: punteggio_composito}
# Fonte: lettura diretta delle immagini PDF del manuale cartaceo

# ── Variabili condivise per TAVOLA_A10 (formato {composito: somma_minima}) ──────
# DAC: fascia 16-21, ceiling comp120=sum39
_A10_DAC_BASE = {47:3,49:4,51:5,53:6,55:7,57:8,59:9,61:10,63:11,65:12,67:13,69:14,
                 70:15,72:16,75:17,77:18,79:19,81:20,84:21,86:22,88:23,90:24,92:25,
                 94:26,96:27,98:28,100:29,102:30,104:31,106:32,108:33,110:34,113:35,
                 115:36,117:37,119:38,120:39}
# DAC: fasce 22-89, ceiling comp120=sum40
_A10_DAC22 =  {47:3,49:4,51:5,53:6,55:7,57:8,59:9,61:10,63:11,65:12,67:13,69:14,
               70:15,72:16,75:17,77:18,79:19,81:20,84:21,86:22,88:23,90:24,92:25,
               94:26,96:27,98:28,100:29,102:30,104:31,106:32,108:33,110:34,113:35,
               115:36,117:37,119:38,120:40}
# DAS: fasce 16-29, ceiling comp120=sum27
_A10_DAS_BASE = {54:2,57:3,60:4,62:5,64:6,66:7,68:8,70:9,72:10,75:11,78:12,81:13,
                 84:14,87:15,89:16,91:17,93:18,95:19,99:20,103:21,107:22,111:23,
                 115:24,118:25,119:26,120:27}
# DAS: fasce 30-89, ceiling comp120=sum26
_A10_DAS26 =  {54:2,57:3,60:4,62:5,64:6,66:7,68:8,70:9,72:10,75:11,78:12,81:13,
               84:14,87:15,89:16,91:17,93:18,95:19,99:20,103:21,107:22,111:23,
               115:24,118:25,120:26}
# DAP_sl: fasce 30-74, ceiling comp120=sum51
_A10_DAP_SL_BASE = {40:4,42:5,44:6,46:7,48:8,50:9,52:10,54:11,56:12,58:13,60:14,
                    62:15,64:16,65:17,67:19,68:20,69:21,70:22,75:25,77:26,79:27,80:28,
                    82:29,84:30,86:31,87:32,89:33,91:34,92:35,94:36,96:37,98:38,
                    100:39,102:40,104:41,106:42,108:43,110:44,112:45,114:46,116:47,
                    117:48,118:49,119:50,120:51}

TAVOLA_A10 = {
# ── Età 16-21 ── formato {composito: somma_minima} ───────────────────────────
"16-21": _a10_band(
    gac_sl={40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
            50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:28,59:30,
            60:32,61:34,62:36,63:38,64:40,65:42,66:44,67:46,68:48,69:50,
            70:52,71:54,72:55,73:56,74:57,75:58,76:59,77:60,78:61,79:62,
            80:63,81:64,82:65,83:66,84:67,85:69,86:70,87:72,88:73,89:75,
            90:76,91:77,92:79,93:80,94:82,95:83,96:85,97:86,98:88,99:89,
            100:91,101:92,102:93,103:95,104:97,105:98,106:100,107:101,108:103,
            109:105,110:106,111:108,112:110,113:111,114:112,115:113,116:115,
            117:116,118:117,119:118,120:120},
    gac_cl={41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:19,50:21,
            51:23,52:25,53:27,55:31,56:33,57:35,58:37,59:39,60:41,
            61:43,62:45,63:47,64:49,65:51,66:53,67:55,68:57,69:59,70:61,
            71:63,72:64,73:65,74:66,75:67,76:68,77:69,78:70,79:71,80:72,
            81:73,82:74,83:75,84:76,85:77,86:79,87:80,88:82,89:83,90:85,
            91:87,92:88,93:90,94:92,95:93,96:95,97:96,98:98,99:100,100:103,
            101:105,102:106,103:108,104:109,105:111,106:113,107:114,108:116,
            109:117,110:119,111:121,112:122,113:123,114:124,115:126,116:127,
            117:129,118:130,120:131},
    dac=_A10_DAC_BASE,
    das=_A10_DAS_BASE,
    dap_sl={40:4,42:5,44:6,46:7,48:8,50:9,51:10,53:11,55:13,57:15,59:17,
            60:19,61:20,62:21,63:22,64:23,65:24,66:25,67:26,68:27,69:28,
            70:29,72:30,74:31,76:32,78:33,79:34,81:35,83:36,84:37,85:38,
            87:39,88:40,90:41,91:42,92:43,93:44,94:45,95:46,96:47,97:48,
            98:49,99:50,100:51,101:52,102:53,103:54,104:55,105:56,108:57,
            109:58,110:59,112:60,114:61,116:62,120:63},
    dap_cl={40:5,42:6,44:7,46:8,48:9,50:10,51:11,53:13,55:15,57:17,59:19,
            60:20,61:21,62:22,63:23,64:24,65:25,66:26,67:27,68:28,69:29,
            70:30,72:31,74:32,76:33,78:34,79:35,81:36,83:37,84:38,85:39,
            87:40,88:41,90:42,91:43,92:44,93:45,94:46,95:47,96:48,97:49,
            98:50,99:51,100:52,101:53,102:54,103:55,104:56,105:57,108:58,
            109:59,110:60,112:61,114:62,116:63,120:65},
),
# ── Età 22-29 ── formato {composito: somma_minima} ───────────────────────────
"22-29": _a10_band(
    gac_sl={40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
            50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,
            60:29,61:30,62:31,63:32,64:33,65:35,66:37,67:39,68:41,69:43,
            70:45,71:47,72:48,73:50,74:51,75:53,76:54,77:55,78:56,79:57,
            80:59,81:61,82:63,83:64,84:65,85:67,86:69,87:71,88:72,89:73,
            90:75,91:76,92:79,93:80,94:82,95:84,96:86,97:88,98:89,99:91,
            100:92,101:93,102:95,103:97,104:98,105:100,106:102,107:104,
            108:105,109:107,110:108,111:110,112:111,113:113,114:115,115:116,
            116:117,117:118,119:119,120:120},
    gac_cl={41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,50:19,
            51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,60:29,
            61:30,62:32,63:33,64:34,65:36,66:38,67:40,68:42,69:44,70:46,
            71:48,72:49,73:51,74:53,75:55,76:57,77:58,78:60,79:62,80:63,
            81:65,82:67,83:68,84:70,85:72,86:74,87:75,88:77,89:79,90:81,
            91:82,92:84,93:86,94:87,95:89,96:91,97:93,98:95,99:97,100:99,
            101:100,102:102,103:104,104:106,105:108,106:110,107:112,108:113,
            109:115,110:117,111:119,112:120,113:122,114:124,115:126,116:127,
            117:129,118:131,119:133,120:134},
    dac=_A10_DAC22,
    das=_A10_DAS_BASE,
    dap_sl={40:4,42:5,44:6,46:7,48:8,50:9,51:10,53:11,55:13,57:15,59:17,
            60:19,61:20,62:21,63:22,64:23,65:24,66:25,67:26,68:27,69:28,
            70:29,72:30,74:31,76:32,78:33,79:34,81:35,83:36,84:37,85:38,
            87:39,88:40,90:41,91:42,92:43,93:44,94:45,95:46,96:47,97:48,
            98:49,99:50,100:51,101:52,102:53,103:54,104:55,105:56,108:57,
            109:58,110:59,112:60,114:61,116:62,120:63},
    dap_cl={40:5,42:6,44:7,46:8,48:9,50:10,51:11,53:13,55:15,57:17,59:19,
            60:20,61:21,62:22,63:23,64:24,65:25,66:26,67:27,68:28,69:29,
            70:30,72:31,74:32,76:33,78:34,79:35,81:36,83:37,84:38,85:39,
            87:40,88:41,90:42,91:43,92:44,93:45,94:46,95:47,96:48,97:49,
            98:50,99:51,100:52,101:53,102:54,103:55,104:56,105:57,108:58,
            109:59,110:60,112:61,114:62,120:64},
),
# ── Età 30-39 ── formato {composito: somma_minima} ───────────────────────────
"30-39": _a10_band(
    gac_sl={40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
            50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,
            60:29,61:30,62:31,63:32,64:33,65:34,66:36,67:38,68:40,69:41,
            70:43,71:44,72:46,73:47,74:49,75:50,76:52,77:53,78:54,79:56,
            80:59,81:60,82:62,83:64,84:65,85:66,86:68,87:70,88:72,89:73,
            90:75,91:77,92:79,93:80,94:82,95:84,96:85,97:87,98:88,99:90,
            100:91,101:93,102:94,103:96,104:97,105:99,106:101,107:103,
            108:104,109:106,110:107,111:108,112:109,113:110,114:112,115:113,
            116:114,119:115,120:116},
    gac_cl={41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,50:19,
            51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,60:29,
            61:30,62:31,63:32,64:34,65:35,66:37,67:39,68:41,69:43,70:45,
            71:47,72:48,73:50,74:52,75:54,76:56,77:58,78:60,79:61,80:63,
            81:65,82:66,83:68,84:69,85:71,86:73,87:75,88:77,89:78,90:80,
            91:81,92:83,93:85,94:87,95:89,96:91,97:93,98:94,99:96,100:98,
            101:100,102:101,103:103,104:105,105:107,106:109,107:111,108:112,
            109:114,110:116,111:118,112:119,113:121,114:122,115:124,116:126,
            117:127,119:128,120:129},
    dac=_A10_DAC22,
    das=_A10_DAS26,
    dap_sl=_A10_DAP_SL_BASE,
    dap_cl={40:5,42:6,44:7,46:8,48:9,50:10,51:11,53:13,55:15,57:17,59:19,
            60:20,61:21,62:22,63:23,64:24,65:25,66:26,67:27,68:28,69:29,
            70:30,72:31,74:32,76:33,78:34,79:35,81:36,83:37,84:38,85:39,
            87:40,88:41,90:42,91:43,92:44,93:45,94:46,95:47,96:48,97:49,
            98:50,99:51,100:52,101:53,102:54,103:55,104:56,105:57,108:58,
            109:59,110:60,112:61,114:62,120:63},
),
# ── Età 40-49 ── formato {composito: somma_minima} ───────────────────────────
"40-49": _a10_band(
    gac_sl={40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
            50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,
            60:29,61:30,62:31,63:32,64:33,65:34,66:36,67:38,68:40,69:41,
            70:43,71:44,72:46,73:47,74:49,75:50,76:52,77:53,78:54,79:56,
            80:59,81:60,82:62,83:64,84:65,85:67,86:69,87:70,88:72,89:73,
            90:75,91:76,92:79,93:80,94:82,95:84,96:86,97:88,98:89,99:91,
            100:92,101:93,102:95,103:97,104:98,105:100,106:102,107:104,
            108:105,109:107,110:108,111:109,112:110,113:112,114:113,115:115,
            116:116,120:117},
    gac_cl={41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,50:19,
            51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,60:29,
            61:30,62:32,63:34,64:36,65:38,66:40,67:42,68:44,69:46,70:48,
            71:49,72:51,73:53,74:55,75:57,76:59,77:61,78:62,79:64,80:66,
            81:68,82:70,83:71,84:73,85:75,86:77,87:79,88:81,89:82,90:84,
            91:85,92:87,93:89,94:91,95:93,96:95,97:97,98:99,99:100,100:102,
            101:104,102:106,103:108,104:110,105:112,106:113,107:115,108:117,
            109:119,110:120,111:122,112:124,113:126,114:127,115:129,116:130,
            120:131},
    dac=_A10_DAC22,
    das=_A10_DAS26,
    dap_sl=_A10_DAP_SL_BASE,
    dap_cl={40:5,42:6,44:7,46:8,48:9,50:10,51:11,53:13,55:15,57:17,59:19,
            60:20,61:21,62:22,63:23,64:24,65:25,66:26,67:27,68:28,69:29,
            70:30,72:31,74:32,76:33,78:34,79:35,81:36,83:37,84:38,85:39,
            87:40,88:41,90:42,91:43,92:44,93:45,94:46,95:47,96:48,97:49,
            98:50,99:51,100:52,101:53,102:54,103:55,104:56,105:57,108:58,
            109:59,110:60,112:61,114:62,120:64},
),
# ── Età 50-64 ── formato {composito: somma_minima} ───────────────────────────
"50-64": _a10_band(
    gac_sl={40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
            50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,
            60:29,61:30,62:31,63:32,64:33,65:35,66:36,67:37,68:39,69:40,
            70:41,71:43,72:45,73:47,74:48,75:50,76:51,77:52,78:53,79:54,
            80:56,81:57,82:59,83:60,84:62,85:63,86:65,87:66,88:67,89:68,
            90:69,91:71,92:72,93:74,94:75,95:77,96:78,97:80,98:81,99:82,
            100:84,101:85,102:87,103:88,104:90,105:91,106:93,107:95,
            108:97,109:99,110:100,111:102,112:104,113:106,114:108,115:110,
            116:112,117:113,118:115,120:117},
    gac_cl={41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,50:19,
            51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,60:29,
            61:30,62:32,63:34,64:36,65:38,66:40,67:42,68:44,69:46,70:48,
            71:49,72:51,73:53,74:55,75:57,76:59,77:61,78:63,79:65,80:68,
            81:70,82:71,83:73,84:75,85:77,86:79,87:81,88:82,89:84,90:86,
            91:88,92:90,93:92,94:93,95:95,96:97,97:99,98:100,99:102,100:104,
            101:106,102:108,103:110,104:112,105:113,106:115,107:117,108:119,
            109:120,110:122,111:124,112:126,113:127,114:129,115:130,
            120:130},
    dac=_A10_DAC22,
    das=_A10_DAS26,
    dap_sl=_A10_DAP_SL_BASE,
    dap_cl={40:5,42:6,44:7,46:8,48:9,50:10,51:11,53:13,55:15,57:17,59:19,
            60:20,61:21,62:22,63:23,64:24,65:25,66:26,67:27,68:28,69:29,
            70:30,72:31,74:32,76:33,78:34,79:35,81:36,83:37,84:38,85:39,
            87:40,88:41,90:42,91:43,92:44,93:45,94:46,95:47,96:48,97:49,
            98:50,99:51,100:52,101:53,102:54,103:55,104:56,105:57,108:58,
            109:59,110:60,112:61,114:62,120:63},
),
# ── Età 65-74 ── formato {composito: somma_minima} ───────────────────────────
"65-74": _a10_band(
    gac_sl={40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
            50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,
            60:29,61:30,62:31,63:32,64:33,65:34,66:35,67:37,68:39,69:41,
            70:43,71:45,72:46,73:47,74:48,75:49,76:50,77:51,78:53,79:54,
            80:56,81:57,82:59,83:60,84:62,85:64,86:65,87:67,88:68,89:69,
            90:70,91:71,92:72,93:73,94:74,95:75,96:76,97:77,98:78,99:79,
            100:80,101:81,102:82,103:83,104:85,105:86,106:87,107:88,
            108:90,109:91,110:92,111:93,112:95,113:97,114:99,115:101,
            116:104,117:106,118:108,120:110},
    gac_cl={41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,50:19,
            51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,60:29,
            61:30,62:31,63:32,64:33,65:34,66:36,67:38,68:40,69:41,70:43,
            71:45,72:47,73:49,74:51,75:52,76:54,77:55,78:57,79:59,80:61,
            81:62,82:64,83:65,84:66,85:68,86:69,87:71,88:73,89:75,90:77,
            91:78,92:79,93:81,94:82,95:84,96:86,97:87,98:89,99:91,100:93,
            101:95,102:97,103:99,104:100,105:102,106:104,107:106,108:108,
            109:110,110:112,111:113,112:115,113:117,114:119,115:120,
            116:122,117:124,118:126,119:132,120:134},
    dac=_A10_DAC22,
    das=_A10_DAS26,
    dap_sl=_A10_DAP_SL_BASE,
    dap_cl={40:5,42:6,44:7,46:8,48:9,50:10,51:11,53:13,55:15,57:17,59:19,
            60:20,61:21,62:22,63:23,64:24,65:25,66:26,67:27,68:28,69:29,
            70:30,72:31,74:32,76:33,78:34,79:35,81:36,83:37,84:38,85:39,
            87:40,88:41,90:42,91:43,92:44,93:45,94:46,95:47,96:48,97:49,
            98:50,99:51,100:52,101:53,102:54,103:55,104:56,105:57,108:58,
            109:59,110:60,112:61,114:62,120:63},
),
# ── Età 75-89 ── solo gac, dac, das, dap (no sl/cl, no lavoro) ───────────────
"75-89": {
    "gac":  _inv({40:9,41:10,42:11,43:12,44:13,45:14,46:15,47:16,48:17,49:18,
                  50:19,51:20,52:21,53:22,54:23,55:24,56:25,57:26,58:27,59:28,
                  60:29,61:30,62:31,63:32,64:33,65:34,66:35,67:37,68:39,69:41,
                  70:43,71:44,72:45,73:46,74:47,75:48,76:49,77:50,78:51,79:53,
                  80:58,81:59,82:60,83:61,84:62,85:63,86:65,87:67,88:68,89:69,
                  90:70,91:71,92:72,93:73,94:74,95:75,96:76,97:77,98:78,99:79,
                  100:80,101:81,102:82,103:83,104:84,105:85,106:86,107:87,
                  108:88,109:89,110:90,111:92,112:93,113:95,114:97,115:99,
                  116:102,117:104,118:106,119:109,120:112}),
    "dac":  _inv(_A10_DAC22),
    "das":  _inv(_A10_DAS26),
    "dap":  _inv({40:4,42:5,44:6,46:7,48:8,50:9,52:10,54:11,56:12,58:13,60:14,
                  62:15,64:16,65:17,67:18,68:19,69:20,70:21,75:23,77:24,79:25,80:26,
                  82:27,84:28,85:29,87:30,89:31,91:32,93:33,94:34,96:35,97:36,98:37,
                  100:38,101:39,102:40,104:41,105:42,106:43,107:44,109:45,112:46,114:47,
                  116:48,118:49,119:50,120:52}),
},
}

# Le vecchie tavole A.2 e A.5c sono state sostituite da tabelle_abas.A2 e tabelle_abas.A6.

# ══════════════════════════════════════════════════════════════════════
# ABAS-II: motore di calcolo con lookup esatto
# ----------------------------------------------------------------------
# Le tavole verificate stanno in tabelle_abas.py (generato dall'Excel
# compilato a mano dal manuale). Ogni tavola viene controllata all'avvio:
# ogni grezzo e ogni somma possibile devono avere uno e un solo valore.
# Niente approssimazioni: se un valore non è in tabella il risultato è
# un errore esplicito, non il valore della riga vicina.
# Le tavole non ancora ritrascritte usano i vecchi dati e l'output lo
# segnala come NON VERIFICATO.
# ══════════════════════════════════════════════════════════════════════
import tabelle_abas as _TA

PERCENTILI_A13 = _TA.PERCENTILI


class TabellaABASError(ValueError):
    pass


def _espandi(tab, nome, contigua=True):
    """{chiave: (min, max)} -> {valore: chiave}, controllando sovrapposizioni e buchi."""
    out = {}
    for chiave, (a, b) in sorted(tab.items(), key=lambda kv: kv[1][0]):
        if b < a:
            raise TabellaABASError(f"{nome}: intervallo rovesciato {a}-{b} per {chiave}")
        for v in range(a, b + 1):
            if v in out:
                raise TabellaABASError(f"{nome}: il valore {v} compare sia per {out[v]} sia per {chiave}")
            out[v] = chiave
    if contigua and out:
        buchi = [v for v in range(min(out), max(out) + 1) if v not in out]
        if buchi:
            raise TabellaABASError(f"{nome}: valori senza corrispondenza {buchi}")
    return out


def _da_vecchia_tabella_grezzi(t):
    """I vecchi dizionari grezzo->Pp sono già espansi."""
    return dict(t)


def _da_vecchia_tabella_comp(pairs):
    """I vecchi elenchi (somma_min, composito) -> {somma: composito} per le somme coperte."""
    out = {}
    for i, (s, comp) in enumerate(pairs):
        fine = pairs[i + 1][0] - 1 if i + 1 < len(pairs) else s
        for v in range(s, fine + 1):
            out[v] = comp
    return out


def _norme(forma, fascia):
    """Restituisce (grezzi, compositi, verificata) per forma e fascia.
    grezzi: {sottoscala: {grezzo: Pp}}; compositi: {colonna: {somma: composito}}."""
    verif = True
    if forma == "etero":
        if fascia in _TA.A12:
            grezzi = {s: _espandi(t, f"A.12 {fascia} {s}") for s, t in _TA.A12[fascia].items()}
            verif = "A12" not in _TA.DA_CONFERMARE
        else:
            grezzi = {s: _da_vecchia_tabella_grezzi(t) for s, t in TAVOLA_A12[fascia].items()}
            verif = False
        comp = {c: _espandi(t, f"A.13 {fascia} {c}") for c, t in _TA.A13[fascia].items()}
    elif forma == "auto":
        if fascia in _TA.A9:
            grezzi = {s: _espandi(t, f"A.9 {fascia} {s}") for s, t in _TA.A9[fascia].items()}
            verif = "A9" not in _TA.DA_CONFERMARE
        else:
            grezzi = {s: _da_vecchia_tabella_grezzi(t) for s, t in TAVOLA_A9[fascia].items()}
            verif = False
        nuove = _TA.A10.get(fascia, {})
        comp = {}
        for c, pairs in TAVOLA_A10[fascia].items():
            if c in nuove:
                comp[c] = _espandi(nuove[c], f"A.10 {fascia} {c}")
                if not c.startswith("dap") and "A10_GAC_DAC_DAS" in _TA.DA_CONFERMARE:
                    verif = False
            else:
                comp[c] = _da_vecchia_tabella_comp(pairs)
                verif = False
    elif forma == "insegnante":
        grezzi = TAVOLA_A1
        comp = {c: _espandi(t, f"A.2 {c}") for c, t in _TA.A2.items()}
    elif forma == "genitore":
        grezzi = TAVOLA_A5_G
        comp = {c: _espandi(t, f"A.6 {c}") for c, t in _TA.A6.items()}
    else:
        raise ValueError(forma)
    return grezzi, comp, verif


def _controlla_tutte_le_tavole():
    """Eseguito all'import: un errore di trascrizione blocca l'app invece di produrre numeri sbagliati."""
    for f in ["16-21", "22-29", "30-39", "40-49", "50-64", "65-74"]:
        _norme("etero", f)
    for f in ["16-21", "22-29", "30-39", "40-49", "50-64", "65-74", "75-89"]:
        _norme("auto", f)
    _norme("insegnante", None)
    _norme("genitore", None)


_NOMI_SUB = {
    "co": "Comunicazione", "am": "Uso dell'ambiente",
    "sco": "Competenze scolastiche", "vc": "Vita a casa",
    "vs": "Vita a scuola", "ss": "Salute e sicurezza",
    "tl": "Tempo libero", "cur": "Cura di sé",
    "ac": "Autocontrollo", "soc": "Socializzazione", "lav": "Lavoro",
}
_SIGLE = {"co": "Co", "am": "Am", "sco": "Sco", "vc": "VC", "vs": "VS", "ss": "SS",
          "tl": "TL", "cur": "Cur", "ac": "Ac", "soc": "Soc", "lav": "Lav"}


def descrizione_qualitativa(c):
    """Fasce del protocollo ABAS-II (curva normale, pagina 11)."""
    if c <= 70: return "Estremamente basso"
    if c <= 79: return "Al limite"
    if c <= 89: return "Sotto la media"
    if c <= 109: return "Nella media"
    if c <= 119: return "Sopra la media"
    if c <= 129: return "Alto"
    return "Estremamente alto"


_TAVOLE = {"etero": ("A.12", "A.13", "A13"), "auto": ("A.9", "A.10", "A10"),
           "insegnante": ("A.1", "A.2", "A2"), "genitore": ("A.5", "A.6", "A6")}


def _calcola(forma, fascia, grezzi_in, ha_lavoro, supposizioni=None, omessi=None):
    """Calcolo completo come nella Pagina riassuntiva e nelle Analisi supplementari del protocollo."""
    grezzi_t, comp_t, verificata = _norme(forma, fascia)
    tav_pp, tav_comp, chiave_ic = _TAVOLE[forma]
    pratico = "vs" if forma == "insegnante" else "vc"
    # Insegnante e genitore: tavole A.2/A.6 con una sola colonna, il DAP arriva a 76
    # (4 sottoscale x 19), quindi Lavoro non entra nei compositi.
    lavoro_nei_compositi = ha_lavoro and forma in ("etero", "auto") and fascia != "75-89"

    errori, pp = [], {}
    aree = []
    for sub, grezzo in grezzi_in.items():
        val = grezzi_t.get(sub, {}).get(int(grezzo))
        if val is None:
            errori.append(f"{_NOMI_SUB[sub]}: grezzo {grezzo} non presente in tabella")
        pp[sub] = val
        aree.append(sub)

    domini = {
        "DAC": ["co", "sco", "ac"],
        "DAS": ["tl", "soc"],
        "DAP": ["am", pratico, "ss", "cur"] + (["lav"] if lavoro_nei_compositi else []),
    }
    unica = fascia == "75-89" or forma in ("insegnante", "genitore")
    if unica:
        col = {"GAC": "gac", "DAC": "dac", "DAS": "das", "DAP": "dap"}
    else:
        suf = "cl" if lavoro_nei_compositi else "sl"
        col = {"GAC": f"gac_{suf}", "DAC": "dac", "DAS": "das", "DAP": f"dap_{suf}"}
    ic = _TA.IC[f"{chiave_ic}|{fascia or '17-21'}"]

    somme = {d: (sum(pp[a] for a in a_) if all(pp.get(a) is not None for a in a_) else None)
             for d, a_ in domini.items()}
    somme["GAC"] = sum(somme[d] for d in domini) if all(somme[d] is not None for d in domini) else None

    compositi = {}
    for d in ["GAC", "DAC", "DAS", "DAP"]:
        s = somme[d]
        if s is None:
            continue
        c = comp_t[col[d]].get(s)
        if c is None:
            errori.append(f"{d}: somma dei Pp {s} non presente nella tavola dei compositi")
            continue
        compositi[d] = {
            "somma": s, "composito": c, "percentile": PERCENTILI_A13[c],
            "ic90": (c - ic["90"][col[d]], c + ic["90"][col[d]]),
            "ic95": (c - ic["95"][col[d]], c + ic["95"][col[d]]),
            "descrizione": descrizione_qualitativa(c),
        }

    # Analisi supplementari: media dei Pp delle aree che entrano nel GAC e scarto di ogni area
    aree_gac = [a for d in ["DAC", "DAS", "DAP"] for a in domini[d]]
    media = None
    if all(pp.get(a) is not None for a in aree_gac):
        media = sum(pp[a] for a in aree_gac) / len(aree_gac)
    differenze = {}
    for a, b in [("DAC", "DAS"), ("DAC", "DAP"), ("DAS", "DAP")]:
        if a in compositi and b in compositi:
            differenze[f"{a}-{b}"] = compositi[a]["composito"] - compositi[b]["composito"]

    note = []
    if ha_lavoro and not lavoro_nei_compositi:
        note.append("Lavoro è riportato come area ma non entra nei compositi"
                    + (" (fascia 75-89)." if fascia == "75-89" else " (tavola con colonna unica)."))
    tot_omessi = sum((omessi or {}).values())
    if tot_omessi:
        note.append(f"ATTENZIONE: {tot_omessi} item senza risposta, conteggiati come 0: "
                    "i punteggi delle aree indicate possono essere sottostimati.")
    if not verificata:
        note.append("ATTENZIONE: per questa forma e fascia alcune tavole normative devono ancora essere "
                    "confrontate con il manuale cartaceo. Non usare questi punteggi a fini clinici.")
    if errori:
        note.append("ERRORE: " + "; ".join(errori) + ".")

    return {
        "tav_pp": tav_pp, "tav_comp": tav_comp, "aree": aree, "grezzi": grezzi_in, "pp": pp,
        "supposizioni": supposizioni or {}, "omessi": omessi or {}, "domini": domini, "compositi": compositi,
        "media": media, "aree_gac": aree_gac, "differenze": differenze, "note": note,
        "lavoro_nei_compositi": lavoro_nei_compositi,
    }


_STILE_ABAS = ("border-collapse:collapse;margin:6px 0 14px 0;font-size:13px")
_TD = "border:1px solid #CBD5E1;padding:3px 8px;text-align:center"
_TH = "border:1px solid #CBD5E1;padding:3px 8px;background:#E0F2F1;text-align:center"


def _html_abas(intestazione, r):
    def riga(celle, th=False):
        st_ = _TH if th else _TD
        return "<tr>" + "".join(f"<td style='{st_}'>{c}</td>" for c in celle) + "</tr>"

    h = [f"<p>{' · '.join(f'<strong>{k}:</strong> {v}' for k, v in intestazione.items())}</p>"]

    # 1. Conversione del punteggio grezzo in punteggio ponderato
    h.append(f"<p><strong>Conversione del punteggio grezzo in punteggio ponderato</strong> (tab. {r['tav_pp']})</p>")
    h.append(f"<table style='{_STILE_ABAS}'>")
    con_supp = bool(r["supposizioni"])
    con_om = any(r["omessi"].values())
    h.append(riga(["Area adattiva", "P.ggio grezzo", "P.ggio ponderato"] + (["Risposte 'suppongo'"] if con_supp else [])
                  + (["Item senza risposta"] if con_om else []), True))
    for a in r["aree"]:
        nome = f"{_NOMI_SUB[a]} ({_SIGLE[a]})"
        if a == "lav" and not r["lavoro_nei_compositi"]:
            nome += " *"
        pp = r["pp"][a] if r["pp"][a] is not None else "ERRORE"
        h.append(riga([nome, r["grezzi"][a], pp] + ([r["supposizioni"].get(a, 0)] if con_supp else [])
                      + ([r["omessi"].get(a, 0)] if con_om else [])))
    h.append("</table>")

    # 2. Conversione della somma dei p.ggi ponderati in p.ggio composito
    h.append(f"<p><strong>Conversione della somma dei punteggi ponderati in punteggio composito</strong> (tab. {r['tav_comp']})</p>")
    h.append(f"<table style='{_STILE_ABAS}'>")
    h.append(riga(["Composito", "Somma p.ggi ponderati", "P.ggio composito", "Percentile",
                   "Int. confidenza 90%", "Int. confidenza 95%", "Descrizione qualitativa"], True))
    nomi = {"GAC": "GAC", "DAC": "Concettuale (DAC)", "DAS": "Sociale (DAS)", "DAP": "Pratico (DAP)"}
    for d in ["GAC", "DAC", "DAS", "DAP"]:
        c = r["compositi"].get(d)
        if c is None:
            h.append(riga([nomi[d], "–", "non calcolabile", "", "", "", ""]))
        else:
            h.append(riga([nomi[d], c["somma"], f"<strong>{c['composito']}</strong>", c["percentile"],
                           f"{c['ic90'][0]}–{c['ic90'][1]}", f"{c['ic95'][0]}–{c['ic95'][1]}", c["descrizione"]]))
    h.append("</table>")

    # 3. Analisi supplementari (parte calcolabile senza le tavole dell'Appendice B)
    if r["media"] is not None:
        n = len(r["aree_gac"])
        h.append(f"<p><strong>Analisi supplementari</strong>: media dei punteggi ponderati ({n} aree) = "
                 f"{r['media']:.2f}</p>")
        h.append(f"<table style='{_STILE_ABAS}'>")
        h.append(riga(["Dominio", "Area", "P.ggio ponderato", "Differenza dalla media"], True))
        for d in ["DAC", "DAS", "DAP"]:
            for a in r["domini"][d]:
                diff = r["pp"][a] - r["media"]
                h.append(riga([d, _NOMI_SUB[a], r["pp"][a], f"{diff:+.2f}"]))
        h.append("</table>")
    if r["differenze"]:
        h.append(f"<table style='{_STILE_ABAS}'>")
        h.append(riga(["Confronto", "Punteggio 1", "Punteggio 2", "Differenza"], True))
        nomi_c = {"DAC-DAS": "Concettuale-Sociale", "DAC-DAP": "Concettuale-Pratico", "DAS-DAP": "Sociale-Pratico"}
        for k, v in r["differenze"].items():
            a, b = k.split("-")
            h.append(riga([nomi_c[k], f"{a} {r['compositi'][a]['composito']}",
                           f"{b} {r['compositi'][b]['composito']}", f"{v:+d}"]))
        h.append("</table>")
        h.append("<p style='font-size:12px;color:#555'>Valori critici, punti di forza/debolezza (F/D) e "
                 "frequenze nel campione di standardizzazione richiedono le tavole B-15/B-27 dell'Appendice B, "
                 "non incluse nel calcolatore.</p>")
    note = list(r["note"])
    if any(a == "lav" and not r["lavoro_nei_compositi"] for a in r["aree"]):
        note.insert(0, "* Lavoro non entra nei compositi.")
    if note:
        h.append("<p style='color:#B91C1C'>" + " ".join(note) + "</p>")
    return "".join(h)


def _risultato_abas(intestazione, r):
    """Formato restituito alle funzioni chiamanti: HTML pronto per l'email più i valori principali."""
    out = {"_html": _html_abas(intestazione, r)}
    for d, c in r["compositi"].items():
        out[d] = c["composito"]
    return out


def _grezzi_da_item(dati, ha_lavoro):
    """Somma degli item per area; le risposte mancanti contano 0 e vengono segnalate."""
    risposte = dati.get('risposte', {})
    suppongo = dati.get('suppongo', {})
    grezzi, supp, omessi = {}, {}, {}
    for area in AREE_ABAS:
        if area == 'lavoro' and not ha_lavoro:
            continue
        k = CHIAVE_AREA[area]
        valori = risposte.get(area, [])
        grezzi[k] = sum(v for v in valori if v is not None)
        omessi[k] = sum(v is None for v in valori)
        supp[k] = sum(bool(x) for x in suppongo.get(area, []))
    return grezzi, supp, omessi


def calcola_abas(risposte_abas):
    eta = risposte_abas.get('eta', 0)
    ha_lavoro = risposte_abas.get('ha_lavoro', False)
    fascia = fascia_eta(eta)
    if not fascia or fascia == "75-89":
        return {"Forma": "Eterovalutazione adulto", "Età": f"{eta} anni",
                "Nota": "Tavole normative di eterovalutazione disponibili solo per 16-74 anni."}
    grezzi, supp, omessi = _grezzi_da_item(risposte_abas, ha_lavoro)
    r = _calcola("etero", fascia, grezzi, ha_lavoro, supp, omessi)
    return _risultato_abas({"Forma": "Eterovalutazione adulto", "Età": f"{eta} anni",
                            "Fascia normativa": fascia, "Lavoro": "Sì" if ha_lavoro else "No"}, r)


def calcola_abas_autovalutazione(dati):
    eta = dati.get("eta", 0)
    fascia = fascia_eta(eta)
    if not fascia:
        return {"Forma": "Autovalutazione adulto", "Nota": f"Età {eta} fuori range (16-89)"}
    ha_lavoro = dati.get("ha_lavoro", False) and fascia != "75-89"
    if "risposte" in dati:   # protocollo compilato item per item nell'app
        grezzi, supp, omessi = _grezzi_da_item(dati, ha_lavoro)
    else:                    # grezzi totali già calcolati sul cartaceo
        subs = ["co", "am", "sco", "vc", "ss", "tl", "cur", "ac", "soc"] + (["lav"] if ha_lavoro else [])
        grezzi, supp, omessi = {k: dati.get("grezzi", {}).get(k, 0) for k in subs}, None, None
    r = _calcola("auto", fascia, grezzi, ha_lavoro, supp, omessi)
    return _risultato_abas({"Forma": "Autovalutazione adulto", "Età": f"{eta} anni", "Fascia normativa": fascia,
                            "Lavoro": "Sì" if ha_lavoro else "No"}, r)


def _calcola_17_21(forma, nome, pratico, dati):
    eta = dati.get("eta", 0)
    ha_lavoro = dati.get("ha_lavoro", False)
    if not (17 <= eta <= 21):
        return {"Forma": nome, "Nota": f"Età {eta} non supportata (17-21 anni)"}
    subs = ["co", "am", "sco", pratico, "ss", "tl", "cur", "ac", "soc"] + (["lav"] if ha_lavoro else [])
    supp = omessi = None
    if dati.get("risposte"):   # protocollo compilato item per item nell'app
        grezzi = {k: sum(v for v in dati["risposte"][k] if v is not None) for k in subs}
        omessi = {k: sum(v is None for v in dati["risposte"][k]) for k in subs}
        supp = {k: sum(bool(x) for x in dati["suppongo"][k]) for k in subs}
    else:
        grezzi = {k: dati.get("grezzi", {}).get(k, 0) for k in subs}
    r = _calcola(forma, None, grezzi, ha_lavoro, supp, omessi)
    return _risultato_abas({"Forma": nome, "Età": f"{eta} anni", "Fascia normativa": "17-21",
                            "Lavoro": "Sì" if ha_lavoro else "No"}, r)



# ══════════════════════════════════════════════════════════════════════
# ABAS-II Genitore (libretto 5-21 anni): struttura del protocollo
# Il testo delle domande non è nel codice: viene letto da item_abas_genitore.json,
# generato dall'Excel compilato dal clinico a partire dal proprio protocollo.
# Finché il file manca o è incompleto, l'app chiede i punteggi grezzi totali.
# ══════════════════════════════════════════════════════════════════════
import json as _json
import os as _os

AREE_GENITORE = [  # (sigla, nome, dominio, numero di item nel libretto)
    ("co", "Comunicazione", "DAC", 24),
    ("am", "Uso dell'ambiente", "DAP", 23),
    ("sco", "Competenze scolastiche", "DAC", 23),
    ("vc", "Vita a casa", "DAP", 25),
    ("ss", "Salute e sicurezza", "DAP", 22),
    ("tl", "Tempo libero", "DAS", 22),
    ("cur", "Cura di sé", "DAP", 24),
    ("ac", "Autocontrollo", "DAC", 25),
    ("soc", "Socializzazione", "DAS", 23),
    ("lav", "Lavoro", "–", 21),
]


def _carica_item(nome_file, struttura):
    percorso = _os.path.join(_os.path.dirname(_os.path.abspath(__file__)), nome_file)
    if not _os.path.exists(percorso):
        return None
    with open(percorso, encoding="utf-8") as f:
        dati = _json.load(f)
    for sigla, nome, _, n in struttura:
        testi = dati.get(sigla, [])
        if len(testi) != n or not all(isinstance(t, str) and t.strip() for t in testi):
            raise ValueError(f"{nome_file}: l'area {nome} deve avere {n} item compilati, ne ha {len(testi)}")
    return dati


ITEM_GENITORE = _carica_item("item_abas_genitore.json", AREE_GENITORE)


def calcola_abas_insegnante(dati):
    return _calcola_17_21("insegnante", "Insegnante (17-21)", "vs", dati)


def calcola_abas_genitore(dati):
    return _calcola_17_21("genitore", "Genitore (17-21)", "vc", dati)


_controlla_tutte_le_tavole()



# ══════════════════════════════════════════════════════════════════════
# Funzioni di Calcolo dei Punteggi — Test esistenti
# ══════════════════════════════════════════════════════════════════════

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
        interpretazione = "Livello significativo di affaticamento e irrequietezza mentale (punteggio >= 22)"
    else:
        interpretazione = "Livello non significativo di affaticamento e irrequietezza mentale (punteggio < 22)"
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
    somma_percentuali = sum(risposte)
    punteggio_medio = round(somma_percentuali / 28, 2)
    if punteggio_medio >= 30:
        interpretazione = "Punteggio indicativo di possibile disturbo dissociativo clinicamente significativo (>= 30)"
    else:
        interpretazione = "Punteggio non indicativo di disturbo dissociativo clinicamente significativo (< 30)"
    return {'interpretazione': interpretazione, 'punteggio_medio': punteggio_medio}


# ── Funzione Principale di Calcolo ────────────────────────────────────

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
    if 'des2' in test_compilati:
        risultati['DES-II'] = calcola_des2(risposte['des2'])
    if 'mews' in test_compilati:
        risultati['MEWS'] = calcola_mews(risposte['mews'])
    if 'stai_y2' in test_compilati:
        risultati['STAI-Y-2'] = calcola_stai_y2(risposte['stai_y2'])
    if 'stai_y1' in test_compilati:
        risultati['STAI-Y-1'] = calcola_stai_y1(risposte['stai_y1'])
    if 'abas' in test_compilati:
        risultati['ABAS-II'] = calcola_abas(risposte['abas'])
    if 'abas_auto' in test_compilati:
        risultati['ABAS-II (Autovalutazione)'] = calcola_abas_autovalutazione(risposte['abas_auto'])
    if 'abas_ins' in test_compilati:
        risultati['ABAS-II (Insegnante)'] = calcola_abas_insegnante(risposte['abas_ins'])
    if 'abas_gen' in test_compilati:
        risultati['ABAS-II (Genitore)'] = calcola_abas_genitore(risposte['abas_gen'])
    return risultati


# ── Funzione di Formattazione Email ──────────────────────────────────

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
            if "_html" in res:
                html += f"<h3>{test}</h3>" + res["_html"]
                continue
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
