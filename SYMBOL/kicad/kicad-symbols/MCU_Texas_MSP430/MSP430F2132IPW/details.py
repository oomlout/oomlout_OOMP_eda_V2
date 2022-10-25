
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F2132IPW"
    hexID = "SZKMCUTEXASMSP43MSP43F2132IPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F2112IPW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F2132IPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f2132.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '8kB + 256B Flash, 512B RAM, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F2132IPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

