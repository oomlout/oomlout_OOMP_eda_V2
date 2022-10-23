
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF"
    oIndex = "MOC3063M"
    hexID = "SZKRFMOC363M"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MOC3031M', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MOC3063M', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/MOC3163M-D.pdf', 'kicadSymbolki_keywords': 'Opto-Triac Opto Triac Zero Cross', 'kicadSymbolki_description': 'Zero Cross Opto-Triac, Vdrm 600V, Ift 5mA, DIP6', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* SMDIP*W9.53mm* DIP*W10.16mm*'}])
    newPart['name'].append('MOC3063M')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

