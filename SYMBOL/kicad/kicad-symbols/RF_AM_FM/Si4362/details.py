
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_AM_FM"
    oIndex = "Si4362"
    hexID = "SZKRFAMFMSI4362"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Si4362', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-20-1EP_4x4mm_P0.5mm_EP2.5x2.5mm', 'kicadSymbolDatasheet': 'http://www.silabs.com/Support%20Documents/TechnicalDocs/Si4362.pdf', 'kicadSymbolki_keywords': 'radio receiver', 'kicadSymbolki_description': 'EZRadioPRO Low Current Receiver', 'kicadSymbolki_fp_filters': 'QFN*4x4mm*P0.5mm*'}])
    newPart['name'].append('RF_AM_FM : Si4362')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

