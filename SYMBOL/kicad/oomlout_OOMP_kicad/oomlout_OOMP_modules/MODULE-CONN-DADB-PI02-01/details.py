
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_modules"
    oIndex = "MODULE-CONN-DADB-PI02-01"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPMOSMOCONNDADBPI21"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MODULE-CONN-DADB-PI02-01', 'kicadSymbolFootprint': 'oomlout_OOMP_modules:MODULE-CONN-DADB-PI02-01', 'kicadSymbolDatasheet': 'oom.lt/MCD2'}])
    newPart['name'].append('oomlout_OOMP_modules : MODULE-CONN-DADB-PI02-01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

