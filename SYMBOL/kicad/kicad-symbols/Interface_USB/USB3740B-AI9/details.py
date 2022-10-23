
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_USB"
    oIndex = "USB3740B-AI9"
    hexID = "SZKINTERFACEUU374BAI9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'USB3740B-AI2', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'USB3740B-AI9', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/00001725D.pdf', 'kicadSymbolki_keywords': 'USB 2.0 High Speed Switch', 'kicadSymbolki_description': 'USB 2.0 Switch with ESD Protection, UQFN-10 Pitch 0.5mm', 'kicadSymbolki_fp_filters': 'UQFN*1.3x1.8mm?P0.4mm* UQFN*1.6x2.1mm?P0.5mm*'}])
    newPart['name'].append('USB3740B-AI9')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

