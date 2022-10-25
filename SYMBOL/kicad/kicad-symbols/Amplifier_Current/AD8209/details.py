
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "AD8209"
    hexID = "SZKAMPLIFIERCURRENTAD829"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8203', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8209', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8209.pdf', 'kicadSymbolki_keywords': 'highside HS current sense amplifier linear buffered monitor preamp', 'kicadSymbolki_description': '45V High Voltage, Precision Difference Amplifier, 7V/V x 2V/V adjustable gain, bandwidth 80kHz, Vcc=5V, unidirectional, MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* MSOP*P0.65mm*'}])
    newPart['name'].append('Amplifier_Current : AD8209')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

