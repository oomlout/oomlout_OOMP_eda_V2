
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "DAC101C081CIMK"
    hexID = "SZKANALOGDACDAC11C81CIMK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DAC081C081CIMK', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DAC101C081CIMK', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/dac101c081.pdf', 'kicadSymbolki_keywords': 'I2C DAC 10-bit', 'kicadSymbolki_description': '10-bit Micropower DAC with I2C-Compatible Interface, SOT-23-6', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Analog_DAC : DAC101C081CIMK')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

