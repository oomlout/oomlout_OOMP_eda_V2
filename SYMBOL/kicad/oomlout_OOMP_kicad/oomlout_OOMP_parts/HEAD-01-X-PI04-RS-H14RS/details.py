
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-01-X-PI04-RS-H14RS"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEAD1XPI4RSH14RS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-01-X-PI04-RS-H14RS', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-01-X-PI04-RS-H14RS', 'kicadSymbolDatasheet': 'oom.lt/H14RS', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H14RS;Generic connector, single row, 01x04, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??_*'}])
    newPart['name'].append('HEAD-01-X-PI04-RS-H14RS')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

