
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5310IZQE"
    hexID = "SZKMCUTEXASMSP43MSP43F531IZQE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5308IZQE', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5310IZQE', 'kicadSymbolFootprint': 'Package_BGA:Texas_MicroStar_Junior_BGA-80_5.0x5.0mm_Layout9x9_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5310.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '32kB Flash, 6kB RAM, BGA-80', 'kicadSymbolki_fp_filters': 'Texas*MicroStar*Junior*BGA*5.0x5.0mm*Layout9x9*P0.5mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F5310IZQE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

