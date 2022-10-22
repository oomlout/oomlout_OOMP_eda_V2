
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-JSTXH-X-PI09-01-HXH9"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADJSTXHXPI91HXH9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-JSTXH-X-PI09-01-HXH9', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-JSTXH-X-PI09-01-HXH9', 'kicadSymbolDatasheet': 'oom.lt/HXH9', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: HXH9;Generic connector, single row, 01x09, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??_*'}])
    newPart['name'].append('HEAD-JSTXH-X-PI09-01-HXH9')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

