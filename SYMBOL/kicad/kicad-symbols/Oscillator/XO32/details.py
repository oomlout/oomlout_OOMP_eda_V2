
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "XO32"
    hexID = "SZKOCSXO32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'XO32', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_EuroQuartz_XO32-4Pin_3.2x2.5mm', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/B400/XO32.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'HCMOS Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*EuroQuartz*XO32*3.2x2.5mm*'}])
    newPart['name'].append('XO32')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

