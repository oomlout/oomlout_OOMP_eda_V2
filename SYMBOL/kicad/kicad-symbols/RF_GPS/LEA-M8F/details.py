
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "LEA-M8F"
    hexID = "SZKGPSLEAM8F"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LEA-M8F', 'kicadSymbolFootprint': 'RF_GPS:ublox_LEA', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/products/documents/LEA-M8F_DataSheet_%28UBX-14001772%29.pdf', 'kicadSymbolki_keywords': 'ublox GPS GNSS module', 'kicadSymbolki_description': 'GNSS Module LEA M8, VCC 3V to 3.6V', 'kicadSymbolki_fp_filters': 'ublox*LEA*'}])
    newPart['name'].append('RF_GPS : LEA-M8F')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

