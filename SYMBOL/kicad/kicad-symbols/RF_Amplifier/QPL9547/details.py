
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Amplifier"
    oIndex = "QPL9547"
    hexID = "SZKRFAMPLIFIERQPL9547"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'QPL9547', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_2x2mm_P0.5mm_EP0.8x1.6mm', 'kicadSymbolDatasheet': 'https://www.qorvo.com/products/d/da007268', 'kicadSymbolki_keywords': 'RF GAIN BLOCK', 'kicadSymbolki_description': '100-6000MHz RF/IF +19.5dB gain block, DFN-8', 'kicadSymbolki_fp_filters': 'DFN*1EP*2x2mm*P0.5mm*'}])
    newPart['name'].append('RF_Amplifier : QPL9547')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

