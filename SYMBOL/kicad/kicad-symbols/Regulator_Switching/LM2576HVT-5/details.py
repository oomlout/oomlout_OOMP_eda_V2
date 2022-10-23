
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2576HVT-5"
    hexID = "SZKREGULATORSWITCHINGLM2576HVT5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVT-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2576HVT-5', 'kicadSymbolFootprint': 'Package_TO_SOT_THT:TO-220-5_Vertical', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2576.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 5V 3A High Voltage', 'kicadSymbolki_description': '5V, 3A SIMPLE SWITCHER® Step-Down Voltage Regulator, High Voltage Input, TO-220-5', 'kicadSymbolki_fp_filters': 'TO?220*'}])
    newPart['name'].append('LM2576HVT-5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

