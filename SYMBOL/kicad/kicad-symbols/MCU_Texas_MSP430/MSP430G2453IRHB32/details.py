
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430G2453IRHB32"
    hexID = "SZKMCUTEXASMSP43MSP43G2453IRHB32"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430G2153IRHB32', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430G2453IRHB32', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N32_EP3.45x3.45mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430g2453.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '8kB Flash, 512B RAM, QFN-32', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430G2453IRHB32')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

