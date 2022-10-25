
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430G2333IPW28"
    hexID = "SZKMCUTEXASMSP43MSP43G2333IPW28"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430G2233IPW28', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430G2333IPW28', 'kicadSymbolFootprint': 'Package_SO:TSSOP-28_4.4x9.7mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430g2333.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '4kB Flash, 256B RAM, TSSOP-28', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x9.7mm*P0.65mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430G2333IPW28')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

