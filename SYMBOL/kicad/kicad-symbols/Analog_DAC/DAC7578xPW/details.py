
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC7578xPW"
    hexID = "SZKANALOGDACDAC7578XPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DAC5578xPW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC7578xPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-16_4.4x5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/dac5578.pdf', 'kicadSymbolki_keywords': 'DAC I2C TWI 8-channel', 'kicadSymbolki_description': '12-Bit, Octal-Channel, Ultra-Low Glitch, Voltage Output, Two-Wire Interface Digital-to-Analog Converters, TSSOP-16', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x5mm*P0.65mm*'}])
    newPart['name'].append('Analog_DAC : DAC7578xPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

