
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "MAX2679"
    hexID = "SZKRFAMPLIFIERMAX2679"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX2679', 'kicadSymbolFootprint': 'Package_BGA:WLP-4_0.83x0.83mm_P0.4mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX2679-MAX2679B.pdf', 'kicadSymbolki_keywords': 'RF GAIN BLOCK', 'kicadSymbolki_description': 'GPS/GNSS Ultra-Low Current Low-Noise Amplifier, +19dB @ 1.57GHz, WLP-4', 'kicadSymbolki_fp_filters': 'WLP*0.83x0.83mm*P0.4mm*'}])
    newPart['name'].append('RF_Amplifier : MAX2679')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

