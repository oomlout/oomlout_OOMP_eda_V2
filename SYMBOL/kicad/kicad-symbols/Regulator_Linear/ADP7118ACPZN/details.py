
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "ADP7118ACPZN"
    hexID = "SZKREGULATORLINEARADP7118ACPZN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP7118ACPZN', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-6-1EP_2x2mm_P0.65mm_EP1x1.6mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP7142.pdf', 'kicadSymbolki_keywords': 'linear regulator ldo adjustable positive', 'kicadSymbolki_description': '200mA, Low Noise, CMOS Low Dropout Regulator, Positive, Adjustable, LFCSP-6', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*2x2mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : ADP7118ACPZN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

