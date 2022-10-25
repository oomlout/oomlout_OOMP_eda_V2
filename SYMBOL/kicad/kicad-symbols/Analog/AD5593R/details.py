
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog"
    oIndex = "AD5593R"
    hexID = "SZKANALOGAD5593R"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD5593R', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD5593R.pdf', 'kicadSymbolki_keywords': '8channel 12bit ADC DAC GPIO I2C Temperature', 'kicadSymbolki_description': '8-channel 12bits configurable ADC/DAC/GPIO Internal Reference, I2C interface Integrated temperature sensor,Single Supply, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP-16*'}])
    newPart['name'].append('Analog : AD5593R')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

