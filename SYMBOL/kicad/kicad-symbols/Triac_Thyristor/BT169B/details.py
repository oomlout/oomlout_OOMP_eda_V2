
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "BT169B"
    hexID = "SZKTRIACTHYRISTORBT169B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BT169B', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/NXP%20PDFs/BT169_Series.pdf', 'kicadSymbolki_keywords': 'thyristor logic level', 'kicadSymbolki_description': '0.5A Ion, 200V Voff, Thyristors logic level, Silicon Controlled Rectifier (Thyristor), TO-92', 'kicadSymbolki_fp_filters': 'TO?92*Inline*Narrow*'}])
    newPart['name'].append('BT169B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

