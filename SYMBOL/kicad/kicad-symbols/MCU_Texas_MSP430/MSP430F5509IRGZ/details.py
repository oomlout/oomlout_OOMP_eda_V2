
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5509IRGZ"
    hexID = "SZKMCUTEXASMSP43MSP43F559IRGZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5508IRGZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5509IRGZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N48_EP5.15x5.15mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5509.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '24kB Flash, 4kB + 2kB RAM, QFN-48', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F5509IRGZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

