
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "AN34092B"
    hexID = "SZKDRIVERFETAN3492B"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'AN34092B', 'kicadSymbolFootprint': 'Package_DFN_QFN:Panasonic_HQFN-16-1EP_4x4mm_P0.65mm_EP2.9x2.9mm', 'kicadSymbolDatasheet': 'https://industrial.panasonic.com/content/data/SC/ds/ds4/AN34092B_E.pdf', 'kicadSymbolki_keywords': 'GaN Gate Driver', 'kicadSymbolki_description': 'Single-Channel GaN-Tr High-Speed Gate Driver, Output Current 6.0A, 24V, -5V Negative Gate Voltage, HQFN-16', 'kicadSymbolki_fp_filters': 'Panasonic*HQFN*1EP*4x4mm*P0.65mm*EP2.9x2.9mm*'}])
    newPart['name'].append('Driver_FET : AN34092B')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

