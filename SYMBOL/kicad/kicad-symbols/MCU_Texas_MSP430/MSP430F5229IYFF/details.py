
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430F5229IYFF"
    hexID = "SZKMCUTEXASMSP43MSP43F5229IYFF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430F5227IYFF', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430F5229IYFF', 'kicadSymbolFootprint': 'Package_BGA:Texas_DSBGA-64_3.415x3.535mm_Layout8x8_P0.4mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430f5229.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '128kB Flash, 8kB RAM, BGA-64', 'kicadSymbolki_fp_filters': 'Texas*DSBGA*3.415x3.535mm*Layout8x8*P0.4mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430F5229IYFF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

