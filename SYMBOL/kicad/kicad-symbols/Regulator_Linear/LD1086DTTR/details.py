
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD1086DTTR"
    hexID = "SZKREGULATORLINEARLD186DTTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD1086DTTR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-2', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/ld1086.pdf', 'kicadSymbolki_keywords': 'Linear Regulator 1.5A Adjustable', 'kicadSymbolki_description': 'Positive, 1.5A 30V, Linear Regulator, Adjustable, TO-252', 'kicadSymbolki_fp_filters': 'TO?252?2*'}])
    newPart['name'].append('Regulator_Linear : LD1086DTTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

