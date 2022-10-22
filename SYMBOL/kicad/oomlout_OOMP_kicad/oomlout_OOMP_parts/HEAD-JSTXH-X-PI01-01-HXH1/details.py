
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-JSTXH-X-PI01-01-HXH1"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADJSTXHXPI11HXH1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-JSTXH-X-PI01-01-HXH1', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-JSTXH-X-PI01-01-HXH1', 'kicadSymbolDatasheet': 'oom.lt/HXH1', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: HXH1;Generic connector, single row, 01x01, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*'}])
    newPart['name'].append('HEAD-JSTXH-X-PI01-01-HXH1')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

