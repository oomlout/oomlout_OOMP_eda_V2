
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC1220E"
    hexID = "SZKANALOGDACDAC122E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC1220E', 'kicadSymbolFootprint': 'Package_SO:SSOP-16_3.9x4.9mm_P0.635mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/dac1220.pdf', 'kicadSymbolki_keywords': 'DAC', 'kicadSymbolki_description': '20-Bit , Low-Power Digital-to-Analog Converter, SSOP-16', 'kicadSymbolki_fp_filters': 'SSOP*3.9x4.9mm*P0.635mm*'}])
    newPart['name'].append('Analog_DAC : DAC1220E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

