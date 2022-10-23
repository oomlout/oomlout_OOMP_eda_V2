
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "DFA-S11"
    hexID = "SZKOCSDFAS11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'DFA-S11', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Fordahl_DFAS11-4Pin_7.0x5.0mm', 'kicadSymbolDatasheet': 'http://www.metatech.com.hk/product/fordahl/pdf/2002%20TCXO%20Page%2043-58.pdf', 'kicadSymbolki_keywords': 'Temperature compensated Crystal Clock Oscillator', 'kicadSymbolki_description': 'Temperature compensated Crystal Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Fordahl*DFAS11*7.0x5.0mm*'}])
    newPart['name'].append('DFA-S11')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

