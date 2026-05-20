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

TAVOLA_A12 = {
    "16-21": _A12_16_21,
    "22-29": _A12_22_29,
    "30-39": _A12_30_39,
    "40-49": _A12_40_49,
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

_GAC_SL_16_21 = _inv({
    40:9, 41:10, 42:11, 43:12, 44:13, 45:14, 46:15, 47:16, 48:17,
    49:18, 50:19, 51:20, 52:21, 53:22,
    54:(23,24), 55:(25,26), 56:(27,28), 57:(29,30), 58:(31,32),
    59:(33,34), 60:(35,36), 61:(37,38), 62:(39,40), 63:(41,42),
    64:(43,44), 65:(45,46), 66:(47,48), 67:(49,50), 68:(51,52),
    69:(53,54), 70:(55,56),
    71:57, 72:58, 73:59, 74:60, 75:61, 76:62, 77:63, 78:64, 79:65,
    80:66, 81:67, 82:68, 83:69, 84:70, 85:71, 86:72, 87:73, 88:74,
    89:75, 90:76, 91:77,
    92:(78,79), 93:(80,81), 94:(82,83), 95:(84,85), 96:(86,87),
    97:(88,89), 98:(90,91), 99:(92,93),
    100:94, 101:(95,96), 102:97, 103:98, 104:(99,100),
    105:101, 106:102, 107:(103,104), 108:105, 109:106,
    110:107, 111:(108,109),
    112:110, 113:111, 114:112, 115:113, 116:114,
    117:115, 118:116, 119:117, 120:(118,125),
})

_GAC_CL_16_21 = _inv({
    40:10, 41:11, 42:12, 43:13, 44:14, 45:15, 46:16, 47:17, 48:18,
    49:19, 50:20, 51:21, 52:22, 53:23, 54:24,
    55:(25,26), 56:(27,28), 57:(29,30), 58:(31,32), 59:(33,34),
    60:(35,36), 61:(37,38), 62:(39,40), 63:(41,42), 64:(43,44),
    65:(45,46), 66:(47,48), 67:(49,50), 68:(51,52), 69:(53,54),
    70:(55,56), 71:(57,58), 72:(59,60), 73:(61,62), 74:(63,64),
    75:65, 76:(66,67), 77:(68,69), 78:(70,71), 79:72,
    80:(73,74), 81:(75,76), 82:(77,78), 83:79,
    84:(80,81), 85:(82,83), 86:84, 87:(85,86), 88:(87,88), 89:89,
    90:(90,91), 91:(92,93), 92:94, 93:(95,96), 94:97,
    95:(98,99), 96:100, 97:(101,102), 98:103, 99:(104,105),
    100:106, 101:(107,108), 102:109, 103:(110,111), 104:112,
    105:113, 106:114, 107:(115,116), 108:117, 109:118,
    110:119, 111:120, 112:(121,122), 113:123, 114:124,
    115:125, 116:126, 117:127, 118:128, 119:129,
    120:(130,138),
})

_DAC_16_21 = _inv({
    49:3, 51:4, 53:5, 55:6, 57:7, 59:8, 61:9, 63:10, 65:11,
    67:12, 69:13, 70:14, 72:15, 74:16, 76:17, 78:18, 80:19,
    82:20, 83:21, 85:22, 87:23, 89:24, 90:25, 92:26, 94:27,
    95:28, 97:29, 99:30, 100:31, 102:32, 104:33, 106:34,
    108:35, 110:36, 112:37, 116:38, 120:(39,57),
})

_DAS_16_21 = _inv({
    54:2, 57:3, 60:4, 62:5, 64:6, 66:7, 68:8, 70:9, 72:10,
    75:11, 78:12, 81:13, 84:14, 87:15, 90:16, 92:17,
    95:18, 97:19, 99:20, 101:21, 104:22, 107:23, 110:24,
    114:25, 119:26, 120:(27,38),
})

_DAP_SL_16_21 = _inv({
    43:4, 45:5, 47:6, 49:7, 51:8, 53:9, 55:10, 57:11, 59:12,
    61:13, 63:14, 65:15, 67:16, 69:17, 71:18, 73:19, 75:20,
    76:21, 77:22, 78:23, 79:24, 80:25, 81:26, 83:27, 84:28,
    85:29, 86:30, 87:31, 88:32, 89:33, 90:34, 92:35, 93:36,
    94:37, 95:38, 96:39, 98:40, 99:41, 100:42, 102:43, 103:44,
    105:45, 107:46, 109:47, 111:48, 113:49, 115:50, 117:51,
    120:(52,57),
})

_DAP_CL_16_21 = _inv({
    40:5, 42:6, 44:7, 46:8, 48:9, 50:10, 51:11, 52:12, 53:13,
    54:14, 55:15, 56:16, 57:17, 58:18, 59:19, 60:20, 61:21,
    62:22, 63:23, 64:24, 65:25, 66:26, 67:27, 68:28, 69:29,
    70:30, 72:31, 73:32, 75:33, 76:34, 78:35, 79:36, 81:37,
    82:38, 83:39, 85:40, 86:41, 87:42, 89:43, 90:44, 91:45,
    92:46, 93:47, 94:48, 95:49, 96:50, 97:51, 99:52, 100:53,
    101:54, 102:55, 103:56, 104:57, 106:58, 108:59, 109:60,
    111:61, 113:62, 116:63, 120:(64,69),
})

TAVOLA_A13 = {
    "16-21": {
        "gac_sl": _GAC_SL_16_21,
        "gac_cl": _GAC_CL_16_21,
        "dac":    _DAC_16_21,
        "das":    _DAS_16_21,
        "dap_sl": _DAP_SL_16_21,
        "dap_cl": _DAP_CL_16_21,
    },
}

PERCENTILI_A13 = {
    40:"<0.1", 41:"<0.1", 42:"<0.1", 43:"<0.1", 44:"<0.1",
    45:"<0.1", 46:"<0.1", 47:"<0.1", 48:"<0.1", 49:"<0.1",
    50:"<0.1", 51:"0.1",  52:"0.1",  53:"0.1",  54:"0.1",
    55:"0.1",  56:"0.2",  57:"0.2",  58:"0.3",  59:"0.4",
    60:"0.5",  61:"1",    62:"1",    63:"1",    64:"1",
    65:"1",    66:"1",    67:"2",    68:"2",    69:"2",
    70:"3",    71:"3",    72:"5",    73:"5",    74:"6",
    75:"7",    76:"8",    77:"9",    78:"10",   79:"12",
    80:"13",   81:"14",   82:"16",   83:"18",   84:"19",
    85:"21",   86:"23",   87:"25",   88:"27",   89:"30",
    90:"32",   91:"34",   92:"37",   93:"39",   94:"42",
    95:"45",   96:"46",   97:"47",   98:"50",   99:"53",
    100:"55",  101:"58",  102:"61",  103:"63",  104:"66",
    105:"68",  106:"70",  107:"73",  108:"75",  109:"77",
    110:"79",  111:"81",  112:"82",  113:"84",  114:"86",
    115:"87",  116:"88",  117:"90",  118:">90", 119:">90", 120:">90",
}

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
    return None

def _grezzo_a_pp(area_key, raw, fascia):
    return TAVOLA_A12.get(fascia, {}).get(area_key, {}).get(raw)

def _somma_a_composito(colonna, somma, fascia):
    pairs = TAVOLA_A13.get(fascia, {}).get(colonna, [])
    return _lookup(pairs, somma)

# ── Funzione principale ABAS-II ───────────────────────────────────────
def calcola_abas(risposte_abas):
    import datetime
    eta = risposte_abas.get('eta', 0)
    ha_lavoro = risposte_abas.get('ha_lavoro', False)
    risposte = risposte_abas.get('risposte', {})
    suppongo = risposte_abas.get('suppongo', {})
    fascia = fascia_eta(eta)

    risultato = {}
    risultato['Età soggetto'] = f"{eta} anni"
    risultato['Fascia normativa'] = fascia if fascia else "non supportata (>49 anni)"
    risultato['Ha un lavoro'] = 'Sì' if ha_lavoro else 'No'

    if not fascia:
        risultato['Nota'] = 'Tavole normative non disponibili per questa fascia d\'età'
        return risultato

    # Punteggi per area
    pp_per_area = {}
    for area, info in AREE_ABAS.items():
        if area == 'lavoro' and not ha_lavoro:
            continue
        chiave = CHIAVE_AREA[area]
        r = risposte.get(area, [])
        grezzo = sum(r)
        pp = _grezzo_a_pp(chiave, grezzo, fascia)
        n_supp = sum(suppongo.get(area, []))
        pp_per_area[chiave] = pp
        pp_str = str(pp) if pp is not None else 'N/D'
        risultato[f'{info["label"]} (grezzo/Pp/supp)'] = f"{grezzo}/{pp_str}/{n_supp}"

    # Domini e compositi
    dac_aree = ['co', 'sco', 'ac']
    das_aree = ['tl', 'soc']
    dap_sl_aree = ['am', 'vc', 'ss', 'cur']
    dap_cl_aree = ['am', 'vc', 'ss', 'cur', 'lav']

    def somma_pp(aree):
        vals = [pp_per_area.get(a) for a in aree]
        return sum(vals) if all(v is not None for v in vals) else None

    dac_sum = somma_pp(dac_aree)
    das_sum = somma_pp(das_aree)
    dap_sum = somma_pp(dap_cl_aree if ha_lavoro else dap_sl_aree)

    if fascia == "16-21":
        col_dap = 'dap_cl' if ha_lavoro else 'dap_sl'
        col_gac = 'gac_cl' if ha_lavoro else 'gac_sl'

        comp_dac = _somma_a_composito('dac', dac_sum, fascia) if dac_sum else None
        comp_das = _somma_a_composito('das', das_sum, fascia) if das_sum else None
        comp_dap = _somma_a_composito(col_dap, dap_sum, fascia) if dap_sum else None
        gac_sum = (dac_sum or 0) + (das_sum or 0) + (dap_sum or 0)
        comp_gac = _somma_a_composito(col_gac, gac_sum, fascia) if (dac_sum and das_sum and dap_sum) else None

        def fmt(comp):
            if comp is None: return 'N/D'
            perc = PERCENTILI_A13.get(comp, '–')
            return f"{comp} ({perc}° percentile)"

        risultato['GAC (composito)'] = fmt(comp_gac)
        risultato['DAC – Dominio Concettuale'] = fmt(comp_dac)
        risultato['DAS – Dominio Sociale'] = fmt(comp_das)
        risultato['DAP – Dominio Pratico'] = fmt(comp_dap)
    else:
        nota = (f"Punteggi compositi non disponibili per fascia {fascia}: "
                "tavole A.13 non inserite. Disponibili solo punteggi grezzi e ponderati.")
        risultato['Nota compositi'] = nota

    return risultato


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
