
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD3S044"
    hexID = "SZKPOWERPROTECTIONTPD3S44"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPD3S014', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD3S044', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd3s014.pdf', 'kicadSymbolki_keywords': 'ESD-Protection', 'kicadSymbolki_description': 'Current Limit Switch and D+/D– ESD Protection for USB Host Port, 1.5A, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Power_Protection : TPD3S044')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

