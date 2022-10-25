
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "CC430F5137xRGZ"
    hexID = "SZKMCUTEXASMSP43CC43F5137XRGZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'CC430F5137xRGZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-48-1EP_7x7mm_P0.5mm_EP4.1x4.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/cc430f5137.pdf', 'kicadSymbolki_keywords': 'TI MSP430 CC430 16-bit mixed signal microcontroller CC1101', 'kicadSymbolki_description': '32KB Flash, 4KB RAM, MSP430 core with integrated CC1101 radio transceiver, VQFN-48', 'kicadSymbolki_fp_filters': 'VQFN*1EP*7x7mm*P0.5mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : CC430F5137xRGZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

