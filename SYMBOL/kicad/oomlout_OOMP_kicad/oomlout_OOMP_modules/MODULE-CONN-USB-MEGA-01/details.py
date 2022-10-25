
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-USB-MEGA-01"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNUMEGA1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MODULE-CONN-USB-MEGA-01', 'kicadSymbolFootprint': 'oomlout_OOMP_modules:MODULE-CONN-USB-MEGA-01', 'kicadSymbolDatasheet': 'oom.lt/MCUMEGA'}])
    newPart['name'].append('oomlout_OOMP_modules : MODULE-CONN-USB-MEGA-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

