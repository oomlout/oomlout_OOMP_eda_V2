
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "TCA9548ARGER"
    hexID = "SZKINTERFACEEXPANSIONTCA9548ARGER"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TCA9548AMRGER', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TCA9548ARGER', 'kicadSymbolFootprint': 'Package_DFN_QFN:Texas_RGE0024C_EP2.1x2.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tca9548a.pdf', 'kicadSymbolki_keywords': 'Low voltage 8-channel I2C switch with reset', 'kicadSymbolki_description': 'Low voltage 8-channel I2C switch with reset, QFN-24', 'kicadSymbolki_fp_filters': 'Texas*RGE0024C*'}])
    newPart['name'].append('TCA9548ARGER')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

