
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "DFA-S2"
    hexID = "SZKOCSDFAS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'DFA-S2', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Fordahl_DFAS2-4Pin_7.3x5.1mm', 'kicadSymbolDatasheet': 'http://www.metatech.com.hk/product/fordahl/pdf/2002%20TCXO%20Page%2043-58.pdf', 'kicadSymbolki_keywords': 'Temperature compensated Crystal Clock Oscillator', 'kicadSymbolki_description': 'Temperature compensated Crystal Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Fordahl*DFAS2*7.3x5.1mm*'}])
    newPart['name'].append('DFA-S2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

