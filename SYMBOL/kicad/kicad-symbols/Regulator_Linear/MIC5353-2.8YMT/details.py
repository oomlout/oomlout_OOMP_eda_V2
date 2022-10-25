
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "MIC5353-2.8YMT"
    hexID = "SZKREGULATORLINEARMIC535328YMT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MIC5353-2.5YMT', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MIC5353-2.8YMT', 'kicadSymbolFootprint': 'Package_DFN_QFN:MLF-6-1EP_1.6x1.6mm_P0.5mm_EP0.5x1.26mm', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/mic5353.pdf', 'kicadSymbolki_keywords': 'Single LDO', 'kicadSymbolki_description': 'High-performance, single-output,  ultra-low  LDO regulator', 'kicadSymbolki_fp_filters': 'MLF?6?1EP*1.6x1.6mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Linear : MIC5353-2.8YMT')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

