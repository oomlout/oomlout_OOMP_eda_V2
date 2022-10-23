
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "SANYOU_SRD_Form_B"
    hexID = "SZKRELAYSANYOUSRDFORMB"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'SANYOU_SRD_Form_B', 'kicadSymbolFootprint': 'Relay_THT:Relay_SPST_SANYOU_SRD_Series_Form_B', 'kicadSymbolDatasheet': 'http://www.sanyourelay.ca/public/products/pdf/SRD.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPST', 'kicadSymbolki_description': 'Sanyo SRD relay, Single Pole Miniature Power Relay, Opening Contact', 'kicadSymbolki_fp_filters': 'Relay*SPST*SANYOU*SRD*Series*Form*B*'}])
    newPart['name'].append('SANYOU_SRD_Form_B')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

