
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Current"
    oIndex = "AD8218xCP"
    hexID = "SZKAMPLIFIERCURRENTAD8218XCP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AD8218xCP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-8-1EP_3x2mm_P0.5mm_EP1.6x1.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/AD8218.pdf', 'kicadSymbolki_keywords': 'highside HS current sense amplifier linear buffered', 'kicadSymbolki_description': '80V Zero Drift, Bidirectional, Current Shunt Monitor, 20V/V gain, bandwidth 450kHz, Vcc=5V, LFCSP-8', 'kicadSymbolki_fp_filters': 'LFCSP*3x2mm*P0.5mm*EP1.6x1.65mm*'}])
    newPart['name'].append('Amplifier_Current : AD8218xCP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

