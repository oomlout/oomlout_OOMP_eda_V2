
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "ZED-F9P"
    hexID = "SZKGPSZEDF9P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ZED-F9P', 'kicadSymbolFootprint': 'RF_GPS:ublox_ZED', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/ZED-F9P_DataSheet_%28UBX-17051259%29.pdf', 'kicadSymbolki_keywords': 'u-blox GNSS multi-band RTK', 'kicadSymbolki_description': 'GNSS Module ZED F9, VCC 2.7V to 3.6V, LGA-54', 'kicadSymbolki_fp_filters': 'ublox*ZED*'}])
    newPart['name'].append('RF_GPS : ZED-F9P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

