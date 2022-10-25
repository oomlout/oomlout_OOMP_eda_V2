
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Triac_Thyristor"
    oIndex = "BT138-600"
    hexID = "SZKTRIACTHYRISTORBT1386"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TIC226', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BT138-600', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-3_Vertical', 'kicadSymbolDatasheet': 'https://assets.nexperia.com/documents/data-sheet/BT138_SER_D_E.pdf', 'kicadSymbolki_keywords': 'Triac', 'kicadSymbolki_description': '12A RMS, 600V Off-State Voltage, Triac, TO-220', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('Triac_Thyristor : BT138-600')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

