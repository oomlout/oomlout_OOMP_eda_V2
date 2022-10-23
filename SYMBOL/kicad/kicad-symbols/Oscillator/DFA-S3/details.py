
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Oscillator"
    oIndex = "DFA-S3"
    hexID = "SZKOCSDFAS3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'X', 'kicadSymbolValue': 'DFA-S3', 'kicadSymbolFootprint': 'Oscillator:Oscillator_SMD_Fordahl_DFAS3-4Pin_9.1x7.2mm', 'kicadSymbolDatasheet': 'http://www.metatech.com.hk/product/fordahl/pdf/2002%20TCXO%20Page%2043-58.pdf', 'kicadSymbolki_keywords': 'Temperature compensated Crystal Clock Oscillator', 'kicadSymbolki_description': 'Temperature compensated Crystal Clock Oscillator', 'kicadSymbolki_fp_filters': 'Oscillator*SMD*Fordahl*DFAS3*9.1x7.2mm*'}])
    newPart['name'].append('DFA-S3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

