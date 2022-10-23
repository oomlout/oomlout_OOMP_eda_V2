
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F2111IRGE"
    hexID = "SZKMCUTEXASMSP43MSP43F2111IRGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F2101IRGE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F2111IRGE', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f2111.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '2kB + 256B Flash, 128B RAM, QFN-24', 'kicadSymbolki_fp_filters': 'VQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('MSP430F2111IRGE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

