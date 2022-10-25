
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM2594HVN-3.3"
    hexID = "SZKREGULATORSWITCHINGLM2594HVN33"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM2594N-3.3', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM2594HVN-3.3', 'kicadSymbolFootprint': 'Package_DIP:DIP-8_W7.62mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm2594.pdf', 'kicadSymbolki_keywords': 'buck converter regulator step-down voltage simple switcher fixed', 'kicadSymbolki_description': '3.3V, 0.5A SIMPLE SWITCHER® Step-Down Voltage Regulator, Maximum VIN 60V, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Regulator_Switching : LM2594HVN-3.3')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

