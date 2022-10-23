
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "BT136-800"
    hexID = "SZKTRIACTHYRISTORBT1368"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TIC226', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BT136-800', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'http://www.micropik.com/PDF/BT136-600.pdf', 'kicadSymbolki_keywords': 'Triac', 'kicadSymbolki_description': '4A RMS, 800V Off-State Voltage, Triac, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('BT136-800')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

