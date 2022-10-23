
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LM1085-ADJ"
    hexID = "SZKREGULATORLINEARLM185ADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM1084-ADJ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM1085-ADJ', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm1085.pdf', 'kicadSymbolki_keywords': 'Adjustable Voltage Regulator 5A Positive', 'kicadSymbolki_description': '3A 29V Adjustable Linear Regulator, TO-220 / TO-263 (D2-PAK)', 'kicadSymbolki_fp_filters': 'TO?220* TO?263*'}])
    newPart['name'].append('LM1085-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

