
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC8565"
    hexID = "SZKANALOGDACDAC8565"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DAC8165', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC8565', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/dac8565.pdf', 'kicadSymbolki_keywords': '16-bit quad DAC voltage reference', 'kicadSymbolki_description': '16-bit quad-channel voltage output DAC with 2.5V internal reference', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : DAC8565')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

