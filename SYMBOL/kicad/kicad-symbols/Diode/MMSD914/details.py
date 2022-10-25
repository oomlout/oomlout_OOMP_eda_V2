
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "MMSD914"
    hexID = "SZKDIODESD914"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MMSD914', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-123', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MMSD914T1-D.PDF', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '100V 0.2A Switching Diode, SOD-123', 'kicadSymbolki_fp_filters': 'D*SOD?123*'}])
    newPart['name'].append('Diode : MMSD914')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

