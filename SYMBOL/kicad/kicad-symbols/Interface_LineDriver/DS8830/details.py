
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_LineDriver"
    oIndex = "DS8830"
    hexID = "SZKINTERFACELINEDRIVERDS883"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'DS7830', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'DS8830', 'kicadSymbolFootprint': 'Package_DIP:DIP-14_W7.62mm', 'kicadSymbolDatasheet': 'http://pdf1.alldatasheet.com/datasheet-pdf/view/8473/NSC/DS7830J.html', 'kicadSymbolki_keywords': 'Dual differential line driver', 'kicadSymbolki_description': 'Dual differential line driver and dual four-input NAND or dual four-input AND function, VDD +5V, DIP-14', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('DS8830')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

