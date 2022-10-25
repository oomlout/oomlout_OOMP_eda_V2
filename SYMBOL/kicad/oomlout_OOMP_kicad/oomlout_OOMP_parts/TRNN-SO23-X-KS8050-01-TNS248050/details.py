
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "TRNN-SO23-X-KS8050-01-TNS248050"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSTRNNSO23XKS851TNS2485"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'TRNN-SO23-X-KS8050-01-TNS248050', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:TRNN-SO23-X-KS8050-01-TNS248050', 'kicadSymbolDatasheet': 'oom.lt/TNS248050', 'kicadSymbolki_keywords': 'transistor NPN', 'kicadSymbolki_description': 'hexID: TNS248050;NPN transistor, base/emitter/collector'}])
    newPart['name'].append('oomlout_OOMP_parts : TRNN-SO23-X-KS8050-01-TNS248050')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

