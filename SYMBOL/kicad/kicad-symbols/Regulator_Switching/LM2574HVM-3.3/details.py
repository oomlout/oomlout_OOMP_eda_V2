
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2574HVM-3.3"
    hexID = "SZKREGULATORSWITCHINGLM2574HVM33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2574HVM-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2574HVM-3.3', 'kicadSymbolFootprint': 'Package_SO:SOIC-14W_7.5x9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.national.com/ds/LM/LM2574.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 3.3V 500mA HV', 'kicadSymbolki_description': '3.3V, 0.5A SIMPLE SWITCHER® Step-Down Voltage Regulator, High Voltage Input, SO-8', 'kicadSymbolki_fp_filters': 'SOIC*7.5x9mm*P1.27mm*'}])
    newPart['name'].append('LM2574HVM-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

