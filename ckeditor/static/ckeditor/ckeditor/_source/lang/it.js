﻿/*
 Copyright (c) 2003-2011, CKSource - Frederico Knabben. All rights reserved.
 For licensing, see LICENSE.html or http://ckeditor.com/license
 */

/**
 * @fileOverview Defines the {@link CKEDITOR.lang} object, for the
 * Italian language.
 */

/**#@+
 @type String
 @example
 */

/**
 * Contains the dictionary of language entries.
 * @namespace
 */
CKEDITOR.lang['it'] =
{
    /**
     * The language reading direction. Possible values are "rtl" for
     * Right-To-Left languages (like Arabic) and "ltr" for Left-To-Right
     * languages (like English).
     * @default 'ltr'
     */
    dir: 'ltr',

    /*
     * Screenreader titles. Please note that screenreaders are not always capable
     * of reading non-English words. So be careful while translating it.
     */
    editorTitle: 'Rich text editor, %1, premere ALT 0 per l\'help in linea.',

    // ARIA descriptions.
    toolbars: 'Editor toolbar',
    editor: 'Rich Text Editor',

    // Toolbar buttons without dialogs.
    source: 'Codice Sorgente',
    newPage: 'Nuova pagina vuota',
    save: 'Salva',
    preview: 'Anteprima',
    cut: 'Taglia',
    copy: 'Copia',
    paste: 'Incolla',
    print: 'Stampa',
    underline: 'Sottolineato',
    bold: 'Grassetto',
    italic: 'Corsivo',
    selectAll: 'Seleziona tutto',
    removeFormat: 'Elimina formattazione',
    strike: 'Barrato',
    subscript: 'Pedice',
    superscript: 'Apice',
    horizontalrule: 'Inserisci riga orizzontale',
    pagebreak: 'Inserisci interruzione di pagina',
    pagebreakAlt: 'Interruzione di pagina',
    unlink: 'Elimina collegamento',
    undo: 'Annulla',
    redo: 'Ripristina',

    // Common messages and labels.
    common: {
        browseServer: 'Cerca sul server',
        url: 'URL',
        protocol: 'Protocollo',
        upload: 'Carica',
        uploadSubmit: 'Invia al server',
        image: 'Immagine',
        flash: 'Oggetto Flash',
        form: 'Modulo',
        checkbox: 'Checkbox',
        radio: 'Radio Button',
        textField: 'Campo di testo',
        textarea: 'Area di testo',
        hiddenField: 'Campo nascosto',
        button: 'Bottone',
        select: 'Menu di selezione',
        imageButton: 'Bottone immagine',
        notSet: '<non impostato>',
        id: 'Id',
        name: 'Nome',
        langDir: 'Direzione scrittura',
        langDirLtr: 'Da Sinistra a Destra (LTR)',
        langDirRtl: 'Da Destra a Sinistra (RTL)',
        langCode: 'Codice Lingua',
        longDescr: 'URL descrizione estesa',
        cssClass: 'Nome classe CSS',
        advisoryTitle: 'Titolo',
        cssStyle: 'Stile',
        ok: 'OK',
        cancel: 'Annulla',
        close: 'Chiudi',
        preview: 'Anteprima',
        generalTab: 'Generale',
        advancedTab: 'Avanzate',
        validateNumberFailed: 'Il valore inserito non è un numero.',
        confirmNewPage: 'Ogni modifica non salvata sarà persa. Sei sicuro di voler caricare una nuova pagina?',
        confirmCancel: 'Alcune delle opzioni sono state cambiate. Sei sicuro di voler chiudere la finestra di dialogo?',
        options: 'Opzioni',
        target: 'Destinazione',
        targetNew: 'Nuova finestra (_blank)',
        targetTop: 'Finestra in primo piano (_top)',
        targetSelf: 'Stessa finestra (_self)',
        targetParent: 'Finestra Padre (_parent)',
        langDirLTR: 'Da sinistra a destra (LTR)',
        langDirRTL: 'Da destra a sinistra (RTL)',
        styles: 'Stile',
        cssClasses: 'Classi di stile',
        width: 'Larghezza',
        height: 'Altezza',
        align: 'Allineamento',
        alignLeft: 'Sinistra',
        alignRight: 'Destra',
        alignCenter: 'Centrato',
        alignTop: 'In Alto',
        alignMiddle: 'Centrato',
        alignBottom: 'In Basso',
        invalidHeight: 'L\'altezza dev\'essere un numero',
        invalidWidth: 'La Larghezza dev\'essere un numero',
        invalidCssLength: 'Il valore indicato per il campo "%1" deve essere un numero positivo con o senza indicazione di una valida unità di misura per le classi CSS (px, %, in, cm, mm, em, ex, pt, o pc).',
        invalidHtmlLength: 'Il valore indicato per il campo "%1" deve essere un numero positivo con o senza indicazione di una valida unità di misura per le pagine HTML (px o %).',
        invalidInlineStyle: 'Value specified for the inline style must consist of one or more tuples with the format of "name : value", separated by semi-colons.', // MISSING
        cssLengthTooltip: 'Enter a number for a value in pixels or a number with a valid CSS unit (px, %, in, cm, mm, em, ex, pt, or pc).', // MISSING

        // Put the voice-only part of the label in the span.
        unavailable: '%1<span class="cke_accessibility">, non disponibile</span>'
    },

    contextmenu: {
        options: 'Opzioni del menù contestuale'
    },

    // Special char dialog.
    specialChar: {
        toolbar: 'Inserisci carattere speciale',
        title: 'Seleziona carattere speciale',
        options: 'Opzioni carattere speciale'
    },

    // Link dialog.
    link: {
        toolbar: 'Inserisci/Modifica collegamento',
        other: '<altro>',
        menu: 'Modifica collegamento',
        title: 'Collegamento',
        info: 'Informazioni collegamento',
        target: 'Destinazione',
        upload: 'Carica',
        advanced: 'Avanzate',
        type: 'Tipo di Collegamento',
        toUrl: 'URL',
        toAnchor: 'Ancora nella pagina',
        toEmail: 'E-Mail',
        targetFrame: '<riquadro>',
        targetPopup: '<finestra popup>',
        targetFrameName: 'Nome del riquadro di destinazione',
        targetPopupName: 'Nome finestra popup',
        popupFeatures: 'Caratteristiche finestra popup',
        popupResizable: 'Ridimensionabile',
        popupStatusBar: 'Barra di stato',
        popupLocationBar: 'Barra degli indirizzi',
        popupToolbar: 'Barra degli strumenti',
        popupMenuBar: 'Barra del menu',
        popupFullScreen: 'A tutto schermo (IE)',
        popupScrollBars: 'Barre di scorrimento',
        popupDependent: 'Dipendente (Netscape)',
        popupLeft: 'Posizione da sinistra',
        popupTop: 'Posizione dall\'alto',
        id: 'Id',
        langDir: 'Direzione scrittura',
        langDirLTR: 'Da Sinistra a Destra (LTR)',
        langDirRTL: 'Da Destra a Sinistra (RTL)',
        acccessKey: 'Scorciatoia<br />da tastiera',
        name: 'Nome',
        langCode: 'Direzione scrittura',
        tabIndex: 'Ordine di tabulazione',
        advisoryTitle: 'Titolo',
        advisoryContentType: 'Tipo della risorsa collegata',
        cssClasses: 'Nome classe CSS',
        charset: 'Set di caretteri della risorsa collegata',
        styles: 'Stile',
        rel: 'Relazioni',
        selectAnchor: 'Scegli Ancora',
        anchorName: 'Per Nome',
        anchorId: 'Per id elemento',
        emailAddress: 'Indirizzo E-Mail',
        emailSubject: 'Oggetto del messaggio',
        emailBody: 'Corpo del messaggio',
        noAnchors: '(Nessuna ancora disponibile nel documento)',
        noUrl: 'Devi inserire l\'URL del collegamento',
        noEmail: 'Devi inserire un\'indirizzo e-mail'
    },

    // Anchor dialog
    anchor: {
        toolbar: 'Inserisci/Modifica Ancora',
        menu: 'Proprietà ancora',
        title: 'Proprietà ancora',
        name: 'Nome ancora',
        errorName: 'Inserici il nome dell\'ancora',
        remove: 'Rimuovi l\'ancora'
    },

    // List style dialog
    list: {
        numberedTitle: 'Proprietà liste numerate',
        bulletedTitle: 'Proprietà liste puntate',
        type: 'Tipo',
        start: 'Inizio',
        validateStartNumber: 'Il numero di inizio di una lista numerata deve essere un numero intero.',
        circle: 'Cerchio',
        disc: 'Disco',
        square: 'Quadrato',
        none: 'Nessuno',
        notset: '<non impostato>',
        armenian: 'Numerazione Armena',
        georgian: 'Numerazione Georgiana (an, ban, gan, ecc.)',
        lowerRoman: 'Numerazione Romana minuscola (i, ii, iii, iv, v, ecc.)',
        upperRoman: 'Numerazione Romana maiuscola (I, II, III, IV, V, ecc.)',
        lowerAlpha: 'Alfabetico minuscolo (a, b, c, d, e, ecc.)',
        upperAlpha: 'Alfabetico maiuscolo (A, B, C, D, E, ecc.)',
        lowerGreek: 'Greco minuscolo (alpha, beta, gamma, ecc.)',
        decimal: 'Decimale (1, 2, 3, ecc.)',
        decimalLeadingZero: 'Decimale preceduto da 0 (01, 02, 03, ecc.)'
    },

    // Find And Replace Dialog
    findAndReplace: {
        title: 'Cerca e Sostituisci',
        find: 'Trova',
        replace: 'Sostituisci',
        findWhat: 'Trova:',
        replaceWith: 'Sostituisci con:',
        notFoundMsg: 'L\'elemento cercato non è stato trovato.',
        findOptions: 'Find Options', // MISSING
        matchCase: 'Maiuscole/minuscole',
        matchWord: 'Solo parole intere',
        matchCyclic: 'Ricerca ciclica',
        replaceAll: 'Sostituisci tutto',
        replaceSuccessMsg: '%1 occorrenza(e) sostituite.'
    },

    // Table Dialog
    table: {
        toolbar: 'Tabella',
        title: 'Proprietà tabella',
        menu: 'Proprietà tabella',
        deleteTable: 'Cancella Tabella',
        rows: 'Righe',
        columns: 'Colonne',
        border: 'Dimensione bordo',
        widthPx: 'pixel',
        widthPc: 'percento',
        widthUnit: 'unità larghezza',
        cellSpace: 'Spaziatura celle',
        cellPad: 'Padding celle',
        caption: 'Intestazione',
        summary: 'Indice',
        headers: 'Intestazione',
        headersNone: 'Nessuna',
        headersColumn: 'Prima Colonna',
        headersRow: 'Prima Riga',
        headersBoth: 'Entrambe',
        invalidRows: 'Il numero di righe dev\'essere un numero maggiore di 0.',
        invalidCols: 'Il numero di colonne dev\'essere un numero maggiore di 0.',
        invalidBorder: 'La dimensione del bordo dev\'essere un numero.',
        invalidWidth: 'La larghezza della tabella dev\'essere un numero.',
        invalidHeight: 'L\'altezza della tabella dev\'essere un numero.',
        invalidCellSpacing: 'La spaziatura tra le celle dev\'essere un numero.',
        invalidCellPadding: 'Il paging delle celle dev\'essere un numero',

        cell: {
            menu: 'Cella',
            insertBefore: 'Inserisci Cella Prima',
            insertAfter: 'Inserisci Cella Dopo',
            deleteCell: 'Elimina celle',
            merge: 'Unisce celle',
            mergeRight: 'Unisci a Destra',
            mergeDown: 'Unisci in Basso',
            splitHorizontal: 'Dividi Cella Orizzontalmente',
            splitVertical: 'Dividi Cella Verticalmente',
            title: 'Proprietà della cella',
            cellType: 'Tipo di cella',
            rowSpan: 'Su più righe',
            colSpan: 'Su più colonne',
            wordWrap: 'Ritorno a capo',
            hAlign: 'Allineamento orizzontale',
            vAlign: 'Allineamento verticale',
            alignBaseline: 'Linea Base',
            bgColor: 'Colore di Sfondo',
            borderColor: 'Colore del Bordo',
            data: 'Dati',
            header: 'Intestazione',
            yes: 'Si',
            no: 'No',
            invalidWidth: 'La larghezza della cella dev\'essere un numero.',
            invalidHeight: 'L\'altezza della cella dev\'essere un numero.',
            invalidRowSpan: 'Il numero di righe dev\'essere un numero intero.',
            invalidColSpan: 'Il numero di colonne dev\'essere un numero intero.',
            chooseColor: 'Scegli'
        },

        row: {
            menu: 'Riga',
            insertBefore: 'Inserisci Riga Prima',
            insertAfter: 'Inserisci Riga Dopo',
            deleteRow: 'Elimina righe'
        },

        column: {
            menu: 'Colonna',
            insertBefore: 'Inserisci Colonna Prima',
            insertAfter: 'Inserisci Colonna Dopo',
            deleteColumn: 'Elimina colonne'
        }
    },

    // Button Dialog.
    button: {
        title: 'Proprietà bottone',
        text: 'Testo (Valore)',
        type: 'Tipo',
        typeBtn: 'Bottone',
        typeSbm: 'Invio',
        typeRst: 'Annulla'
    },

    // Checkbox and Radio Button Dialogs.
    checkboxAndRadio: {
        checkboxTitle: 'Proprietà checkbox',
        radioTitle: 'Proprietà radio button',
        value: 'Valore',
        selected: 'Selezionato'
    },

    // Form Dialog.
    form: {
        title: 'Proprietà modulo',
        menu: 'Proprietà modulo',
        action: 'Azione',
        method: 'Metodo',
        encoding: 'Codifica'
    },

    // Select Field Dialog.
    select: {
        title: 'Proprietà menu di selezione',
        selectInfo: 'Info',
        opAvail: 'Opzioni disponibili',
        value: 'Valore',
        size: 'Dimensione',
        lines: 'righe',
        chkMulti: 'Permetti selezione multipla',
        opText: 'Testo',
        opValue: 'Valore',
        btnAdd: 'Aggiungi',
        btnModify: 'Modifica',
        btnUp: 'Su',
        btnDown: 'Gi',
        btnSetValue: 'Imposta come predefinito',
        btnDelete: 'Rimuovi'
    },

    // Textarea Dialog.
    textarea: {
        title: 'Proprietà area di testo',
        cols: 'Colonne',
        rows: 'Righe'
    },

    // Text Field Dialog.
    textfield: {
        title: 'Proprietà campo di testo',
        name: 'Nome',
        value: 'Valore',
        charWidth: 'Larghezza',
        maxChars: 'Numero massimo di caratteri',
        type: 'Tipo',
        typeText: 'Testo',
        typePass: 'Password'
    },

    // Hidden Field Dialog.
    hidden: {
        title: 'Proprietà campo nascosto',
        name: 'Nome',
        value: 'Valore'
    },

    // Image Dialog.
    image: {
        title: 'Proprietà immagine',
        titleButton: 'Proprietà bottone immagine',
        menu: 'Proprietà immagine',
        infoTab: 'Informazioni immagine',
        btnUpload: 'Invia al server',
        upload: 'Carica',
        alt: 'Testo alternativo',
        lockRatio: 'Blocca rapporto',
        resetSize: 'Reimposta dimensione',
        border: 'Bordo',
        hSpace: 'HSpace',
        vSpace: 'VSpace',
        alertUrl: 'Devi inserire l\'URL per l\'immagine',
        linkTab: 'Collegamento',
        button2Img: 'Vuoi trasformare il bottone immagine selezionato in un\'immagine semplice?',
        img2Button: 'Vuoi trasferomare l\'immagine selezionata in un bottone immagine?',
        urlMissing: 'Manca l\'URL dell\'immagine.',
        validateBorder: 'Il campo Bordo deve essere un numero intero.',
        validateHSpace: 'Il campo HSpace deve essere un numero intero.',
        validateVSpace: 'Il campo VSpace deve essere un numero intero.'
    },

    // Flash Dialog
    flash: {
        properties: 'Proprietà Oggetto Flash',
        propertiesTab: 'Proprietà',
        title: 'Proprietà Oggetto Flash',
        chkPlay: 'Avvio Automatico',
        chkLoop: 'Riavvio automatico',
        chkMenu: 'Abilita Menu di Flash',
        chkFull: 'Permetti la modalità tutto schermo',
        scale: 'Ridimensiona',
        scaleAll: 'Mostra Tutto',
        scaleNoBorder: 'Senza Bordo',
        scaleFit: 'Dimensione Esatta',
        access: 'Accesso Script',
        accessAlways: 'Sempre',
        accessSameDomain: 'Solo stesso dominio',
        accessNever: 'Mai',
        alignAbsBottom: 'In basso assoluto',
        alignAbsMiddle: 'Centrato assoluto',
        alignBaseline: 'Linea base',
        alignTextTop: 'In alto al testo',
        quality: 'Qualità',
        qualityBest: 'Massima',
        qualityHigh: 'Alta',
        qualityAutoHigh: 'Alta Automatica',
        qualityMedium: 'Intermedia',
        qualityAutoLow: 'Bassa Automatica',
        qualityLow: 'Bassa',
        windowModeWindow: 'Finestra',
        windowModeOpaque: 'Opaca',
        windowModeTransparent: 'Trasparente',
        windowMode: 'Modalità finestra',
        flashvars: 'Variabili per Flash',
        bgcolor: 'Colore sfondo',
        hSpace: 'HSpace',
        vSpace: 'VSpace',
        validateSrc: 'Devi inserire l\'URL del collegamento',
        validateHSpace: 'L\'HSpace dev\'essere un numero.',
        validateVSpace: 'Il VSpace dev\'essere un numero.'
    },

    // Speller Pages Dialog
    spellCheck: {
        toolbar: 'Correttore ortografico',
        title: 'Controllo ortografico',
        notAvailable: 'Il servizio non è momentaneamente disponibile.',
        errorLoading: 'Errore nel caricamento dell\'host col servizio applicativo: %s.',
        notInDic: 'Non nel dizionario',
        changeTo: 'Cambia in',
        btnIgnore: 'Ignora',
        btnIgnoreAll: 'Ignora tutto',
        btnReplace: 'Cambia',
        btnReplaceAll: 'Cambia tutto',
        btnUndo: 'Annulla',
        noSuggestions: '- Nessun suggerimento -',
        progress: 'Controllo ortografico in corso',
        noMispell: 'Controllo ortografico completato: nessun errore trovato',
        noChanges: 'Controllo ortografico completato: nessuna parola cambiata',
        oneChange: 'Controllo ortografico completato: 1 parola cambiata',
        manyChanges: 'Controllo ortografico completato: %1 parole cambiate',
        ieSpellDownload: 'Contollo ortografico non installato. Lo vuoi scaricare ora?'
    },

    smiley: {
        toolbar: 'Emoticon',
        title: 'Inserisci emoticon',
        options: 'Opzioni Smiley'
    },

    elementsPath: {
        eleLabel: 'Percorso degli elementi',
        eleTitle: '%1 elemento'
    },

    numberedlist: 'Elenco numerato',
    bulletedlist: 'Elenco puntato',
    indent: 'Aumenta rientro',
    outdent: 'Riduci rientro',

    justify: {
        left: 'Allinea a sinistra',
        center: 'Centra',
        right: 'Allinea a destra',
        block: 'Giustifica'
    },

    blockquote: 'Citazione',

    clipboard: {
        title: 'Incolla',
        cutError: 'Le impostazioni di sicurezza del browser non permettono di tagliare automaticamente il testo. Usa la tastiera (Ctrl/Cmd+X).',
        copyError: 'Le impostazioni di sicurezza del browser non permettono di copiare automaticamente il testo. Usa la tastiera (Ctrl/Cmd+C).',
        pasteMsg: 'Incolla il testo all\'interno dell\'area sottostante usando la scorciatoia di tastiere (<STRONG>Ctrl/Cmd+V</STRONG>) e premi <STRONG>OK</STRONG>.',
        securityMsg: 'A causa delle impostazioni di sicurezza del browser,l\'editor non è in grado di accedere direttamente agli appunti. E\' pertanto necessario incollarli di nuovo in questa finestra.',
        pasteArea: 'Incolla'
    },

    pastefromword: {
        confirmCleanup: 'Il testo da incollare sembra provenire da Word. Desideri pulirlo prima di incollare?',
        toolbar: 'Incolla da Word',
        title: 'Incolla da Word',
        error: 'Non è stato possibile eliminarre il testo incollato a causa di un errore interno.'
    },

    pasteText: {
        button: 'Incolla come testo semplice',
        title: 'Incolla come testo semplice'
    },

    templates: {
        button: 'Modelli',
        title: 'Contenuto dei modelli',
        options: 'Opzioni del Modello',
        insertOption: 'Cancella il contenuto corrente',
        selectPromptMsg: 'Seleziona il modello da aprire nell\'editor<br />(il contenuto attuale verrà eliminato):',
        emptyListMsg: '(Nessun modello definito)'
    },

    showBlocks: 'Visualizza Blocchi',

    stylesCombo: {
        label: 'Stile',
        panelTitle: 'Stili di formattazione',
        panelTitle1: 'Stili per blocchi',
        panelTitle2: 'Stili in linea',
        panelTitle3: 'Stili per oggetti'
    },

    format: {
        label: 'Formato',
        panelTitle: 'Formato',

        tag_p: 'Normale',
        tag_pre: 'Formattato',
        tag_address: 'Indirizzo',
        tag_h1: 'Titolo 1',
        tag_h2: 'Titolo 2',
        tag_h3: 'Titolo 3',
        tag_h4: 'Titolo 4',
        tag_h5: 'Titolo 5',
        tag_h6: 'Titolo 6',
        tag_div: 'Paragrafo (DIV)'
    },

    div: {
        title: 'Crea DIV contenitore',
        toolbar: 'Crea DIV contenitore',
        cssClassInputLabel: 'Classi di stile',
        styleSelectLabel: 'Stile',
        IdInputLabel: 'Id',
        languageCodeInputLabel: 'Codice lingua',
        inlineStyleInputLabel: 'Stile Inline',
        advisoryTitleInputLabel: 'Titolo Avviso',
        langDirLabel: 'Direzione di scrittura',
        langDirLTRLabel: 'Da sinistra a destra (LTR)',
        langDirRTLLabel: 'Da destra a sinistra (RTL)',
        edit: 'Modifica DIV',
        remove: 'Rimuovi DIV'
    },

    iframe: {
        title: 'Proprietà IFrame',
        toolbar: 'IFrame',
        noUrl: 'Inserire l\'URL del campo IFrame',
        scrolling: 'Abilita scrollbar',
        border: 'Mostra il bordo'
    },

    font: {
        label: 'Carattere',
        voiceLabel: 'Carattere',
        panelTitle: 'Carattere'
    },

    fontSize: {
        label: 'Dimensione',
        voiceLabel: 'Dimensione Carattere',
        panelTitle: 'Dimensione'
    },

    colorButton: {
        textColorTitle: 'Colore testo',
        bgColorTitle: 'Colore sfondo',
        panelTitle: 'Colori',
        auto: 'Automatico',
        more: 'Altri colori...'
    },

    colors: {
        '000': 'Nero',
        '800000': 'Marrone Castagna',
        '8B4513': 'Marrone Cuoio',
        '2F4F4F': 'Grigio Fumo di Londra',
        '008080': 'Acquamarina',
        '000080': 'Blu Oceano',
        '4B0082': 'Indigo',
        '696969': 'Grigio Scuro',
        'B22222': 'Giallo Fiamma',
        'A52A2A': 'Marrone',
        'DAA520': 'Giallo Mimosa',
        '006400': 'Verde Scuro',
        '40E0D0': 'Turchese',
        '0000CD': 'Blue Scuro',
        '800080': 'Viola',
        '808080': 'Grigio',
        'F00': 'Rosso',
        'FF8C00': 'Arancio Scuro',
        'FFD700': 'Oro',
        '008000': 'Verde',
        '0FF': 'Ciano',
        '00F': 'Blu',
        'EE82EE': 'Violetto',
        'A9A9A9': 'Grigio Scuro',
        'FFA07A': 'Salmone',
        'FFA500': 'Arancio',
        'FFFF00': 'Giallo',
        '00FF00': 'Lime',
        'AFEEEE': 'Turchese Chiaro',
        'ADD8E6': 'Blu Chiaro',
        'DDA0DD': 'Rosso Ciliegia',
        'D3D3D3': 'Grigio Chiaro',
        'FFF0F5': 'Lavanda Chiara',
        'FAEBD7': 'Bianco Antico',
        'FFFFE0': 'Giallo Chiaro',
        'F0FFF0': 'Verde Mela',
        'F0FFFF': 'Azzurro',
        'F0F8FF': 'Celeste',
        'E6E6FA': 'Lavanda',
        'FFF': 'Bianco'
    },

    scayt: {
        title: 'Controllo Ortografico Mentre Scrivi',
        opera_title: 'Non supportato da Opera',
        enable: 'Abilita COMS',
        disable: 'Disabilita COMS',
        about: 'About COMS',
        toggle: 'Inverti abilitazione SCOMS',
        options: 'Opzioni',
        langs: 'Lingue',
        moreSuggestions: 'Altri suggerimenti',
        ignore: 'Ignora',
        ignoreAll: 'Ignora tutti',
        addWord: 'Aggiungi Parola',
        emptyDic: 'Il nome del dizionario non può essere vuoto.',

        optionsTab: 'Opzioni',
        allCaps: 'Ignora Parole in maiuscolo',
        ignoreDomainNames: 'Ignora nomi di dominio',
        mixedCase: 'Ignora parole con maiuscole e minuscole',
        mixedWithDigits: 'Ignora parole con numeri',

        languagesTab: 'Lingue',

        dictionariesTab: 'Dizionari',
        dic_field_name: 'Nome del dizionario',
        dic_create: 'Crea',
        dic_restore: 'Ripristina',
        dic_delete: 'Cancella',
        dic_rename: 'Rinomina',
        dic_info: 'Inizialmente il dizionario utente è memorizzato in un Cookie. I Cookie però hanno una dimensioni massima limitata. Quando il dizionario utente creasce a tal punto da non poter più essere memorizzato in un Cookie, allora il dizionario può essere memorizzato sul nostro server. Per memorizzare il proprio dizionario personale sul nostro server, è necessario specificare un nome per il proprio dizionario. Se avete già memorizzato un dizionario, inserite il nome che gli avete dato e premete il pulsante Ripristina.',

        aboutTab: 'Info'
    },

    about: {
        title: 'Riguardo CKEditor',
        dlgTitle: 'Riguardo CKEditor',
        help: 'Vedi $1 per l\'aiuto.',
        userGuide: 'Guida Utente CKEditor',
        moreInfo: 'Per le informazioni sulla licenza si prega di visitare il nostro sito:',
        copy: 'Copyright &copy; $1. Tutti i diritti riservati.'
    },

    maximize: 'Massimizza',
    minimize: 'Minimizza',

    fakeobjects: {
        anchor: 'Ancora',
        flash: 'Animazione Flash',
        iframe: 'IFrame',
        hiddenfield: 'Campo Nascosto',
        unknown: 'Oggetto sconosciuto'
    },

    resize: 'Trascina per ridimensionare',

    colordialog: {
        title: 'Selezionare il colore',
        options: 'Opzioni colore',
        highlight: 'Evidenzia',
        selected: 'Seleziona il colore',
        clear: 'cancella'
    },

    toolbarCollapse: 'Minimizza Toolbar',
    toolbarExpand: 'Espandi Toolbar',

    toolbarGroups: {
        document: 'Documento',
        clipboard: 'Copia negli appunti/Indietro',
        editing: 'Modifica',
        forms: 'Form',
        basicstyles: 'Stili di base',
        paragraph: 'Paragrafo',
        links: 'Link',
        insert: 'Inserisci',
        styles: 'Stili',
        colors: 'Colori',
        tools: 'Strumenti'
    },

    bidi: {
        ltr: 'Direzione del testo da sinistra verso destra',
        rtl: 'Direzione del testo da destra verso sinistra'
    },

    docprops: {
        label: 'Proprietà del Documento',
        title: 'Proprietà del Documento',
        design: 'Disegna',
        meta: 'Meta Data',
        chooseColor: 'Scegli',
        other: '<altro>',
        docTitle: 'Titolo pagina',
        charset: 'Set di caretteri',
        charsetOther: 'Altro set di caretteri',
        charsetASCII: 'ASCII',
        charsetCE: 'Europa Centrale',
        charsetCT: 'Cinese Tradizionale (Big5)',
        charsetCR: 'Cirillico',
        charsetGR: 'Greco',
        charsetJP: 'Giapponese',
        charsetKR: 'Coreano',
        charsetTR: 'Turco',
        charsetUN: 'Unicode (UTF-8)',
        charsetWE: 'Europa Occidentale',
        docType: 'Intestazione DocType',
        docTypeOther: 'Altra intestazione DocType',
        xhtmlDec: 'Includi dichiarazione XHTML',
        bgColor: 'Colore di sfondo',
        bgImage: 'Immagine di sfondo',
        bgFixed: 'Sfondo fissato',
        txtColor: 'Colore testo',
        margin: 'Margini',
        marginTop: 'In Alto',
        marginLeft: 'A Sinistra',
        marginRight: 'A Destra',
        marginBottom: 'In Basso',
        metaKeywords: 'Chiavi di indicizzazione documento (separate da virgola)',
        metaDescription: 'Descrizione documento',
        metaAuthor: 'Autore',
        metaCopyright: 'Copyright',
        previewHtml: '<p>Questo è un <strong>testo di esempio</strong>. State usando <a href="javascript:void(0)">CKEditor</a>.</p>'
    }
};
