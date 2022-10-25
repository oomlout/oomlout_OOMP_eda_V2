
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Difference"
    oIndex = "AD8207"
    hexID = "SZKAMPLIFIERDIFFERENCEAD827"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8207', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8207.pdf', 'kicadSymbolki_keywords': 'highside HS current sense difference amplifier linear buffered', 'kicadSymbolki_description': '65V (35V) Zero-Drift, High Voltage, Bidirectional, Difference Amplifier, 20V/V gain, bandwidth 150kHz, Vcc=5V (3.3V), SOIC-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Amplifier_Difference : AD8207')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

