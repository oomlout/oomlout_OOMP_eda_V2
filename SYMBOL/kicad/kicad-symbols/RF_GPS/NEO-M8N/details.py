
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "NEO-M8N"
    hexID = "SZKGPSNEOM8N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NEO-M8N', 'kicadSymbolFootprint': 'RF_GPS:ublox_NEO', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/NEO-M8-FW3_DataSheet_%28UBX-15031086%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module NEO M8, VCC 2.7V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*NEO*'}])
    newPart['name'].append('RF_GPS : NEO-M8N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

