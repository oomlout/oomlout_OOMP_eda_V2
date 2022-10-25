
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TCA9555PWR"
    hexID = "SZKINTERFACEEXPANSIONTCA9555PWR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCA9535PWR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9555PWR', 'kicadSymbolFootprint': 'Package_SO:TSSOP-24_4.4x7.8mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9555.pdf', 'kicadSymbolki_keywords': 'ti parallel port', 'kicadSymbolki_description': '16-bit I/O expander, I2C and SMBus interface, interrupts, w/ pull-ups, TSSOP-24 package', 'kicadSymbolki_fp_filters': 'TSSOP*4.4x7.8mm*P0.65mm*'}])
    newPart['name'].append('Interface_Expansion : TCA9555PWR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

