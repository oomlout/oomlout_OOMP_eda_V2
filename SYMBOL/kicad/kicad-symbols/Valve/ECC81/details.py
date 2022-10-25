
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "ECC81"
    hexID = "SZKVAECC81"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ECC81', 'kicadSymbolFootprint': 'Valve:Valve_Noval_P', 'kicadSymbolDatasheet': 'http://www.r-type.org/pdfs/ecc81.pdf', 'kicadSymbolki_locked': '', 'kicadSymbolki_keywords': 'triode valve', 'kicadSymbolki_description': 'double triode', 'kicadSymbolki_fp_filters': 'VALVE*NOVAL*P*'}])
    newPart['name'].append('Valve : ECC81')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

