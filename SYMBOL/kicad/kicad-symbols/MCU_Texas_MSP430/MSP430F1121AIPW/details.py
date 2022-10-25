
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F1121AIPW"
    hexID = "SZKMCUTEXASMSP43MSP43F1121AIPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F1101AIPW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F1121AIPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-20_4.4x6.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f1121a.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '4kB + 256B Flash, 256B RAM, TSSOP-20', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F1121AIPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

