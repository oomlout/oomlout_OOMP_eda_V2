
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMR16006YQ5"
    hexID = "SZKREGULATORSWITCHINGLMR166YQ5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR16006YQ', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMR16006YQ5', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmr16006y-q1.pdf', 'kicadSymbolki_keywords': 'simple-switcher buck step-down voltage-regulator', 'kicadSymbolki_description': 'Simple Switcher Buck Regulator, Vin=4-40V, Iout=600mA, Fixed 5.0V output voltage, SOT-23-6 package', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('LMR16006YQ5')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

