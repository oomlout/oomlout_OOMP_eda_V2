
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator_Analog"
    oIndex = "IL300"
    hexID = "SZKISOLATORANALOGIL3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IL300', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.vishay.com/docs/83622/il300.pdf', 'kicadSymbolki_keywords': 'Isolated Linear Photocoupler', 'kicadSymbolki_description': 'Isolated Linear Photocoupler, High Gain, Wideband, DIP8/SMD-DIP8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm* DIP*W10.16mm* SMDIP*W7.62mm* SMDIP*W9.53mm* SMDIP*W11.48mm*'}])
    newPart['name'].append('IL300')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

