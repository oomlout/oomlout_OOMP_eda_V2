
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "MAX-8Q"
    hexID = "SZKGPSMAX8Q"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX-8C', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX-8Q', 'kicadSymbolFootprint': 'RF_GPS:ublox_MAX', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/MAX-8_DataSheet_%28UBX-16000093%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module M8, VCC 2.7V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*MAX*'}])
    newPart['name'].append('MAX-8Q')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

