
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Valve"
    oIndex = "NOS-6418"
    hexID = "SZKVANOS6418"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'CK6418', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NOS-6418', 'kicadSymbolFootprint': 'Valve:Valve_Mini_Pentode_Linear', 'kicadSymbolDatasheet': 'https://frank.pocnet.net/sheets/127/6/6418.pdf', 'kicadSymbolki_keywords': 'subminiature pentode valve', 'kicadSymbolki_description': 'Subminiature Pentode', 'kicadSymbolki_fp_filters': 'VALVE*MINI*PENTODE*LINEAR*'}])
    newPart['name'].append('NOS-6418')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

