
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_LineDriver"
    oIndex = "MC3486N"
    hexID = "SZKINTERFACELINEDRIVERMC3486N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC3486N', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/mc3486.pdf', 'kicadSymbolki_keywords': 'Quadruple differential line receiver', 'kicadSymbolki_description': 'Quadruple differential line receiver, SOIC-16', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Interface_LineDriver : MC3486N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

