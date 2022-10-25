
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "1N914WT"
    hexID = "SZKDIODE1N914WT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': '1N914WT', 'kicadSymbolFootprint': 'Diode_SMD:D_SOD-523', 'kicadSymbolDatasheet': 'http://www.mouser.com/ds/2/149/1N4148WT-461550.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '75V 0.15A Fast switching Diode, SOD-523', 'kicadSymbolki_fp_filters': 'D*SOD?523*'}])
    newPart['name'].append('Diode : 1N914WT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

