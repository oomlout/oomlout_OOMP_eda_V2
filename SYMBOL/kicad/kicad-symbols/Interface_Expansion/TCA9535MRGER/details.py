
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TCA9535MRGER"
    hexID = "SZKINTERFACEEXPANSIONTCA9535MRGER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCA9535RGER', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9535MRGER', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9535.pdf', 'kicadSymbolki_keywords': 'ti parallel port', 'kicadSymbolki_description': '16-bit I/O expander, I2C and SMBus interface, interrupts, w/o pull-ups, QFN-24', 'kicadSymbolki_fp_filters': 'VQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('Interface_Expansion : TCA9535MRGER')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

