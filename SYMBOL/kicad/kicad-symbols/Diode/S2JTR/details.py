
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "S2JTR"
    hexID = "SZKDIODES2JTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'S2JTR', 'kicadSymbolFootprint': 'Diode_SMD:D_SMB', 'kicadSymbolDatasheet': 'http://www.smc-diodes.com/propdf/S2A-S2M%20N0562%20REV.A.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '600V 2A General Purpose Rectifier Diode, SMB', 'kicadSymbolki_fp_filters': '*D?SMB*'}])
    newPart['name'].append('Diode : S2JTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

