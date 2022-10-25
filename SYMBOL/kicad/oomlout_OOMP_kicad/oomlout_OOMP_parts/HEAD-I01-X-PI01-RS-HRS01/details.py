
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-X-PI01-RS-HRS01"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1XPI1RSHRS1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-X-PI01-RS-HRS01', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-X-PI01-RS-HRS01', 'kicadSymbolDatasheet': 'oom.lt/HRS01', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: HRS01;Generic connector, single row, 01x01, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*'}])
    newPart['name'].append('oomlout_OOMP_parts : HEAD-I01-X-PI01-RS-HRS01')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

