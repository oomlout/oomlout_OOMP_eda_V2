
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F1132IDW"
    hexID = "SZKMCUTEXASMSP43MSP43F1132IDW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F1122IDW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F1132IDW', 'kicadSymbolFootprint': 'Package_SO:SOIC-28W_7.5x17.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f1132.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '8kB + 256B Flash, 256B RAM, SOWB-20', 'kicadSymbolki_fp_filters': 'SOIC*7.5x17.9mm*P1.27mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F1132IDW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

