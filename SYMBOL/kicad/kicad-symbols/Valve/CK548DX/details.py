
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "CK548DX"
    hexID = "SZKVACK548DX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CK6418', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CK548DX', 'kicadSymbolFootprint': 'Valve:Valve_Mini_Pentode_Linear', 'kicadSymbolDatasheet': '', 'kicadSymbolki_keywords': 'subminiature pentode valve', 'kicadSymbolki_description': 'Subminiature Pentode', 'kicadSymbolki_fp_filters': 'VALVE*MINI*PENTODE*LINEAR*'}])
    newPart['name'].append('CK548DX')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

