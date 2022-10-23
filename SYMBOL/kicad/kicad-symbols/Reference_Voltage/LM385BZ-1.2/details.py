
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM385BZ-1.2"
    hexID = "SZKREFERENCEVOLTAGELM385BZ12"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM285Z-2.5', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM385BZ-1.2', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub_link/Collateral/LM285-D.PDF', 'kicadSymbolki_keywords': 'diode device voltage reference', 'kicadSymbolki_description': '1.235V Micropower Voltage Reference Diodes, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*Inline*'}])
    newPart['name'].append('LM385BZ-1.2')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

