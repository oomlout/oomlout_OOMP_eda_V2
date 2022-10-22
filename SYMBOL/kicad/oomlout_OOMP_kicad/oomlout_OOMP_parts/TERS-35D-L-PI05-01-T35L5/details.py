
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "oomlout_OOMP_kicad"
    oDesc = "oomlout_OOMP_parts"
    oIndex = "TERS-35D-L-PI05-01-T35L5"
    hexID = "SZKICADOOMLOUTOOMPKICADOOMLOUTOOMPPARTSTERS35DLPI51T35L5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'J', 'kicadSymbolValue': 'TERS-35D-L-PI05-01-T35L5', 'kicadSymbolFootprint': 'oomlout_OOMP_parts:TERS-35D-L-PI05-01-T35L5', 'kicadSymbolDatasheet': 'oom.lt/T35L5', 'kicadSymbolki_keywords': 'screw terminal', 'kicadSymbolki_description': 'hexID: T35L5;Generic screw terminal, single row, 01x05, script generated (kicad-library-utils/schlib/autogen/connector/)', 'kicadSymbolki_fp_filters': 'TerminalBlock*:*'}])
    newPart['name'].append('TERS-35D-L-PI05-01-T35L5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

