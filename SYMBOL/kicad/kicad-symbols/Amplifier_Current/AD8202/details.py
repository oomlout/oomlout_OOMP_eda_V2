
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "AD8202"
    hexID = "SZKAMPLIFIERCURRENTAD822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8202', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8202.pdf', 'kicadSymbolki_keywords': 'highside HS current sense amplifier linear buffered monitor preamp', 'kicadSymbolki_description': '28V High Common-Mode Voltage, Single-Supply Difference Amplifier, 10V/V x 2V/V adjustable gain, bandwidth 50kHz, Vcc=3.5V~12V, unidirectional, SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* MSOP*P0.65mm*'}])
    newPart['name'].append('Amplifier_Current : AD8202')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

