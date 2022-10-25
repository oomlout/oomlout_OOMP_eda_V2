
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "EM84"
    hexID = "SZKVAEM84"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'EM84', 'kicadSymbolFootprint': 'Valve:Valve_Noval_P', 'kicadSymbolDatasheet': 'http://www.r-type.org/pdfs/em84.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'indicator tube valve magic eye', 'kicadSymbolki_description': 'indicator tube "magic eye"', 'kicadSymbolki_fp_filters': 'VALVE*NOVAL*P*'}])
    newPart['name'].append('Valve : EM84')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

