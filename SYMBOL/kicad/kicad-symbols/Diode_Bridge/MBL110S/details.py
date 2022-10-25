
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "MBL110S"
    hexID = "SZKDIODEBRIDGEMBL11S"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MBL104S', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'MBL110S', 'kicadSymbolFootprint': 'Diode_SMD:Diode_Bridge_Vishay_MBLS', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/89959/mbl104s.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Miniature Glass Passivated Single-Phase Surface Mount Bridge Rectifiers, 700V Vrms, 1.0A If, MBLS SMD package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Vishay*MBLS*'}])
    newPart['name'].append('Diode_Bridge : MBL110S')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

