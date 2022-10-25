
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "DTC115G"
    hexID = "SZKTRANSISTORBJTDTC115G"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DTC115G', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'ROHM Digital NPN Transistor', 'kicadSymbolki_description': 'Digital NPN Transistor, 0k/100k, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23* SC?59*'}])
    newPart['name'].append('Transistor_BJT : DTC115G')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

