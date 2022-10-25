
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMR14206"
    hexID = "SZKREGULATORSWITCHINGLMR1426"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR16006YQ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMR14206', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmr14206.pdf', 'kicadSymbolki_keywords': 'simple-switcher buck step-down voltage-regulator', 'kicadSymbolki_description': 'Simple Switcher Buck Regulator, Vin=4.5-42V, Iout=600mA, Adjustable output voltage, SOT-23-6 package', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Switching : LMR14206')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

