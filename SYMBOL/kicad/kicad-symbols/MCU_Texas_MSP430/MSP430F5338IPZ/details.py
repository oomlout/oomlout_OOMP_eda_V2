
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5338IPZ"
    hexID = "SZKMCUTEXASMSP43MSP43F5338IPZ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5336IPZ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5338IPZ', 'kicadSymbolFootprint': 'Package_QFP:LQFP-100_14x14mm_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5338.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '256kB Flash, 18kB RAM, LQFP-100', 'kicadSymbolki_fp_filters': 'LQFP*14x14mm*P0.5mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F5338IPZ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

