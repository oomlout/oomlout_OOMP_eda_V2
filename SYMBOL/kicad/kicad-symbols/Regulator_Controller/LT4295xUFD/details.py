
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Controller"
    oIndex = "LT4295xUFD"
    hexID = "SZKREGULATORCONTROLLERLT4295XUFD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT4295xUFD', 'kicadSymbolFootprint': 'Package_DFN_QFN:QFN-28-1EP_4x5mm_P0.5mm_EP2.65x3.65mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/LT4295.pdf', 'kicadSymbolki_keywords': 'LTPoE++ IEEE 802.3af IEEE 802.3at IEEE 802.3bt', 'kicadSymbolki_description': 'IEEE 802.3bt PD Interface with Forward/Flyback Controller, QFN-28', 'kicadSymbolki_fp_filters': 'QFN*1EP*4x5mm*P0.5mm*'}])
    newPart['name'].append('Regulator_Controller : LT4295xUFD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

