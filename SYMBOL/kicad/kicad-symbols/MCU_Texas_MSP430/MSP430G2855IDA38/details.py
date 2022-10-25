
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430G2855IDA38"
    hexID = "SZKMCUTEXASMSP43MSP43G2855IDA38"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430G2755IDA38', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430G2855IDA38', 'kicadSymbolFootprint': 'Package_SO:TSSOP-38_6.1x12.5mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430g2855.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '48kB Flash, 4kB RAM, TSSOP-38', 'kicadSymbolki_fp_filters': 'TSSOP*6.1x12.5mm*P0.65mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430G2855IDA38')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

