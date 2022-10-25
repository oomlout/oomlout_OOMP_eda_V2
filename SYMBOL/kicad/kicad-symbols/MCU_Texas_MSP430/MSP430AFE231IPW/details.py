
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Texas_MSP430"
    oIndex = "MSP430AFE231IPW"
    hexID = "SZKMCUTEXASMSP43MSP43AFE231IPW"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MSP430AFE221IPW', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MSP430AFE231IPW', 'kicadSymbolFootprint': 'Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/msp430afe231.pdf', 'kicadSymbolki_keywords': 'TI MSP430 16-bit mixed signal microcontroller', 'kicadSymbolki_description': '8kB Flash, 512B RAM, TSSOP-24', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('MCU_Texas_MSP430 : MSP430AFE231IPW')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

