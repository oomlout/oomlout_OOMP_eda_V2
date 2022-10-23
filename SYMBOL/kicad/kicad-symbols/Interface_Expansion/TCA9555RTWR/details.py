
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TCA9555RTWR"
    hexID = "SZKINTERFACEEXPANSIONTCA9555RTWR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCA9535RTWR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9555RTWR', 'kicadSymbolFootprint': 'Package_DFN_QFN:WQFN-24-1EP_4x4mm_P0.5mm_EP2.45x2.45mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9555.pdf', 'kicadSymbolki_keywords': 'ti parallel port', 'kicadSymbolki_description': '16-bit I/O expander, I2C and SMBus interface, interrupts, w/ pull-ups, QFN-24', 'kicadSymbolki_fp_filters': 'WQFN*1EP*4x4mm*P0.5mm*'}])
    newPart['name'].append('TCA9555RTWR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

