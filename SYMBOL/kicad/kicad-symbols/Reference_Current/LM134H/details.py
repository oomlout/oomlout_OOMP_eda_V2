
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Reference_Current"
    oIndex = "LM134H"
    hexID = "SZKREFERENCECURRENTLM134H"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM134H', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-46-3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm134.pdf', 'kicadSymbolki_keywords': 'Adjustable Current Source 10mA', 'kicadSymbolki_description': ' 1μA to 10mA 3-Terminal Adjustable Current Source, TO-46', 'kicadSymbolki_fp_filters': 'TO?46*'}])
    newPart['name'].append('Reference_Current : LM134H')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

