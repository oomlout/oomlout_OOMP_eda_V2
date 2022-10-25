
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Protection"
    oIndex = "TPD3E001DRLR"
    hexID = "SZKPOWERPROTECTIONTPD3E1DRLR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPD3E001DRLR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-553', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tpd3e001.pdf', 'kicadSymbolki_keywords': 'ESD-Protection', 'kicadSymbolki_description': 'TPD3E001 Low-Capacitance 3-Channel ESD-Protection for High-Speed Data Interfaces', 'kicadSymbolki_fp_filters': 'SOT?553*'}])
    newPart['name'].append('Power_Protection : TPD3E001DRLR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

