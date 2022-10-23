
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "FODM3052"
    hexID = "SZKRFFODM352"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FODM3011', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FODM3052', 'kicadSymbolFootprint': 'Package_DIP:SMDIP-4_W7.62mm', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FODM3053_NF098-D.PDF', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Random Phase Mini-Flat', 'kicadSymbolki_description': 'Full Pitch Mini-Flat Random Phase Opto-Triac, Vdrm 600V, Ift 10mA, MFP 4L', 'kicadSymbolki_fp_filters': 'SMDIP*W7.62mm*'}])
    newPart['name'].append('FODM3052')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

