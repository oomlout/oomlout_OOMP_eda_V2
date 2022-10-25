
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MAX5093AATE"
    hexID = "SZKREGULATORLINEARMAX593AATE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MAX5092AATE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX5093AATE', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-16-1EP_5x5mm_P0.8mm_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'http://datasheets.maximintegrated.com/en/ds/MAX5092-MAX5093.pdf', 'kicadSymbolki_keywords': 'High Voltage 72V Input LDO Boost Preregulator 250mA 3.3V', 'kicadSymbolki_description': '4V to 72V Input LDOs with Boost Preregulator, 250mA Output, 3.3V Preset Vout, TQFN-16', 'kicadSymbolki_fp_filters': 'QFN*5x5mm*P0.8mm*'}])
    newPart['name'].append('Regulator_Linear : MAX5093AATE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

