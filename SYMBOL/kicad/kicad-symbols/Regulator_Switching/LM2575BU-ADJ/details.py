
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2575BU-ADJ"
    hexID = "SZKREGULATORSWITCHINGLM2575BUADJ"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2576HVS-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2575BU-ADJ', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-263-5_TabPin3', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/lm2575.pdf', 'kicadSymbolki_keywords': 'Buck Regulator Switcher', 'kicadSymbolki_description': 'Adjustable 52kHz Simple 1A Buck Regulator, TO-263', 'kicadSymbolki_fp_filters': 'TO?263*'}])
    newPart['name'].append('Regulator_Switching : LM2575BU-ADJ')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

