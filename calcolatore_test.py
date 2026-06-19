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

# ── Tabelle A.13 per fasce 22-74 ─────────────────────────────────────
# Fonte: pagine 23-30 del PDF (ruotate 180°). Formato: {composito: min_sum_ponderati}

_DAC_22_29 = _inv({
    75:24, 78:25, 80:26, 81:27, 83:28, 87:30, 90:31,
    92:32, 94:33, 96:34, 98:35, 100:36, 103:37, 106:38,
    116:39, 125:(40,57),
})
_DAS_22_29 = _inv({
    63:13, 69:14, 73:15, 76:16, 79:17, 83:18, 85:19,
    89:20, 93:21, 97:22, 105:24, 108:25, 112:26, 117:27,
    125:(28,38),
})
_DAP_SL_22_29 = _inv({
    75:33, 77:34, 79:35, 81:36, 83:37, 85:38, 87:39,
    89:40, 91:41, 93:42, 95:43, 99:45, 101:46, 104:47,
    106:48, 109:49, 112:50, 116:51, 125:(52,76),
})
_DAP_CL_22_29 = _inv({
    63:32, 69:33, 74:34, 76:35, 78:36, 80:37, 83:38,
    85:39, 88:40, 90:41, 93:42, 96:43, 99:44, 102:45,
    105:46, 108:47, 111:48, 114:49, 125:(50,65),
})
_GAC_SL_22_29 = _inv({
    62:67, 63:68, 64:69, 65:70, 66:71, 67:72, 68:73,
    69:74, 70:75, 71:76, 72:77, 73:78, 74:79, 75:81,
    76:83, 77:85, 78:87, 79:89, 81:91, 84:98, 87:101,
    90:104, 93:107, 96:111, 99:114, 102:117, 105:120,
    108:123, 111:126, 114:129, 117:131, 125:(132,138),
})
_GAC_CL_22_29 = _inv({
    62:75, 63:76, 64:77, 65:78, 66:79, 67:80, 68:81,
    69:82, 70:83, 71:84, 72:85, 73:86, 74:87, 75:88,
    76:89, 77:90, 78:91, 79:92, 80:93, 81:95, 83:97,
    85:99, 87:101, 89:103, 90:105, 91:106, 93:108,
    95:110, 97:112, 99:114, 101:116, 103:118,
    105:120, 108:123, 111:126, 114:129, 117:132,
    125:(133,138),
})

_DAC_30_39 = _inv({
    64:20, 66:21, 68:22, 69:23, 73:24, 74:25, 77:26,
    79:27, 80:28, 82:29, 85:30, 86:31, 89:32, 90:33,
    93:34, 96:35, 99:36, 102:37, 105:38, 108:39,
    120:(40,57),
})
_DAS_30_39 = _inv({
    64:13, 72:14, 77:15, 79:16, 83:18, 86:19, 90:20,
    93:21, 97:22, 100:23, 104:24, 108:25, 112:26,
    117:27, 120:(28,38),
})
_DAP_SL_30_39 = _inv({
    73:27, 74:28, 75:29, 76:30, 77:31, 78:32, 79:33,
    80:34, 81:35, 83:37, 85:38, 87:39, 89:40, 91:41,
    93:42, 95:43, 99:45, 101:46, 103:47, 105:48,
    108:49, 110:50, 113:51, 120:(52,57),
})
_DAP_CL_30_39 = _inv({
    67:28, 69:29, 71:30, 72:31, 75:32, 77:33, 79:34,
    80:35, 83:36, 85:37, 87:38, 89:39, 91:40, 94:41,
    96:42, 99:43, 101:44, 103:45, 106:46, 109:47,
    112:48, 116:49, 120:(50,62),
})
_GAC_SL_30_39 = _GAC_SL_22_29   # tavola simile; valori esatti non estratti dall'OCR
_GAC_CL_30_39 = _GAC_CL_22_29

_DAC_40_49 = _inv({
    70:19, 72:20, 73:21, 75:22, 76:23, 78:24, 79:25,
    81:26, 82:27, 84:28, 87:29, 88:30, 91:31, 93:32,
    94:33, 96:34, 98:35, 100:36, 103:37, 106:38,
    112:39, 118:(40,57),
})
_DAS_40_49 = _inv({
    71:13, 73:14, 76:15, 78:16, 80:17, 82:18, 84:19,
    87:20, 90:21, 93:22, 95:23, 97:24, 101:25,
    105:26, 109:27, 112:28, 116:29, 118:(30,38),
})
_DAP_SL_40_49 = _inv({
    70:27, 71:28, 72:29, 73:30, 74:31, 75:32, 76:33,
    77:34, 78:35, 79:36, 80:37, 83:38, 85:39, 87:40,
    88:41, 90:42, 93:43, 95:44, 97:45, 101:46,
    105:47, 108:48, 112:49, 116:50, 118:(51,57),
})
_DAP_CL_40_49 = _inv({
    70:34, 72:37, 73:38, 74:39, 75:41, 76:42, 77:43,
    78:44, 79:45, 80:46, 82:47, 84:48, 87:49, 90:50,
    93:51, 95:52, 98:53, 101:54, 104:55, 108:56,
    112:57, 118:(58,63),
})
_GAC_SL_40_49 = _GAC_SL_22_29
_GAC_CL_40_49 = _GAC_CL_22_29

_DAC_50_64 = _inv({
    70:19, 72:20, 75:21, 77:22, 79:23, 81:24, 83:25,
    86:26, 87:27, 89:28, 90:29, 93:30, 95:31, 98:32,
    100:33, 103:34, 105:35, 108:36, 111:37, 113:38,
    118:(39,40), 125:(41,57),
})
_DAS_50_64 = _inv({
    72:14, 74:15, 77:16, 79:17, 81:18, 83:19, 86:20,
    90:21, 94:22, 99:23, 104:24, 108:25, 112:26,
    118:27, 125:(28,38),
})
_DAP_SL_50_64 = _inv({
    71:28, 73:29, 75:31, 77:32, 78:33, 80:34, 83:35,
    85:36, 88:37, 90:38, 94:39, 96:40, 101:41,
    105:42, 108:43, 112:44, 117:45, 125:(46,57),
})
_DAP_CL_50_64 = _inv({
    70:27, 73:36, 75:38, 77:39, 79:40, 81:41, 83:42,
    85:43, 88:44, 90:45, 94:46, 96:47, 99:48, 102:49,
    104:50, 107:51, 109:52, 112:53, 117:54, 125:(55,64),
})
_GAC_SL_50_64 = _GAC_SL_22_29
_GAC_CL_50_64 = _GAC_CL_22_29

_DAC_65_74 = _inv({
    72:20, 74:21, 75:22, 77:23, 79:24, 81:25, 82:26,
    85:27, 87:28, 90:29, 93:30, 96:31, 97:32, 100:33,
    103:34, 106:35, 109:36, 112:37, 115:38, 118:(39,40),
    125:(41,57),
})
_DAS_65_74 = _inv({
    72:14, 74:15, 77:16, 79:17, 81:18, 85:19, 88:20,
    93:21, 96:22, 99:23, 104:24, 108:25, 112:26,
    118:27, 125:(28,38),
})
_DAP_SL_65_74 = _inv({
    70:28, 71:29, 73:30, 74:31, 75:32, 76:33, 78:34,
    79:35, 80:36, 83:37, 85:38, 88:39, 91:40, 95:41,
    97:42, 101:43, 105:44, 108:45, 112:46, 117:47,
    125:(48,57),
})
_DAP_CL_65_74 = _inv({
    69:27, 72:37, 74:39, 76:40, 78:41, 79:42, 83:43,
    86:44, 88:45, 91:46, 95:47, 99:48, 102:49,
    105:50, 108:51, 112:52, 117:53, 125:(54,64),
})
_GAC_SL_65_74 = _GAC_SL_22_29
_GAC_CL_65_74 = _GAC_CL_22_29

TAVOLA_A13 = {
    "16-21": {
        "gac_sl": _GAC_SL_16_21,
        "gac_cl": _GAC_CL_16_21,
        "dac":    _DAC_16_21,
        "das":    _DAS_16_21,
        "dap_sl": _DAP_SL_16_21,
        "dap_cl": _DAP_CL_16_21,
    },
    "22-29": {
        "gac_sl": _GAC_SL_22_29, "gac_cl": _GAC_CL_22_29,
        "dac":    _DAC_22_29,    "das":    _DAS_22_29,
        "dap_sl": _DAP_SL_22_29, "dap_cl": _DAP_CL_22_29,
    },
    "30-39": {
        "gac_sl": _GAC_SL_30_39, "gac_cl": _GAC_CL_30_39,
        "dac":    _DAC_30_39,    "das":    _DAS_30_39,
        "dap_sl": _DAP_SL_30_39, "dap_cl": _DAP_CL_30_39,
    },
    "40-49": {
        "gac_sl": _GAC_SL_40_49, "gac_cl": _GAC_CL_40_49,
        "dac":    _DAC_40_49,    "das":    _DAS_40_49,
        "dap_sl": _DAP_SL_40_49, "dap_cl": _DAP_CL_40_49,
    },
    "50-64": {
        "gac_sl": _GAC_SL_50_64, "gac_cl": _GAC_CL_50_64,
        "dac":    _DAC_50_64,    "das":    _DAS_50_64,
        "dap_sl": _DAP_SL_50_64, "dap_cl": _DAP_CL_50_64,
    },
    "65-74": {
        "gac_sl": _GAC_SL_65_74, "gac_cl": _GAC_CL_65_74,
        "dac":    _DAC_65_74,    "das":    _DAS_65_74,
        "dap_sl": _DAP_SL_65_74, "dap_cl": _DAP_CL_65_74,
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
    if 50 <= eta <= 64: return "50-64"
    if 65 <= eta <= 74: return "65-74"
    if 75 <= eta <= 89: return "75-89"
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

    if fascia != "16-21":
        risultato['Nota'] = ("I punteggi compositi per fasce 22-74 sono derivati da tavole "
                             "estratte via OCR dal manuale: verificare i valori critici sul "
                             "manuale cartaceo prima dell'uso clinico.")

    return risultato


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

# ── TAVOLA A.2 — Insegnante 17-21 compositi (somma Pp → composito) ───
TAVOLA_A2 = {
    "gac":    _inv({41:9, 42:10, 43:11, 44:12, 45:13, 46:14, 47:15, 48:16, 49:17,
                    50:18, 51:19, 52:20, 53:21, 54:22, 55:23, 56:24, 57:25, 58:26,
                    59:27, 60:28, 61:29, 62:30, 63:31, 64:32, 65:33, 66:34, 67:35,
                    68:36, 69:37, 70:38, 71:39, 72:40, 73:41, 74:42, 75:43, 76:44,
                    77:45, 78:47, 79:50, 81:56, 82:59, 83:62, 84:63, 85:64, 86:66,
                    87:68, 88:70, 89:72, 90:74, 91:75, 92:77, 93:78, 94:79, 95:80,
                    96:81, 97:82, 98:85, 99:86, 100:87, 101:88, 102:89, 103:91,
                    104:92, 105:93, 106:94, 107:95, 108:96, 109:97, 110:98, 111:99,
                    112:101, 113:102, 114:103, 115:104, 116:105, 117:107, 118:108,
                    119:109, 120:113}),
    "dac":    _inv({48:3, 51:4, 53:5, 55:6, 57:7, 59:8, 61:9, 63:10, 65:11, 67:12,
                    69:13, 70:14, 72:15, 75:16, 77:17, 81:18, 83:19, 86:20, 87:21,
                    89:22, 91:23, 93:24, 96:29, 99:30, 102:31, 107:32, 112:33,
                    117:34, 120:35}),
    "das":    _inv({54:2, 57:3, 60:4, 62:5, 64:6, 66:7, 68:8, 70:9, 72:10, 75:11,
                    77:12, 85:14, 87:15, 93:16, 95:17, 104:18, 110:19, 115:20,
                    120:21}),
    "dap":    _inv({45:5, 47:6, 49:7, 51:8, 53:9, 55:10, 57:11, 59:12, 61:13, 63:14,
                    65:15, 67:16, 69:17, 70:18, 72:19, 75:20, 77:21, 78:22, 81:26,
                    83:28, 86:30, 87:31, 88:32, 90:33, 92:34, 99:36, 107:37}),
}

# ── TAVOLA A.5c — Genitore 17-21 compositi (somma Pp → composito) ────
TAVOLA_A5C = {
    "gac":    _inv({43:61, 44:64, 45:66, 46:68, 47:71, 48:73, 49:75, 50:78, 51:80,
                    52:82, 53:85, 55:88, 57:89, 59:91, 60:93, 61:94, 62:95, 63:97,
                    64:98, 65:99, 66:100, 67:101, 68:103, 69:104, 70:105, 71:106,
                    72:107, 73:108, 74:110, 75:111, 76:112, 77:113, 78:115, 80:116}),
    "dac":    _inv({49:24, 50:25, 51:26, 52:27, 55:29, 57:30, 59:31, 60:32, 63:33,
                    66:34, 70:35, 74:36, 80:37}),
    "das":    _inv({52:17, 54:18, 55:19, 57:20, 60:21, 68:23, 73:24, 77:25, 80:26}),
    "dap":    _inv({57:42, 60:43, 63:45, 65:46, 67:47, 70:48, 73:49, 75:50, 80:51}),
}

# ── Etichette subscale per output ────────────────────────────────────
_NOMI_SUB = {
    "co": "Comunicazione", "am": "Uso dell'ambiente",
    "sco": "Competenze scolastiche", "vc": "Vita a casa",
    "vs": "Vita a scuola", "ss": "Salute e sicurezza",
    "tl": "Tempo libero", "cur": "Cura di sé",
    "ac": "Autocontrollo", "soc": "Socializzazione", "lav": "Lavoro",
}


def _calcola_abas_forma(grezzi, tabella_grezzi, tavola_comp, fascia_label,
                         dominio_pratico_sl, dominio_pratico_cl,
                         ha_lavoro, forma_nome):
    """Nucleo comune di calcolo per tutte e tre le nuove forme ABAS."""
    pp = {}
    righe = {}
    for sub, grezzo in grezzi.items():
        pp_val = tabella_grezzi.get(sub, {}).get(int(grezzo))
        pp[sub] = pp_val
        pp_str = str(pp_val) if pp_val is not None else "N/D"
        righe[f'{_NOMI_SUB.get(sub, sub)} (grezzo/Pp)'] = f"{grezzo}/{pp_str}"

    def sp(aree):
        vals = [pp.get(a) for a in aree]
        return sum(vals) if all(v is not None for v in vals) else None

    dac_aree = ["co", "sco", "ac"]
    das_aree = ["tl", "soc"]
    dap_sl_aree = dominio_pratico_sl
    dap_cl_aree = dominio_pratico_cl

    dac_sum = sp(dac_aree)
    das_sum = sp(das_aree)
    dap_sum = sp(dap_cl_aree if ha_lavoro else dap_sl_aree)
    col_dap = "dap_cl" if ha_lavoro else "dap_sl"
    col_gac = "gac_cl" if ha_lavoro else "gac"

    # Usa tavola specifica se ha "gac_sl"/"gac_cl", altrimenti usa "gac"
    col_gac_key = "gac_sl" if "gac_sl" in tavola_comp else ("gac_cl" if ha_lavoro and "gac_cl" in tavola_comp else "gac")
    col_dap_key = "dap_cl" if ha_lavoro and "dap_cl" in tavola_comp else ("dap_sl" if "dap_sl" in tavola_comp else "dap")

    comp_dac = _lookup(tavola_comp["dac"], dac_sum) if dac_sum is not None else None
    comp_das = _lookup(tavola_comp["das"], das_sum) if das_sum is not None else None
    comp_dap = _lookup(tavola_comp.get(col_dap_key, tavola_comp.get("dap", [])), dap_sum) if dap_sum is not None else None
    gac_sum = (dac_sum or 0) + (das_sum or 0) + (dap_sum or 0)
    comp_gac = _lookup(tavola_comp.get(col_gac_key, tavola_comp.get("gac", [])), gac_sum) if (dac_sum and das_sum and dap_sum) else None

    def fmt(comp):
        if comp is None: return "N/D"
        perc = PERCENTILI_A13.get(comp, "–")
        return f"{comp} ({perc}° percentile)"

    res = {"Forma": forma_nome, "Fascia normativa": fascia_label, "Ha un lavoro": "Sì" if ha_lavoro else "No"}
    res.update(righe)
    res["GAC (composito)"] = fmt(comp_gac)
    res["DAC – Dominio Concettuale"] = fmt(comp_dac)
    res["DAS – Dominio Sociale"] = fmt(comp_das)
    res["DAP – Dominio Pratico"] = fmt(comp_dap)
    return res


def calcola_abas_autovalutazione(dati):
    eta = dati.get("eta", 0)
    ha_lavoro = dati.get("ha_lavoro", False)
    grezzi = dati.get("grezzi", {})
    fascia = fascia_eta(eta)
    if not fascia:
        return {"Forma": "Autovalutazione adulto", "Nota": f"Età {eta} fuori range (16-89)"}
    # La fascia 75-89 non ha sottoscala Lavoro
    if fascia == "75-89":
        ha_lavoro = False
    subs_base = ["co", "am", "sco", "vc", "ss", "tl", "cur", "ac", "soc"]
    if ha_lavoro:
        subs_base.append("lav")
    grezzi_f = {k: grezzi.get(k, 0) for k in subs_base}
    tavola_comp = TAVOLA_A10[fascia]
    res = _calcola_abas_forma(
        grezzi_f, TAVOLA_A9[fascia], tavola_comp, fascia, ha_lavoro=ha_lavoro,
        dominio_pratico_sl=["am","vc","ss","cur"],
        dominio_pratico_cl=["am","vc","ss","cur","lav"],
        forma_nome="Autovalutazione adulto (16-89)"
    )
    return res


def calcola_abas_insegnante(dati):
    eta = dati.get("eta", 0)
    ha_lavoro = dati.get("ha_lavoro", False)
    grezzi = dati.get("grezzi", {})
    if not (17 <= eta <= 21):
        return {"Forma": "Insegnante", "Nota": f"Età {eta} non supportata (17-21 anni)"}
    subs_base = ["co", "am", "sco", "vs", "ss", "tl", "cur", "ac", "soc"]
    if ha_lavoro:
        subs_base.append("lav")
    grezzi_f = {k: grezzi.get(k, 0) for k in subs_base}
    return _calcola_abas_forma(
        grezzi_f, TAVOLA_A1, TAVOLA_A2, "17-21", ha_lavoro=ha_lavoro,
        dominio_pratico_sl=["am","vs","ss","cur"],
        dominio_pratico_cl=["am","vs","ss","cur","lav"],
        forma_nome="Insegnante (17-21)"
    )


def calcola_abas_genitore(dati):
    eta = dati.get("eta", 0)
    ha_lavoro = dati.get("ha_lavoro", False)
    grezzi = dati.get("grezzi", {})
    if not (17 <= eta <= 21):
        return {"Forma": "Genitore", "Nota": f"Età {eta} non supportata (17-21 anni)"}
    subs_base = ["co", "am", "sco", "vc", "ss", "tl", "cur", "ac", "soc"]
    if ha_lavoro:
        subs_base.append("lav")
    grezzi_f = {k: grezzi.get(k, 0) for k in subs_base}
    return _calcola_abas_forma(
        grezzi_f, TAVOLA_A5_G, TAVOLA_A5C, "17-21", ha_lavoro=ha_lavoro,
        dominio_pratico_sl=["am","vc","ss","cur"],
        dominio_pratico_cl=["am","vc","ss","cur","lav"],
        forma_nome="Genitore (17-21)"
    )


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
