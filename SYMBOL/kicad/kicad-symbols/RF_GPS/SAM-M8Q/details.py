
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "SAM-M8Q"
    hexID = "SZKGPSSAMM8Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SAM-M8Q', 'kicadSymbolFootprint': 'RF_GPS:ublox_SAM-M8Q', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/SAM-M8Q_DataSheet_%28UBX-16012619%29.pdf', 'kicadSymbolki_keywords': 'gps module with antenna', 'kicadSymbolki_description': 'GPS ublox M8 variant', 'kicadSymbolki_fp_filters': 'ublox*SAM?M8Q*'}])
    newPart['name'].append('SAM-M8Q')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

