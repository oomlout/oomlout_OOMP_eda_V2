
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "DTC143E"
    hexID = "SZKTRANSISTORBJTDTC143E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'DTC143E', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'ROHM Digital NPN Transistor', 'kicadSymbolki_description': 'Digital NPN Transistor, 4k7/4k7, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23* SC?59*'}])
    newPart['name'].append('Transistor_BJT : DTC143E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

