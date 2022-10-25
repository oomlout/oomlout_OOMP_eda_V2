
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GSM"
    oIndex = "SARA-U260"
    hexID = "SZKGSMSARAU26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SARA-U201', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SARA-U260', 'kicadSymbolFootprint': 'RF_GSM:ublox_SARA-G3_LGA-96', 'kicadSymbolDatasheet': 'https://www.u-blox.com/sites/default/files/SARA-U2_DataSheet_(UBX-13005287).pdf', 'kicadSymbolki_keywords': 'GSM HSPA 2G 3G', 'kicadSymbolki_description': 'Ublox HSPA GSM Quad-Band Communication Module, AT Command Set, Designed for America, LGA-96', 'kicadSymbolki_fp_filters': 'ublox*SARA*'}])
    newPart['name'].append('RF_GSM : SARA-U260')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

