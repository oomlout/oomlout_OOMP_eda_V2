
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD8F003"
    hexID = "SZKPOWERPROTECTIONTPD8F3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD8F003', 'kicadSymbolFootprint': 'Package_SON:WSON-16_3.3x1.35_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd6f003.pdf', 'kicadSymbolki_keywords': 'EMI, ESD protection', 'kicadSymbolki_description': '8 channel EMI filters with integrated ESD protection', 'kicadSymbolki_fp_filters': 'WSON*3.3x1.35*P0.4mm*'}])
    newPart['name'].append('Power_Protection : TPD8F003')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

