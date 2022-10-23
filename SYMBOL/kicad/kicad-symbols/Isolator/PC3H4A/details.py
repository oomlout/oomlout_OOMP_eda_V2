
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Isolator"
    oIndex = "PC3H4A"
    hexID = "SZKISOLATORPC3H4A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PC3H4', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PC3H4A', 'kicadSymbolFootprint': 'Package_DIP:SMDIP-4_W7.62mm', 'kicadSymbolDatasheet': 'http://www.sharpsma.com/webfm_send/395', 'kicadSymbolki_keywords': 'NPN AC DC Optocoupler', 'kicadSymbolki_description': 'AC/DC Optocoupler, Vce 70V, CTR 100-250%, SOP4', 'kicadSymbolki_fp_filters': 'SMDIP*W7.62mm*'}])
    newPart['name'].append('PC3H4A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

