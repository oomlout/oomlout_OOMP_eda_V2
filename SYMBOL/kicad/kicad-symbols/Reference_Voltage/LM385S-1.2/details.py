
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM385S-1.2"
    hexID = "SZKREFERENCEVOLTAGELM385S12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM285S-1.2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM385S-1.2', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/185fc.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference', 'kicadSymbolki_description': '1.235V Micropower Voltage Reference Diodes, SO-8', 'kicadSymbolki_fp_filters': 'SOIC?8*3.9x4.9m*P1.27mm*'}])
    newPart['name'].append('LM385S-1.2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

