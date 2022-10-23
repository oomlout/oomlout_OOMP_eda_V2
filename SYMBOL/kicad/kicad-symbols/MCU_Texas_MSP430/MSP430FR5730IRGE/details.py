
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430FR5730IRGE"
    hexID = "SZKMCUTEXASMSP43MSP43FR573IRGE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430FR5720IRGE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430FR5730IRGE', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_S-PVQFN-N24_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430fr5730.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '4kB FRAM, 1kB SRAM, QFN-24', 'kicadSymbolki_fp_filters': 'Texas*S?PVQFN*'}])
    newPart['name'].append('MSP430FR5730IRGE')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

