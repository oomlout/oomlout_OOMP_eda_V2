
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2576S-15"
    hexID = "SZKREGULATORSWITCHINGLM2576S15"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVS-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2576S-15', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2576.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 15V 3A', 'kicadSymbolki_description': '15V, 3A SIMPLE SWITCHER® Step-Down Voltage Regulator, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Switching : LM2576S-15')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

