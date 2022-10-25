
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430FR5720IRGE"
    hexID = "SZKMCUTEXASMSP43MSP43FR572IRGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430FR5720IRGE', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N24_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430fr5720.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '4kB FRAM, 1kB SRAM, QFN-24', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430FR5720IRGE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

