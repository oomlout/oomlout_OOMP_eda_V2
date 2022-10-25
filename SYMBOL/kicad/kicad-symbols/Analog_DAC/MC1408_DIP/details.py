
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Analog_DAC"
    oIndex = "MC1408_DIP"
    hexID = "SZKANALOGDACMC148DIP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MC1408_DIP', 'kicadSymbolFootprint': 'Package_DIP:DIP-16_W7.62mm', 'kicadSymbolDatasheet': 'http://www.pinballpcb.com/datasheets/OnMC1408-dac.pdf', 'kicadSymbolki_keywords': '8 bit multiplying DAC', 'kicadSymbolki_description': '8-bit multiplying DAC', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Analog_DAC : MC1408_DIP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

