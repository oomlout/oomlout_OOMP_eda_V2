
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "AD8418"
    hexID = "SZKAMPLIFIERCURRENTAD8418"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8417', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8418', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8418.pdf', 'kicadSymbolki_keywords': 'highside HS current sense amplifier linear', 'kicadSymbolki_description': '70V Bidirectional, Zero Drift, Current Sense Amplifier, 20V/V gain, bandwidth 250kHz, VS=2.7V~5.5V, SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*3.9x4.9mm*P1.27mm* MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Current : AD8418')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

