
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "AD8208"
    hexID = "SZKAMPLIFIERCURRENTAD828"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'AD8202', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8208', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8208.pdf', 'kicadSymbolki_keywords': 'highside HS current sense amplifier linear buffered monitor preamp', 'kicadSymbolki_description': '45V High Voltage, Precision Difference Amplifier, 10V/V x 2V/V adjustable gain, bandwidth 70kHz, Vcc=5V, unidirectional, SOIC-8/MSOP-8', 'kicadSymbolki_fp_filters': 'SOIC*P1.27mm* MSOP*P0.65mm*'}])
    newPart['name'].append('AD8208')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

