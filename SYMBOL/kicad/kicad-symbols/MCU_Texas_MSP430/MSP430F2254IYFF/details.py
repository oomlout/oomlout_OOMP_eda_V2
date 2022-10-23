
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F2254IYFF"
    hexID = "SZKMCUTEXASMSP43MSP43F2254IYFF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F2234IYFF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F2254IYFF', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-49_3.33x3.488mm_Layout7x7_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f2254.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '16kB + 256B Flash, 512B RAM, BGA-49', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*3.33x3.488mm*Layout7x7*P0.4mm*'}])
    newPart['name'].append('MSP430F2254IYFF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

