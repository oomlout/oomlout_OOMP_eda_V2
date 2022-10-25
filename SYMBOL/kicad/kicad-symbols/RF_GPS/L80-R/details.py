
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_GPS"
    oIndex = "L80-R"
    hexID = "SZKGPSL8R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L80-R', 'kicadSymbolFootprint': 'RF_GPS:Quectel_L80-R', 'kicadSymbolDatasheet': 'https://www.quectel.com/UploadImage/Downlad/Quectel_L80-R_Hardware_Design_V1.2.pdf', 'kicadSymbolki_keywords': 'quectel GPS GNSS module', 'kicadSymbolki_description': 'Quectel GPS Module', 'kicadSymbolki_fp_filters': 'Quectel*L80*R*'}])
    newPart['name'].append('RF_GPS : L80-R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

