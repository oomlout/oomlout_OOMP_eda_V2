
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3514xUFD"
    hexID = "SZKREGULATORSWITCHINGLT3514XUFD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3514xUFD', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x5mm_P0.5mm_EP2.65x3.65mm_ThermalVias', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3514fa.pdf', 'kicadSymbolki_keywords': 'triple step-down', 'kicadSymbolki_description': 'Triple Step-Down Switching Regulator with 100% Duty Cycle Operation, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*4x5mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Switching : LT3514xUFD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

