
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5501IRGZ"
    hexID = "SZKMCUTEXASMSP43MSP43F551IRGZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5500IRGZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5501IRGZ', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N48_EP5.15x5.15mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5501.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '16kB Flash, 4kB + 2kB RAM, QFN-48', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MSP430F5501IRGZ')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

