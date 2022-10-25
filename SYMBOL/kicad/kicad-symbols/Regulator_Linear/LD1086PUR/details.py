
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "LD1086PUR"
    hexID = "SZKREGULATORLINEARLD186PUR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LD1086PUR', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-8-1EP_4x4mm_P0.8mm_EP2.3x3.24mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/ld1086.pdf', 'kicadSymbolki_keywords': 'Linear Regulator 1.5A Adjustable', 'kicadSymbolki_description': 'Positive, 1.5A 30V, Linear Regulator, Adjustable, DFN8', 'kicadSymbolki_fp_filters': 'DFN*1EP*4x4mm*P0.8mm*'}])
    newPart['name'].append('Regulator_Linear : LD1086PUR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

