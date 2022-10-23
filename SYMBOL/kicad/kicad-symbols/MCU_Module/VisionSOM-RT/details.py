
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "MCU_Module"
    oIndex = "VisionSOM-RT"
    hexID = "SZKMCUMOVISIONSOMRT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'VisionSOM-RT', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://wiki.somlabs.com/index.php/VisionSOM-RT_Datasheet_and_Pinout', 'kicadSymbolki_keywords': 'somlabs module', 'kicadSymbolki_description': 'i.MX-RT NXP ARM Cortex-M7 528MHz single core industrial SoM computer', 'kicadSymbolki_fp_filters': '*SODIMM*'}])
    newPart['name'].append('VisionSOM-RT')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

