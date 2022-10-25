
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "Rohm_UMP11N"
    hexID = "SZKDIODEROHMUMP11N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'Rohm_UMP11N', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/discrete/diode/switching/ump11n.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': ' High-speed switching diodes 2 pair Com A', 'kicadSymbolki_fp_filters': 'SOT?363*'}])
    newPart['name'].append('Diode : Rohm_UMP11N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

