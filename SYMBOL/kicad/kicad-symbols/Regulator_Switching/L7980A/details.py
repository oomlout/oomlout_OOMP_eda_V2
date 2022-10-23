
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "L7980A"
    hexID = "SZKREGULATORSWITCHINGL798A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L7980A', 'kicadSymbolFootprint': 'Package_SO:HSOP-8-1EP_3.9x4.9mm_P1.27mm_EP2.3x2.3mm', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/l7980.pdf', 'kicadSymbolki_keywords': 'step down buck regulator', 'kicadSymbolki_description': '2A step down switching regulator, HSOP-8', 'kicadSymbolki_fp_filters': 'HSOP*EP*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('L7980A')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

