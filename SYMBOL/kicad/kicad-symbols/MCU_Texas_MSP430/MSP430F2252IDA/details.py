
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F2252IDA"
    hexID = "SZKMCUTEXASMSP43MSP43F2252IDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F2232IDA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F2252IDA', 'kicadSymbolFootprint': 'Package_SO:TSSOP-38_6.1x12.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f2252.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '16kB + 256B Flash, 512B RAM, TSSOP-38', 'kicadSymbolki_fp_filters': 'TSSOP*6.1x12.5mm*P0.65mm*'}])
    newPart['name'].append('MSP430F2252IDA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

