
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD1086D2MTR"
    hexID = "SZKREGULATORLINEARLD186D2MTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD1086D2MTR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-3_TabPin2', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/ld1086.pdf', 'kicadSymbolki_keywords': 'Linear Regulator 1.5A Adjustable', 'kicadSymbolki_description': 'Positive, 1.5A 30V, Linear Regulator, Adjustable TO-263', 'kicadSymbolki_fp_filters': 'TO?263*TabPin2*'}])
    newPart['name'].append('Regulator_Linear : LD1086D2MTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

