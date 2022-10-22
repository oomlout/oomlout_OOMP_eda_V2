
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Panasonic_MA5J002E"
    hexID = "SZKDIODEPMA5J2E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'Rohm_UMN1N', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Panasonic_MA5J002E', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'http://www.semicon.panasonic.co.jp/ds4/MA5J002E_BED_discon.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': 'Quad Ultra high Speed Switching Diode Array Com K', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Panasonic_MA5J002E')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

