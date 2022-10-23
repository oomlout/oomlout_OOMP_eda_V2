
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "XO91"
    hexID = "SZKOCSXO91"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'XO91', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_EuroQuartz_XO91-4Pin_7.0x5.0mm', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/B400/XO91.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'HCMOS Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*EuroQuartz*XO91*7.0x5.0mm*'}])
    newPart['name'].append('XO91')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

