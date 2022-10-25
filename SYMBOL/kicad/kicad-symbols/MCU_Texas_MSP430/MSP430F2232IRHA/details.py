
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F2232IRHA"
    hexID = "SZKMCUTEXASMSP43MSP43F2232IRHA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F2232IRHA', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N40_EP4.15x4.15mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f2232.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '8kB + 256B Flash, 512B RAM, QFN-40', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F2232IRHA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

