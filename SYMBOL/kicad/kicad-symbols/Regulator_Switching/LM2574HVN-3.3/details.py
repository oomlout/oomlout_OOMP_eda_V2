
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2574HVN-3.3"
    hexID = "SZKREGULATORSWITCHINGLM2574HVN33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2574HVN-12', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2574HVN-3.3', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.national.com/ds/LM/LM2574.pdf', 'kicadSymbolki_keywords': 'Step-Down Voltage Regulator 3.3V 500mA HV', 'kicadSymbolki_description': '3.3V, 0.5A SIMPLE SWITCHER® Step-Down Voltage Regulator, High Voltage Input, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LM2574HVN-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

