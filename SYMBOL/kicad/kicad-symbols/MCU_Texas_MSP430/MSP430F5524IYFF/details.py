
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5524IYFF"
    hexID = "SZKMCUTEXASMSP43MSP43F5524IYFF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5524IYFF', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5524.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '64kB Flash, 4kB + 2kB RAM, BGA-64', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*3.415x3.535mm*Layout8x8*P0.4mm*'}])
    newPart['name'].append('MSP430F5524IYFF')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

