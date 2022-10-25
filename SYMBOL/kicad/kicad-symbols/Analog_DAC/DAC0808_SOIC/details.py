
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC0808_SOIC"
    hexID = "SZKANALOGDACDAC88SOIC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MC1408_SOIC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC0808_SOIC', 'kicadSymbolFootprint': 'Package_SO:SOIC-16_3.9x9.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/dac0808.pdf', 'kicadSymbolki_keywords': '8 bit multiplying DAC', 'kicadSymbolki_description': '8-bit multiplying DAC', 'kicadSymbolki_fp_filters': 'SOIC*3.9x9.9mm*P1.27mm*'}])
    newPart['name'].append('Analog_DAC : DAC0808_SOIC')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

