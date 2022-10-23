
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "VisionSOM-6ULL"
    hexID = "SZKMCUMOVISIONSOM6ULL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'VisionSOM-6UL', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VisionSOM-6ULL', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://wiki.somlabs.com/extensions/JZPDFGen/pdf/VisionSOM-6ULL%20Datasheet%20and%20Pinout-21.pdf', 'kicadSymbolki_keywords': 'somlabs module', 'kicadSymbolki_description': 'i.MX6-ULL NXP ARM Cortex-A7 900MHz single core industrial SoM computer', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('VisionSOM-6ULL')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

