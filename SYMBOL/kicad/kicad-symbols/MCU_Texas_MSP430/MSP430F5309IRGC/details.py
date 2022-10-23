
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5309IRGC"
    hexID = "SZKMCUTEXASMSP43MSP43F539IRGC"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5308IRGC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5309IRGC', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N64_EP4.25x4.25mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5309.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '24kB Flash, 6kB RAM, QFN-64', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MSP430F5309IRGC')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

