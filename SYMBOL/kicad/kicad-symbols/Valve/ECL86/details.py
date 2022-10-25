
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "ECL86"
    hexID = "SZKVAECL86"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ECL86', 'kicadSymbolFootprint': 'Valve:Valve_Noval_P', 'kicadSymbolDatasheet': 'http://www.r-type.org/pdfs/ecl86.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'triode pentode valve', 'kicadSymbolki_description': 'triode pentode', 'kicadSymbolki_fp_filters': 'Valve*Noval*P*'}])
    newPart['name'].append('Valve : ECL86')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

