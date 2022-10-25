
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5634IZQW"
    hexID = "SZKMCUTEXASMSP43MSP43F5634IZQW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5633IZQW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5634IZQW', 'kicadSymbolFootprint': 'Package_BGA:Texas_MicroStar_Junior_BGA-113_7.0x7.0mm_Layout12x12_P0.5mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5634.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '192kB Flash, 16kB + 2kB RAM, BGA-113', 'kicadSymbolki_fp_filters': 'Texas*MicroStar*Junior*BGA*7.0x7.0mm*Layout12x12*P0.5mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F5634IZQW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

