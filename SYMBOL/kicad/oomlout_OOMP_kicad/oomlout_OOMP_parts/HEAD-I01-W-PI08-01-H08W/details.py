
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "HEAD-I01-W-PI08-01-H08W"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSHEADI1WPI81H8W"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'HEAD-I01-W-PI08-01-H08W', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:HEAD-I01-W-PI08-01-H08W', 'kicadSymbolDatasheet': 'oom.lt/H08W', 'kicadSymbolki_keywords': 'connector', 'kicadSymbolki_description': 'hexID: H08W;Generic connector, single row, 01x08, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'Connector*:*_1x??_*'}])
    newPart['name'].append('HEAD-I01-W-PI08-01-H08W')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

