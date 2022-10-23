
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "VisionSOM-6UL"
    hexID = "SZKMCUMOVISIONSOM6UL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VisionSOM-6UL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://wiki.somlabs.com/extensions/JZPDFGen/pdf/VisionSOM-6UL%20Datasheet%20and%20Pinout-41.pdf', 'kicadSymbolki_keywords': 'somlabs module', 'kicadSymbolki_description': 'i.MX6-UL NXP ARM Cortex-A7 696MHz single core industrial SoM computer', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('VisionSOM-6UL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

