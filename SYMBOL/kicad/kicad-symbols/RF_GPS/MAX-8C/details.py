
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "MAX-8C"
    hexID = "SZKGPSMAX8C"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX-8C', 'kicadSymbolFootprint': 'RF_GPS:ublox_MAX', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/MAX-8_DataSheet_%28UBX-16000093%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module MAX M8, VCC 1.65V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*MAX*'}])
    newPart['name'].append('RF_GPS : MAX-8C')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

