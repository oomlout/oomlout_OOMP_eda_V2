
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F2013IRSA"
    hexID = "SZKMCUTEXASMSP43MSP43F213IRSA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F2003IRSA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F2013IRSA', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N16_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f2013.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '2kB + 256B Flash, 128B RAM, QFN-16', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F2013IRSA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

