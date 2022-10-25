
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD6F003"
    hexID = "SZKPOWERPROTECTIONTPD6F3"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD6F003', 'kicadSymbolFootprint': 'Package_SON:Texas_R-PWSON-N12_EP0.4x2mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd6f003.pdf', 'kicadSymbolki_keywords': 'EMI, ESD protection', 'kicadSymbolki_description': '6 channel EMI filters with integrated ESD protection', 'kicadSymbolki_fp_filters': '*WSON*EP0.4x2mm*'}])
    newPart['name'].append('Power_Protection : TPD6F003')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

