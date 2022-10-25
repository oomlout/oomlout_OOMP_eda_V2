
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "MOSN-T252-X-K4184-01-MN2524184A"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSMOSNT252XK41841MN2524184A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'MOSN-T252-X-K4184-01-MN2524184A', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:MOSN-T252-X-K4184-01-MN2524184A', 'kicadSymbolDatasheet': 'oom.lt/MN2524184A', 'kicadSymbolki_keywords': 'transistor NMOS N-MOS N-MOSFET', 'kicadSymbolki_description': 'hexID: MN2524184A;N-MOSFET transistor, gate/drain/source'}])
    newPart['name'].append('oomlout_OOMP_parts : MOSN-T252-X-K4184-01-MN2524184A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

