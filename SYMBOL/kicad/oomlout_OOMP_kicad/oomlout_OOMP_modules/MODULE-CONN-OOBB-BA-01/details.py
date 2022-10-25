
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-OOBB-BA-01"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNOOBBBA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'MODULE-CONN-OOBB-BA-01', 'kicadSymbolFootprint': 'oomlout_OOMP_modules:MODULE-CONN-OOBB-BA-01', 'kicadSymbolDatasheet': 'oom.lt/MCOBA'}])
    newPart['name'].append('oomlout_OOMP_modules : MODULE-CONN-OOBB-BA-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

