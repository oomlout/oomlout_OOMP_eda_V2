
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "L5973D"
    hexID = "SZKREGULATORSWITCHINGL5973D"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L5973D', 'kicadSymbolFootprint': 'Package_SO:HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.41x3.1mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.st.com/resource/en/datasheet/l5973d.pdf', 'kicadSymbolki_keywords': 'step down buck regulator', 'kicadSymbolki_description': '2.5A step down switching regulator, HSOP-8', 'kicadSymbolki_fp_filters': 'HSOP*EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('L5973D')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

