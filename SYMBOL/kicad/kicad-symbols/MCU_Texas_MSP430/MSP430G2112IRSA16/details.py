
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430G2112IRSA16"
    hexID = "SZKMCUTEXASMSP43MSP43G2112IRSA16"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430G2112IRSA16', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N16_EP2.7x2.7mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430g2112.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '1kB Flash, 128B RAM, QFN-16', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430G2112IRSA16')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

