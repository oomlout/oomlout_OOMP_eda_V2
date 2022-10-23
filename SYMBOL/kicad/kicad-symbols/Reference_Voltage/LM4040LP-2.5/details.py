
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Voltage"
    oIndex = "LM4040LP-2.5"
    hexID = "SZKREFERENCEVOLTAGELM44LP25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM4040LP-2.0', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM4040LP-2.5', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm4040-n.pdf', 'kicadSymbolki_keywords': 'diode device voltage reference shunt', 'kicadSymbolki_description': '2.500V Precision Micropower Shunt Voltage Reference, TO-92', 'kicadSymbolki_fp_filters': 'TO?92*Inline*'}])
    newPart['name'].append('LM4040LP-2.5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

