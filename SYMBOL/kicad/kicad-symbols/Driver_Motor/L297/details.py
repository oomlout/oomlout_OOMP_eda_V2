
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "L297"
    hexID = "SZKDRIVERMOTORL297"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L297', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'www.st.com/resource/en/datasheet/cd00000063.pdf', 'kicadSymbolki_keywords': 'Stepper Motor Controller', 'kicadSymbolki_description': 'Stepper Motor Controller, DIP-20/SO-20', 'kicadSymbolki_fp_filters': 'DIP* SO*'}])
    newPart['name'].append('L297')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

