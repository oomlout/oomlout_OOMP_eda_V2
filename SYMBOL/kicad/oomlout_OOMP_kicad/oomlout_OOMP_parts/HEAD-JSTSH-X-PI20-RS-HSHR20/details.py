
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-JSTSH-X-PI20-RS-HSHR20"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADJSTSHXPI2RSHSHR2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-JSTSH-X-PI20-RS-HSHR20', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-JSTSH-X-PI20-RS-HSHR20', 'kicadSymbolDatasheet': 'oom.lt/HSHR20', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: HSHR20;Generic connector, single row, 01x20, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??_*'}])
    newPart['name'].append('HEAD-JSTSH-X-PI20-RS-HSHR20')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

