
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "AD8206"
    hexID = "SZKAMPLIFIERCURRENTAD826"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8210', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8206', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8206.pdf', 'kicadSymbolki_keywords': 'highside HS current sense amplifier linear buffered', 'kicadSymbolki_description': '65V High Common-Mode Voltage, Bidirectional, Current Shunt Amplifier, 20V/V gain, bandwidth 100kHz, Vcc=5V, SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Current : AD8206')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

