import streamlit as st
import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from calcolatore_test import calcola_tutti_i_risultati, formatta_risultati_email, AREE_ABAS, OPZIONI_ABAS, fascia_eta

st.set_page_config(
    page_title="Valutazione ADHD - Test Autosomministrati",
    page_icon="🧠",
    layout="wide"
)

st.title("Valutazione ADHD - Test Autosomministrati")
st.caption('Creata dal Dott. Marco Manzo')
st.caption('_Department of Psychiatry, University of Campania "Luigi Vanvitelli", Naples, Italy_')

st.write("""
Benvenuto/a. Questa applicazione ti guiderà attraverso una serie di questionari.
Per favore, compila i campi seguenti e rispondi alle domande dei test che ti sono stati indicati.
Non è necessario compilarli tutti.
""")

with st.expander("1. Dati del Paziente", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        codice_paziente = st.text_input("Codice Paziente (fornito dallo specialista)")
        genere = st.selectbox("Genere", ["Maschio", "Femmina", "Non binario", "Altro", "Preferisco non specificare"])
    with col2:
        data_nascita = st.date_input("Data di nascita",
                                     min_value=datetime.date(1920, 1, 1),
                                     max_value=datetime.date.today(),
                                     format="DD/MM/YYYY")
        livello_istruzione = st.selectbox("Livello di istruzione", [
            "Nessuno / Licenza elementare", "Licenza media", "Diploma di scuola superiore",
            "Laurea triennale", "Laurea magistrale/specialistica", "Dottorato o superiore", "Altro"
        ])

st.divider()

if 'risposte' not in st.session_state:
    st.session_state.risposte = {
        'asrs': [0] * 18, 'wurs': [0] * 61, 'wurs_extra_testo': "", 'temps_a': [1] * 110,
        'bis11': [1] * 30, 'tas20': [3] * 20, 'mdq': {'gate': False, 'parte1': [False] * 13, 'parte2': False, 'parte3': 1},
        'hcl34': [False] * 34, 'ders': [3] * 36, 'des2': [0] * 28, 'mews': [0] * 12,
        'stai_y2': [1] * 20, 'stai_y1': [1] * 20,
        'abas': {
            'eta': 0,
            'ha_lavoro': False,
            'risposte': {area: [0] * len(info['items']) for area, info in AREE_ABAS.items()},
            'suppongo': {area: [False] * len(info['items']) for area, info in AREE_ABAS.items()},
        }
    }
if 'test_compilati' not in st.session_state:
    st.session_state.test_compilati = set()

def on_change_test(test_name):
    st.session_state.test_compilati.add(test_name)

st.header("2. Questionari")
st.info("Apri e compila solo i questionari che ti sono stati indicati dallo specialista.")


# ── ASRS ──────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_asrs():
    with st.expander("Questionario ASRS-v1.1"):
        st.info("Le seguenti domande si riferiscono a come ti sei sentito/a e comportato/a negli **ultimi 6 mesi**.")
        domande = [
            "1. Con che frequenza ha difficoltà a concludere i dettagli finali di un progetto, una volta che le parti più stimolanti sono state fatte?",
            "2. Con che frequenza ha difficoltà a mettere le cose in ordine quando deve svolgere un compito che richiede organizzazione?",
            "3. Con che frequenza ha problemi a ricordarsi gli appuntamenti o gli impegni?",
            "4. Quando ha un compito che richiede un sacco di concentrazione, con che frequenza evita o ritarda l'inizio?",
            "5. Con che frequenza agita o si contorce le mani o i piedi quando deve stare seduto/a per molto tempo?",
            "6. Con che frequenza si sente eccessivamente attivo/a e costretto a fare delle cose, come se fosse azionato/a da un motore?",
            "7. Con che frequenza fa errori di distrazione quando deve lavorare ad un progetto noioso o difficile?",
            "8. Con che frequenza ha difficoltà a mantenere la sua attenzione quando sta svolgendo un compito noioso o ripetitivo?",
            "9. Con che frequenza ha difficoltà a concentrarsi su quello che le persone le dicono, anche quando stanno parlando a lei direttamente?",
            "10. Con che frequenza perde o ha difficoltà a le cose a casa o al lavoro?",
            "11. Con che frequenza è distratto dalle attività o dal rumore attorno a lei?",
            "12. Con che frequenza abbandona il suo posto nelle riunioni o in altre situazioni in ci si aspetta che lei resti seduto/a?",
            "13. Con che frequenza si sente agitato/a o irrequieto/a?",
            "14. Con che frequenza ha difficoltà a staccare e a rilassarsi quando ha tempo per sé?",
            "15. Con che frequenza si trova a parlare troppo quando è nelle situazioni sociali?",
            "16. Durante conversazione, con che frequenza si trova a terminare le frasi delle persone con cui sta parlando, prima che possano finirle da sole?",
            "17. Con che frequenza ha difficoltà ad attendere il suo turno nelle situazioni in cui si richiede di aspettare il proprio turno?",
            "18. Con che frequenza interrompe gli altri quando sono indaffarati?"
        ]
        opzioni = ["Mai", "Raramente", "Talvolta", "Spesso", "Molto spesso"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['asrs'][i] = st.radio(
                domanda, options=range(len(opzioni)), format_func=lambda x: opzioni[x],
                key=f"asrs_{i}", horizontal=True, on_change=on_change_test, args=('asrs',)
            )

sezione_asrs()


# ── WURS ──────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_wurs(genere):
    with st.expander("Questionario WURS"):
        st.info("Le seguenti affermazioni si riferiscono a quando era un/a bambino/a di età **fra gli 8 e i 10 anni**.")
        domande = [
            "1. Attivo, irrequieto, sempre in movimento", "2. Pauroso di fronte alle cose",
            "3. Problemi di concentrazione, facilmente distraibile", "4. Ansioso, preoccupato",
            "5. Nervoso, irrequieto", "6. Distratto, trasognato",
            "7. Facilmente arrabbiato, irascibile", "8. Timido, sensibile",
            "9. Crolli emotivi, esplosioni di rabbia", "10. Scarsa perseveranza, interrompere le attività prima di finirle",
            "11. Testardo, ostinato", "12. Spesso triste, depresso, infelice",
            "13. Imprudente, azzardato, coinvolto in marachelle", "14. Niente mi divertiva, insoddisfatto della vita",
            "15. Indisciplinato, disobbediente con i genitori, ribelle", "16. Scarsa autostima, bassa considerazione di sé",
            "17. Facilmente irritabile", "18. Estroverso, gentile, socievole",
            "19. Disordinato, caotico", "20. Forti sbalzi d'umore, lunatico",
            "21. Irritabile, arrabbiato", "22. Amici, popolare",
            "23. Ben organizzato, pulito, ordinato", "24. Impulsivo, agire senza riflettere",
            "25. Tendenza a essere immaturo", "26. Sensi di colpa e pentimento",
            "27. Perdita dell'autocontrollo", "28. Tendenza a essere o ad agire irrazionalmente",
            "29. Impopolare con gli altri bambini, non mantenere a lungo le amicizie", "30. Scarso coordinamento motorio, non partecipare a sport",
            "31. Paura di perdere l'autocontrollo", "32. Buona coordinazione motoria, scelto per primo nei giochi di squadra",
            "33. [Solo per donne:] maschiaccio", "34. Scappato di casa",
            "35. Coinvolto in risse", "36. Prendere in giro gli altri bambini",
            "37. Leader, autoritario", "38. Difficoltà a svegliarsi la mattina",
            "39. Seguire gli altri, lasciarsi trascinare dagli altri", "40. Problemi ad assumere il punto di vista di qualcun altro",
            "41. Problemi a scuola o con le autorità, convocazioni dal direttore", "42. Problemi con la polizia, arrestato",
            "43. Mal di testa", "44. Mal di stomaco, mal di pancia",
            "45. Stipsi", "46. Diarrea",
            "47. Allergie alimentari", "48. Altre allergie",
            "49. Bagnare il letto", "50. Complessivamente un buon alunno, imparavo in fretta",
            "51. Complessivamente un cattivo alunno, imparavo lentamente", "52. Lento a imparare a leggere",
            "53. Lento a leggere", "54. Difficoltà per il fatto di scambiare le lettere",
            "55. Problemi a sillabare", "56. Problemi con calcoli e numeri",
            "57. Una brutta scrittura", "58. Nonostante leggevo bene non mi è mai piaciuto",
            "59. Non ho sfruttato a pieno le mie potenzialità", "60. Ho dovuto ripetere delle classi",
            "61. Sospeso o espulso"
        ]
        opzioni = ["Per niente o solo marginalmente", "Lievemente", "Moderatamente", "Decisamente", "Molto intensamente"]
        for i, domanda in enumerate(domande):
            if i == 32 and genere == "Maschio":
                st.session_state.risposte['wurs'][i] = 0
                continue
            st.session_state.risposte['wurs'][i] = st.select_slider(
                domanda, options=range(len(opzioni)), format_func=lambda x: opzioni[x],
                key=f"wurs_{i}", on_change=on_change_test, args=('wurs',)
            )
            if i == 60:
                st.session_state.risposte['wurs_extra_testo'] = st.text_input("Specificare (se applicabile)", key="wurs_extra")

sezione_wurs(genere)


# ── TEMPS-A ───────────────────────────────────────────────────────────────────
@st.fragment
def sezione_temps_a(genere):
    with st.expander("Questionario TEMPS-A"):
        st.info("Le seguenti affermazioni descrivono tratti personali. Indica se per te sono Vere o False.")
        domande = [
            "1. Sono una persona scontenta e triste", "2. La gente mi dice che non sono in grado di apprezzare il lato positivo delle cose",
            "3. Ho sofferto molto nella mia vita", "4. Penso che spesso le cose si rivelano negative", "5. Mi arrendo facilmente",
            "6. Per quanto mi posso ricordare, sono sempre stato un fallimento", "7. Mi sono sempre incolpato di cose che gli altri considerano di poco conto",
            "8. Non penso di avere tanta energia come gli altri", "9. Sono il tipo di persona che non ama i cambiamenti",
            "10. In un gruppo, preferisco ascoltare gli altri che parlare", "11. Spesso cedo nei confronti degli altri",
            "12. Mi sento a disagio nell'incontrare gli altri", "13. I miei sentimenti sono spesso feriti da critiche e rifiuti",
            "14. Son il tipo di persona sulla quale si può fare affidamento", "15. I bisogni degli altri vengono prima dei miei",
            "16. Sono una persona dedita al lavoro", "17. Preferirei lavorare per qualcun altro invece che per il mio capo",
            "18. Per me è naturale essere ordinato ed organizzato", "19. Sono il tipo di persona che dubita di ogni cosa",
            "20. Il mio istinto sessuale è stato sempre scarso", "21. Normalmente ho bisogno di più di nove ore di sonno",
            "22. Spesso mi sento stanco per nessun motivo", "23. Ho improvvisi cambiamenti di umore",
            "24. Il mio umore ed energia o sono alti o bassi, raramente un cosa intermedia", "25. La mia abilità di pensare passa dalla nitidezza all'intorpidimento per nessuna ragione",
            "26. Può piacermi qualcuno molto e poi perdere completamente l'interesse", "27. Spesso ho scatti d'ira verso gli altri e poi mi sento in colpa",
            "28. Spesso inizio delle attività e poi perdo l'interesse prima di finirle", "29. Il mio umore spesso cambia per nessun motivo",
            "30. Costantemente passo dall'essere gioioso all'essere stanco", "31. Spesso vado a letto triste, ma mi alzo al mattino sentendomi eccezionale",
            "32. Spesso vado a letto sentendomi bene, ma mi alzo e sento che non vale la pena di vivere", "33. Spesso mi dicono che divento pessimista e mi dimentico dei momenti precedenti felici",
            "34. Passo da sentimenti di grande autostima a sentimenti di insicurezza", "35. Passo da momenti di estroversione a momenti di introversione",
            "36. Sento tutte le emozioni intensamente", "37. Il mio bisogno di sonno varia molto, da sole poche ore a più di nove ore",
            "38. Il modo di cui vedo le cose è a volte vivido, ma altre volte è privo di vita", "39. Sono il tipo di persona che può essere triste e felice allo stesso tempo",
            "40. Sogno molto a occhi aperti su cose che gli altri considerano impossibili da raggiungere", "41. Spesso sento un bisogno irrefrenabile di fare cose oltraggiose",
            "42. Sono il tipo di persona che si innamora e si 'disinnamora' facilmente", "43. Sono di solito su di giri e di umore gioioso",
            "44. La vita è una festa che io mi godo nella sua interezza", "45. Mi piace raccontare barzellette e la gente mi dice che sono divertente",
            "46. Sono il tipo di persona che pensa che ogni cosa si risolverà per il meglio", "47. Ho una grande fiducia in me stesso",
            "48. Ho spesso molte idee geniali", "49. Sono sempre sul punto di partire", "50. Riesco ad eseguire molti compiti senza stancarmi",
            "51. Ho la dote del parlare, convincere e ispirare gli altri", "52. Mi piace affrontare nuovi progetti anche se pericolosi",
            "53. Una volta che ho deciso di raggiungere qualcosa, niente mi può fermare", "54. Sono completamente a mio agio anche con persone che conosco appena",
            "55. Mi piace stare con molte persone", "56. La gente mi dice che mi intrometto negli affari altrui",
            "57. Sono conosciuto per la mia generosità, e spendo molti soldi per gli altri", "58. Ho competenza ed esperienza nel mio campo",
            "59. Ritengo di avere il diritto e il privilegio di fare quello che voglio", "60. Sono il tipo di persona a cui piace comandare",
            "61. Quando non sono d'accordo con qualcuno, mi infervoro nella discussione", "62. Il mio desiderio sessuale è sempre alto",
            "63. Normalmente riesco ad andare avanti con meno di 6 ore di sonno", "64. Sono una persona irritabile",
            "65. Sono per natura una persona insoddisfatta", "66. Mi lamento molto", "67. Sono molto critico verso gli altri",
            "68. Spesso mi sento in allarme", "69. Spesso mi sento avvolto in me stesso", "70. Sono governato da un irrequietezza spiacevole che non comprendo",
            "71. Spesso sono così furibondo che getterei via tutto", "72. Quando sono provocato, potrei finire in una rissa",
            "73. La gente mi dice che perdo la pazienza per niente", "74. Quando sono arrabbiato, scatto nervosamente con la gente",
            "75. Mi piace provocare la gente, anche so la conosco appena", "76. Il mio sarcasmo mi ha messo nei guai",
            "77. Posso essere così furioso che potrei far del male a qualcuno", "78. Sono così geloso del mio partner, che ne sono tormentato",
            "79. Sono conosciuto come colui che dice molte parolacce", "80. Mi è stato detto che divento violento anche solo dopo pochi drinks alcolici",
            "81. Sono una persona molto scettica", "82. Potrei essere un rivoluzionario", "83. Il mio istinto sessuale è spesso così intenso da diventare spiacevole",
            "84. (sole donne) Ho attacchi di rabbia incontrollabile prime del periodo mestruale", "85. Sono stato una persona che ha sempre dato preoccupazioni",
            "86. Mi preoccupo sempre per qualcosa", "87. Mi preoccupo di questioni quotidiane che gli altri considerano di poca importanza",
            "88. Non posso fare a meno di preoccuparmi", "89. Molte persone mi hanno detto di non preoccuparmi cosi tanto",
            "90. Quando sono stressato, la mia mente è spesso vuota", "91. Non riesco a rilassarmi", "92. Spesso mi sento agitato internamente",
            "93. Quando sono stressato, le mie mani tremano", "94. Spesso ho lo stomaco sottosopra", "95. Quando sono nervoso, mi capita di avere la diarrea",
            "96. Quando sono nervoso, mi capita di avere la nausea", "97. Quando sono nervoso, devo andare in bagno più spesso",
            "98. Quando qualcuno ritarda a rientrare in casa, temo che possa aver avuto un incidente", "99. Speso temo che qualcuno nella mia famiglia abbia un grave malattia",
            "100. Temo sempre che qualcuno possa comunicarmi cattive notizie su qualcuno della mia famiglia", "101. Il mio sonno non è riposante",
            "102. Ho spesso difficoltà ad addormentarmi", "103. Sono per natura una persona molto cauta",
            "104. Spesso mi sveglio nella notte impaurito dal fatto che possano esserci dei ladri in casa", "105. Ho facilmente mal di testa quando sono stressato",
            "106. Quando sono stressato, ho una sensazione spiacevole nel mio torace", "107. Sono una persona insicura",
            "108. Anche piccoli cambiamenti nella routine mi stressano molto", "109. Quando guido anche se non ho fatto nulla di sbagliato, temo che la polizia mi possa fermare",
            "110. Rumori improvvisi mi fanno sobbalzare facilmente"
        ]
        opzioni = {1: "Falso", 2: "Vero"}
        for i, domanda in enumerate(domande):
            if i == 83 and genere == "Maschio":
                st.session_state.risposte['temps_a'][i] = 1
                continue
            st.session_state.risposte['temps_a'][i] = st.radio(
                domanda, options=[1, 2], format_func=lambda x: opzioni[x],
                key=f"temps_a_{i}", horizontal=True, on_change=on_change_test, args=('temps_a',)
            )

sezione_temps_a(genere)


# ── BIS-11 ────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_bis11():
    with st.expander("Questionario BIS-11"):
        st.info("Leggi attentamente ciascuna affermazione ed indica la risposta che più si adatta a te. Rispondi rapidamente e sinceramente.")
        domande = [
            "1. Io programmo accuratamente le attività", "2. Faccio le cose senza pensare", "3. Decido con molta rapidità",
            "4. Prendo il mondo come viene", "5. Non presto attenzione", "6. I miei pensieri "corrono"",
            "7. Programmo i miei viaggi con molto anticipo", "8. Sono padrone di me", "9. Mi concentro facilmente",
            "10. Io risparmio con regolarità", "11. Sto sulle spine al teatro o alle conferenze", "12. Sono uno che pensa accuratamente",
            "13. Faccio piani per un investimento per il futuro", "14. Dico le cose senza pensare", "15. Mi piace pensare a problemi complessi",
            "16. Cambio spesso lavoro", "17. Io agisco d'impulso", "18. Mi annoio facilmente quando affronto ragionamenti complessi",
            "19. Agisco sotto l'impulso del momento", "20. Sono uno che pensa con serietà", "21. Cambio spesso abitazione",
            "22. Compro le cose impulsivamente", "23. Posso pensare solo ad un problema alla volta", "24. Cambio spesso i miei hobby",
            "25. Spendo o addebito sul mio conto più di quello che guadagno", "26. Quando penso ho pensieri estranei, parassitari",
            "27. So più interessato al presente che al futuro", "28. Sono irrequieto alle conferenze o ai discorsi",
            "29. Mi piacciono i puzzle", "30. Faccio progetti per il futuro"
        ]
        opzioni = ["Raramente/Mai", "Occasionalmente", "Spesso", "Quasi sempre/Sempre"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['bis11'][i] = st.radio(
                domanda, options=range(1, 5), format_func=lambda x: opzioni[x-1],
                key=f"bis11_{i}", horizontal=True, on_change=on_change_test, args=('bis11',)
            )

sezione_bis11()


# ── TAS-20 ────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_tas20():
    with st.expander("Questionario TAS-20"):
        st.info("Indica quanto sei d'accordo o in disaccordo con ciascuna delle seguenti affermazioni.")
        domande = [
            "1. Sono spesso confuso/a circa le emozioni che provo", "2. Mi è difficile trovare le parole giuste per esprimere i miei sentimenti",
            "3. Provo delle sensazioni fisiche che neanche i medici capiscono", "4. Riesco facilmente a descrivere i miei sentimenti",
            "5. Preferisco approfondire i miei problemi piuttosto che descriverli semplicemente", "6. Quando sono sconvolto/a non so se sono triste, spaventato/a o arrabbiato/a",
            "7. Sono spesso disorientato dalle sensazioni che provo nel mio corpo", "8. Preferisco lasciare che le cose seguano il loro corso piuttosto che capire perché sono andate in quel modo",
            "9. Provo sentimenti che non riesco proprio ad identificare", "10. È essenziale conoscere le proprie emozioni",
            "11. Mi è difficile descrivere ciò che provo per gli altri", "12. Gli altri mi chiedono di parlare di più dei miei sentimenti",
            "13. Non capisco cosa stia accadendo dentro di me", "14. Spesso non so perché mi arrabbio",
            "15. Con le persone preferisco parlare di cose di tutti i giorni piuttosto che delle loro emozioni", "16. Preferisco vedere spettacoli leggeri, piuttosto che spettacoli a sfondo psicologico",
            "17. Mi è difficile rivelare i sentimenti più profondi anche ad amici più intimi", "18. Riesco a sentirmi vicino ad una persona, anche se ci capita di stare in silenzio",
            "19. Trovo che l'esame dei miei sentimenti mi serve a risolvere i miei problemi personali", "20. Cercare significati nascosti in films o commedie distoglie dal piacere dello spettacolo"
        ]
        opzioni = ["NON SONO PER NIENTE D'ACCORDO", "NON SONO MOLTO D'ACCORDO", "NON SONO NÉ D'ACCORDO NÉ IN DISACCORDO", "SONO D'ACCORDO IN PARTE", "SONO COMPLETAMENTE D'ACCORDO"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['tas20'][i] = st.select_slider(
                domanda, options=range(1, 6), format_func=lambda x: f"{x} - {opzioni[x-1]}",
                key=f"tas20_{i}", on_change=on_change_test, args=('tas20',)
            )

sezione_tas20()


# ── MDQ ───────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_mdq():
    with st.expander("Questionario MDQ (Mood Disorder Questionnaire)"):
        risposta_gate = st.radio(
            "**C'è mai stato un periodo di tempo durante il quale non ti sentivi come al tuo solito e...**",
            options=["No", "Sì"], key="mdq_gate", horizontal=True,
            help="Se rispondi 'Sì', appariranno le domande successive."
        )
        st.session_state.risposte['mdq']['gate'] = (risposta_gate == "Sì")

        if st.session_state.risposte['mdq']['gate']:
            on_change_test('mdq')
            st.subheader("Parte 1: Sintomi")
            domande_p1 = [
                "...ti sentivi così bene o così 'su' che gli altri hanno pensato che tu non fossi come al solito o che fossi talmente 'su' da poterti trovare in qualche guaio?",
                "...eri talmente irritabile da urlare contro altre persone o provocare un litigio o uno scontro fisico?",
                "...ti sentivi molto più sicuro di te del solito?",
                "...dormivi molto meno del normale e ti sembrava di non sentire la necessità di dormire?",
                "...eri più loquace e parlavi più velocemente del solito?",
                "...i pensieri ti attraversavano velocemente la testa o non riuscivi a rilassarti?",
                "...eri così facilmente distraibile dalle cose intorno a te da avere difficoltà nel concentrarti e nel mantenere l'attenzione?",
                "...avevi molta più energia del solito?",
                "...eri molto più attivo e facevi molte più cose del solito?",
                "...eri molto più socievole ed espansivo del solito, per esempio telefonavi agli amici nel mezzo della notte?",
                "...eri molto più interessato al sesso del solito?",
                "...facevi delle cose per te inusuali o che gli altri avrebbero potuto considerare eccessive, stupide o rischiose?",
                "...spendevi così tanti soldi da creare delle difficoltà a te o alla tua famiglia?"
            ]
            for i, domanda in enumerate(domande_p1):
                risposta = st.radio(domanda, options=["No", "Sì"], key=f"mdq_p1_{i}", horizontal=True)
                st.session_state.risposte['mdq']['parte1'][i] = (risposta == "Sì")

            st.subheader("Parte 2: Simultaneità")
            risposta_p2 = st.radio(
                "Se hai risposto 'Sì' ad una o più delle domande poste sopra, molte di queste situazioni si sono verificate durante lo stesso periodo di tempo?",
                options=["No", "Sì"], key="mdq_p2", horizontal=True
            )
            st.session_state.risposte['mdq']['parte2'] = (risposta_p2 == "Sì")

            st.subheader("Parte 3: Compromissione")
            opzioni_p3 = {1: "Nessun problema", 2: "Problemi di lieve entità", 3: "Problemi di moderata entità", 4: "Problemi gravi"}
            st.session_state.risposte['mdq']['parte3'] = st.radio(
                "In che misura qualcuna di queste situazioni ti ha creato problemi (es. incapacità a lavorare, problemi familiari, economici o legali, litigi o scontri fisici)?",
                options=opzioni_p3.keys(), format_func=lambda x: opzioni_p3[x], key="mdq_p3"
            )

sezione_mdq()


# ── HCL-34 ────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_hcl34():
    with st.expander("Questionario HCL-34 (Hypomania Checklist)"):
        st.info("Pensa a un periodo di tempo in cui non ti sentivi come al tuo solito. In quel periodo, si sono verificate le seguenti cose?")
        domande = [
            "1. Ho meno bisogno di sonno", "2. Ho più energie e sono più attivo", "3. Ho più fiducia in me",
            "4. Mi piace di più il mio lavoro", "5. Sono più socievole (telefono di più, esco di più)", "6. Voglio viaggiare e viaggio di più",
            "7. Tendo a guidare più velocemente o guido in modo più rischioso", "8. Spendo di più/spendo troppi soldi",
            "9. Rischio di più nella vita quotidiana (nel mio lavoro e/o in altre attività)", "10. Sono fisicamente più attivo (sport e altre cose)",
            "11. Penso di fare più cose e/o faccio più progetti", "12. Ho più idee, sono più creativo", "13. Sono meno timido o meno inibito",
            "14. Metto vestiti o trucco più vivaci e più stravaganti", "15. Ho più voglia di incontrare o realmente incontro di più le persone",
            "16. Ho più interessi sessuali e/o il mio desiderio sessuale è aumentato", "17. Faccio più approcci sessuali e/o sono più attivo sessualmente",
            "18. Parlo di più", "19. Il mio pensiero è più veloce", "20. Faccio più battute", "21. Ho più difficoltà a concentrarmi",
            "22. Faccio molte cose nuove", "23. I pensieri saltano da un tema ad un altro", "24. Faccio le cose più velocemente e/o più facilmente",
            "25. Sono più impaziente e/o mi arrabbio più facilmente", "26. Posso essere stancante o irritante per gli altri",
            "27. Litigo più facilmente", "28. Mi sento più su, più ottimista", "29. Bevo più caffè", "30. Fumo più sigarette",
            "31. Bevo più alcolici", "32. Prendo più farmaci (sedativi, antiansia, stimolanti…)",
            "33. Gioco di più d'azzardo (più spesso e/o puntando cifre maggiori)", "34. Mangio di più (più spesso e/o quantità maggiori di cibo)"
        ]
        for i, domanda in enumerate(domande):
            risposta = st.radio(domanda, options=["No", "Sì"], key=f"hcl34_{i}", horizontal=True, on_change=on_change_test, args=('hcl34',))
            st.session_state.risposte['hcl34'][i] = (risposta == "Sì")

sezione_hcl34()


# ── DERS ──────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_ders():
    with st.expander("Questionario DERS (Difficulties in Emotion Regulation Scale)"):
        st.info("Indica quanto spesso si applicano a te le seguenti affermazioni.")
        domande = [
            "1. Sono sereno riguardo a ciò che provo", "2. Presto attenzione a come mi sento",
            "3. Vivo le mie emozioni come travolgenti e fuori dal controllo", "4. Non ho idea di come mi sento",
            "5. Ho difficoltà a dare un senso a ciò che provo", "6. Presto attenzione alle mie emozioni",
            "7. So esattamente come mi sento", "8. Mi interessa come mi sento",
            "9. Sono confuso riguardo a ciò che provo", "10. Quando sono turbato, riconosco le mie emozioni",
            "11. Quando sono turbato, mi arrabbio con me stesso perché mi sento in quel modo", "12. Quando sono turbato, mi imbarazza sentirmi in quel modo",
            "13. Quando sono turbato, ho delle difficoltà a completare il mio lavoro", "14. Quando sono turbato, perdo il controllo",
            "15. Quando sono turbato, credo che rimarrò in quello stato per molto tempo", "16. Quando sono turbato, credo che finirò per sentirmi depresso",
            "17. Quando sono turbato, credo che i miei sentimenti siano validi e importanti", "18. Quando sono turbato, faccio fatica a focalizzarmi su altre cose",
            "19. Quando sono turbato, mi sento senza controllo", "20. Quando sono turbato, posso comunque finire le cose che devo fare",
            "21. Quando sono turbato, mi vergogno con me stesso perché mi sento in quel modo", "22. Quando sono turbato, so che alla fine posso trovare un modo per sentirmi meglio",
            "23. Quando sono turbato, mi sento debole", "24. Quando sono turbato, sento di potere avere ancora il controllo dei miei comportamenti",
            "25. Quando sono turbato, mi sento in colpa perché mi sento in quel modo", "26. Quando sono turbato, ho delle difficoltà a concentrarmi",
            "27. Quando sono turbato, ho delle difficoltà nel controllare i miei comportamenti", "28. Quando sono turbato, credo che non ci sia niente che io possa fare per sentirmi meglio",
            "29. Quando sono turbato, mi irrito con me stesso perché mi sento in quel modo", "30. Quando sono turbato, inizio a sentirmi molto male con me stesso",
            "31. Quando sono turbato, credo che crogiolarmi in questa emozione sia l'unica cosa che io possa fare", "32. Quando sono turbato, perdo il controllo sui miei comportamenti",
            "33. Quando sono turbato, faccio fatica a pensare a qualcosa di diverso", "34. Quando sono turbato, mi prendo del tempo per riflettere su quello che sto provando veramente",
            "35. Quando sono turbato, mi ci vuole molto tempo per sentirmi meglio", "36. Quando sono turbato, le mie emozioni sono travolgenti"
        ]
        opzioni = ["Quasi mai (0-10%)", "A volte (11-35%)", "Circa la metà delle volte (36-65%)", "Molte volte (66-90%)", "Quasi sempre (91-100%)"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['ders'][i] = st.select_slider(
                domanda, options=range(1, 6), format_func=lambda x: f"{x} - {opzioni[x-1]}",
                key=f"ders_{i}", on_change=on_change_test, args=('ders',)
            )

sezione_ders()


# ── DES-II ────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_des2():
    with st.expander("Questionario DES-II (Dissociative Experiences Scale)"):
        st.info("Indica con che percentuale di tempo vivi le seguenti esperienze, SENZA essere sotto l'influenza di alcol o droghe.")
        domande = [
            "1. Guidare una macchina e rendersi conto improvvisamente di non ricordare quello che è successo durante tutto il viaggio o in alcune parti del tragitto.",
            "2. Ascoltare qualcuno parlare e rendersi conto improvvisamente che non si è ascoltato tutto il discorso o parte di ciò che è stato detto.",
            "3. Trovarsi in un posto e non avere alcuna idea di come vi si è arrivati.",
            "4. Ritrovarsi vestiti con abiti che non si ricordano di avere indossato.",
            "5. Trovare fra le proprie cose nuovi oggetti che non si ricordano di avere comperato.",
            "6. Essere avvicinati da persone che non si conoscono che chiamano con un altro nome o sostengono con insistenza di aver già incontrato prima.",
            "7. Sentirsi come se ci si ritrovasse al di fuori del proprio corpo o guardarsi dall'esterno, come se si fosse un'altra persona.",
            "8. Sentirsi dire che talvolta non si riconoscono amici o familiari.",
            "9. Accorgersi di non ricordare alcuni eventi importanti della propria vita (ad esempio, un matrimonio o una laurea).",
            "10. Essere accusati di mentire quando non si pensa di averlo fatto.",
            "11. Guardarsi nello specchio e non riconoscersi.",
            "12. Sentire come se le altre persone, gli oggetti e il mondo attorno non fossero reali.",
            "13. Sentire come se il proprio corpo non appartenesse a sé.",
            "14. Ricordare un evento passato in maniera così vivida e netta da sentirsi come se lo si stesse rivivendo.",
            "15. Non essere sicuri se eventi che si ricordano siano realmente avvenuti o se siano stati semplicemente sognati.",
            "16. Trovarsi in un posto familiare ma trovarlo strano e sconosciuto.",
            "17. Quando si guarda la televisione o un film, essere così presi dalla storia da non avere consapevolezza degli altri eventi che accadono intorno.",
            "18. Essere così coinvolti da una fantasia o da un sogno ad occhi aperti che sembra quasi di viverli realmente.",
            "19. Ritenere di essere talvolta in grado di ignorare il dolore.",
            "20. Stare seduti a fissare nel vuoto, senza pensare a niente, e non essere consapevoli del passare del tempo.",
            "21. Quando si è soli, parlare ad alta voce a se stessi.",
            "22. Agire così diversamente in una situazione rispetto ad un'altra da sentirsi quasi come se si fosse altre persone.",
            "23. Accorgersi talvolta che in certe situazioni si è in grado di fare cose che di solito risulterebbero difficili (ad esempio, sport, lavoro, situazioni sociali, ecc) con sorprendente facilità e spontaneità.",
            "24. Non riuscire a ricordare se si è fatto qualcosa o si è solamente pensato di farla (ad esempio, non sapere se si è appena spedito una lettera o si è solo pensato di inviarla).",
            "25. Accorgersi di aver fatto delle cose che non si ricordano di aver compiuto.",
            "26. Trovare a volte cose scritte, disegni o appunti tra le proprie cose, che si devono per forza aver fatto ma che non si riesce a ricordare di avere fatto.",
            "27. Sentire a volte delle voci dentro la propria testa che dicono di fare cose o commentano le azioni che si fanno.",
            "28. Sentirsi a volte come se si stesse guardando il mondo attraverso una cortina di nebbia, cosicché le altre persone o gli oggetti appaiono lontani o sfocati."
        ]
        opzioni = list(range(0, 101, 10))
        for i, domanda in enumerate(domande):
            st.session_state.risposte['des2'][i] = st.select_slider(
                domanda, options=opzioni, format_func=lambda x: f"{x}%",
                key=f"des2_{i}", on_change=on_change_test, args=('des2',)
            )

sezione_des2()


# ── MEWS ──────────────────────────────────────────────────────────────────────
@st.fragment
def sezione_mews():
    with st.expander("Questionario MEWS (Mental Effort / Mental Energy / Mental Restlessness Scale)"):
        st.info("Quanto sono comuni queste affermazioni per Voi")
        domande = [
            "1. Ho difficoltà a controllare i miei pensieri",
            "2. E' difficile spegnere i miei pensieri",
            "3. Ho due o più pensieri contemporaneamente in testa",
            "4. I miei pensieri sono disorganizzati e confusi",
            "5. I miei pensieri sono sempre in movimento",
            "6. Percepisco un'attività mentale senza sosta",
            "7. Faccio fatica a pensare ad una cosa senza che un altro pensiero entri nella mia testa",
            "8. Mi sembra che i miei pensieri siano fonte di distrazione e non mi permettano di concentrarmi su quello che sto facendo",
            "9. Ho difficoltà a rallentare i miei pensieri e concentrarmi su una cosa alla volta",
            "10. Faccio fatica a pensare con lucidità come se la mia mente fosse annebbiata",
            "11. Mi capita che i miei pensieri svolazzino qua e là",
            "12. Posso concentrare i miei pensieri solo su una cosa per volta, con grande sforzo",
        ]
        opzioni = ["Mai o raramente", "Qualche volta", "Per maggior parte del tempo", "Praticamente sempre, costantemente"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['mews'][i] = st.radio(
                domanda, options=range(len(opzioni)), format_func=lambda x: opzioni[x],
                key=f"mews_{i}", horizontal=True, on_change=on_change_test, args=('mews',)
            )

sezione_mews()


# ── ABAS-II ───────────────────────────────────────────────────────────────────
@st.fragment
def sezione_abas(data_nascita):
    with st.expander("Questionario ABAS-II (Adaptive Behavior Assessment System) — Eterovalutazione"):
        st.info(
            "Questo questionario viene compilato da un familiare o caregiver che conosce bene il soggetto. "
            "Per ogni abilità, indica se il soggetto la svolge e con quale frequenza. "
            "Spunta 'Suppongo' se non hai osservato direttamente il comportamento ma pensi che il soggetto sappia farlo."
        )

        eta_abas = int((datetime.date.today() - data_nascita).days / 365.25)
        fascia = fascia_eta(eta_abas)

        if fascia is None:
            st.warning(f"L'età del soggetto ({eta_abas} anni) è fuori dall'intervallo supportato (16–49 anni). Il questionario non verrà calcolato.")
            return

        st.session_state.risposte['abas']['eta'] = eta_abas
        if fascia != "16-21":
            st.info(f"Età rilevata: {eta_abas} anni (fascia {fascia}). I punteggi compositi (GAC, DAC, DAS, DAP) sono disponibili solo per la fascia 16–21; verranno mostrati i punteggi grezzi e ponderati per tutte le fasce.")

        ha_lavoro = st.radio(
            "Il soggetto svolge attualmente un'attività lavorativa?",
            options=["No", "Sì"], key="abas_lavoro", horizontal=True,
            on_change=on_change_test, args=('abas',)
        )
        st.session_state.risposte['abas']['ha_lavoro'] = (ha_lavoro == "Sì")

        aree_da_mostrare = list(AREE_ABAS.keys())
        if not st.session_state.risposte['abas']['ha_lavoro']:
            aree_da_mostrare = [a for a in aree_da_mostrare if a != "lavoro"]

        for area in aree_da_mostrare:
            info = AREE_ABAS[area]
            st.subheader(f"{info['label']} ({info['dominio']})")
            for i, item in enumerate(info['items']):
                col_radio, col_supp = st.columns([4, 1])
                with col_radio:
                    val = st.radio(
                        f"{i+1}. {item}",
                        options=list(OPZIONI_ABAS.keys()),
                        format_func=lambda x: OPZIONI_ABAS[x],
                        key=f"abas_{area}_{i}",
                        horizontal=True,
                        on_change=on_change_test,
                        args=('abas',)
                    )
                    st.session_state.risposte['abas']['risposte'][area][i] = val
                with col_supp:
                    supp = st.checkbox(
                        "Suppongo",
                        key=f"abas_supp_{area}_{i}",
                        on_change=on_change_test,
                        args=('abas',)
                    )
                    st.session_state.risposte['abas']['suppongo'][area][i] = supp

sezione_abas(data_nascita)


# ── STAI-Y-2 ──────────────────────────────────────────────────────────────────
@st.fragment
def sezione_stai_y2():
    with st.expander("Questionario STAI-Y-2 (Ansia di Tratto)"):
        st.info("Leggi le frasi seguenti e indica quanto ti senti **generalmente**, nella maggior parte dei casi.")
        domande = [
            "1. Mi sento bene", "2. Mi sento teso ed irrequieto", "3. Sono soddisfatto di me stesso",
            "4. Vorrei poter essere felice come sembrano gli altri", "5. Mi sento un fallito", "6. Mi sento riposato",
            "7. Io sono calmo, tranquillo e padrone di me", "8. Sento che le difficoltà si accumulano tanto da non poterle superare",
            "9. Mi preoccupo troppo di cose che in realtà non hanno importanza", "10. Sono felice",
            "11. Mi vengono pensieri negativi", "12. Manco di fiducia in me stesso", "13. Mi sento sicuro",
            "14. Prendo decisioni facilmente", "15. Mi sento inadeguato", "16. Sono contento",
            "17. Pensieri di scarsa importanza mi passano per la mente e mi infastidiscono", "18. Vivo le delusioni con tanta partecipazione da non poter togliermele dalla testa",
            "19. Sono una persona costante", "20. Divento teso e turbato quando penso alle mie attuali condizioni"
        ]
        opzioni = ["Per nulla", "Un po'", "Abbastanza", "Moltissimo"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['stai_y2'][i] = st.radio(
                domanda, options=range(1, 5), format_func=lambda x: opzioni[x-1],
                key=f"stai_y2_{i}", horizontal=True, on_change=on_change_test, args=('stai_y2',)
            )

sezione_stai_y2()


# ── STAI-Y-1 ──────────────────────────────────────────────────────────────────
@st.fragment
def sezione_stai_y1():
    with st.expander("Questionario STAI-Y-1 (Ansia di Stato)"):
        st.info("Leggi le frasi seguenti e indica come ti senti **adesso**, in questo preciso momento.")
        domande = [
            "1. Mi sento calmo", "2. Mi sento sicuro", "3. Sono teso", "4. Mi sento sotto pressione",
            "5. Mi sento tranquillo", "6. Mi sento turbato", "7. Sono attualmente preoccupato per possibili disgrazie",
            "8. Mi sento soddisfatto", "9. Mi sento intimorito", "10. Mi sento a mio agio",
            "11. Mi sento sicuro di me", "12. Mi sento nervoso", "13. Sono agitato", "14. Mi sento indeciso",
            "15. Sono rilassato", "16. Mi sento contento", "17. Sono preoccupato", "18. Mi sento confuso",
            "19. Mi sento disteso", "20. Mi sento bene"
        ]
        opzioni = ["Per nulla", "Un po'", "Abbastanza", "Moltissimo"]
        for i, domanda in enumerate(domande):
            st.session_state.risposte['stai_y1'][i] = st.radio(
                domanda, options=range(1, 5), format_func=lambda x: opzioni[x-1],
                key=f"stai_y1_{i}", horizontal=True, on_change=on_change_test, args=('stai_y1',)
            )

sezione_stai_y1()


# ── Pulsante di Invio ─────────────────────────────────────────────────────────
st.divider()
st.header("3. Invia i risultati")
st.info("Una volta completati i questionari indicati, clicca il pulsante qui sotto per inviare le tue risposte in modo sicuro allo specialista.")

if st.button("Invia i risultati in modo sicuro", type="primary", use_container_width=True):
    if not codice_paziente or codice_paziente.strip() == "":
        st.error("⚠️ **Errore:** Per favore, inserisci il 'Codice Paziente' che ti è stato fornito prima di inviare.")
    elif not st.session_state.test_compilati:
        st.warning("⚠️ **Attenzione:** Non hai compilato nessun questionario. Apri uno dei questionari e rispondi ad almeno una domanda prima di inviare.")
    else:
        with st.spinner("Calcolo dei risultati e invio in corso... Per favore, attendi."):
            try:
                dati_paziente = {
                    "codice_paziente": codice_paziente, "data_nascita": data_nascita,
                    "genere": genere, "livello_istruzione": livello_istruzione
                }

                risultati_completi = calcola_tutti_i_risultati(st.session_state.risposte, st.session_state.test_compilati, dati_paziente['genere'])

                corpo_email = formatta_risultati_email(dati_paziente, risultati_completi, st.session_state.risposte['wurs_extra_testo'])

                email_mittente = st.secrets["email_mittente"]
                password_app = st.secrets["password_app"]
                email_destinatario = st.secrets["email_destinatario"]

                msg = MIMEMultipart()
                msg['From'] = email_mittente
                msg['To'] = email_destinatario
                msg['Subject'] = f"Nuova Compilazione Test - Paziente: {codice_paziente}"
                msg.attach(MIMEText(corpo_email, 'html'))

                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login(email_mittente, password_app)
                server.sendmail(email_mittente, email_destinatario, msg.as_string())
                server.quit()

                st.success("✔️ **Invio completato con successo!**")
                st.info("Grazie per aver completato i questionari. Ora puoi chiudere questa pagina.")
                st.balloons()
                st.session_state.test_compilati = set()

            except Exception as e:
                st.error("❌ Si è verificato un errore durante l'invio. Per favore, contatta il tuo specialista e segnala il problema.")
                st.exception(e)
