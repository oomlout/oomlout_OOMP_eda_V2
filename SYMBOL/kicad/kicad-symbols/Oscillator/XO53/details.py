
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "XO53"
    hexID = "SZKOCSXO53"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'XO53', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_EuroQuartz_XO53-4Pin_5.0x3.2mm', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/B400/XO53.pdf', 'kicadSymbolki_keywords': 'Crystal Clock Oscillator', 'kicadSymbolki_description': 'Low Power Consumption Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*EuroQuartz*XO53*5.0x3.2mm*'}])
    newPart['name'].append('XO53')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

