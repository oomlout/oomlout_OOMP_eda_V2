
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TCA9555DBR"
    hexID = "SZKINTERFACEEXPANSIONTCA9555DBR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCA9535DBR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9555DBR', 'kicadSymbolFootprint': 'Package_SO:SSOP-24_5.3x8.2mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9555.pdf', 'kicadSymbolki_keywords': 'ti parallel port', 'kicadSymbolki_description': '16-bit I/O expander, I2C and SMBus interface, interrupts, w/ pull-ups, SSOP-24', 'kicadSymbolki_fp_filters': 'SSOP*5.3x8.2mm*P0.65mm*'}])
    newPart['name'].append('Interface_Expansion : TCA9555DBR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

