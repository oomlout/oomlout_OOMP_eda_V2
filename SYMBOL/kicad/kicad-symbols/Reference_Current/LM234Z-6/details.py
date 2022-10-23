
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Current"
    oIndex = "LM234Z-6"
    hexID = "SZKREFERENCECURRENTLM234Z6"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM334Z', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM234Z-6', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-92_Inline', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm134.pdf', 'kicadSymbolki_keywords': 'Adjustable Current Source 10mA', 'kicadSymbolki_description': '1μA to 10mA 3-Terminal Adjustable Current Source, TO-92', 'kicadSymbolki_fp_filters': 'TO*92*Inline*'}])
    newPart['name'].append('LM234Z-6')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

