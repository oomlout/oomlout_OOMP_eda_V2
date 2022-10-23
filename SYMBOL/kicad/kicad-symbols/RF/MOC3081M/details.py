
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "MOC3081M"
    hexID = "SZKRFMOC381M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MOC3031M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MOC3081M', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MOC3083M-D.PDF', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Zero Cross', 'kicadSymbolki_description': 'Zero Cross Opto-Triac, Vdrm 800V, Ift 15mA, DIP6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SMDIP*W9.53mm* DIP*W10.16mm*'}])
    newPart['name'].append('MOC3081M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

