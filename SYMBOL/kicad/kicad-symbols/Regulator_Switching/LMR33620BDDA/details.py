
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LMR33620BDDA"
    hexID = "SZKREGULATORSWITCHINGLMR3362BDDA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LMR33640ADDA', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LMR33620BDDA', 'kicadSymbolFootprint': 'Package_SO:Texas_HSOP-8-1EP_3.9x4.9mm_P1.27mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lmr33620.pdf', 'kicadSymbolki_keywords': 'simple-switcher synchronous buck step-down voltage-regulator', 'kicadSymbolki_description': 'Simple Switcher Synchronous Buck Regulator, Vin=3.8-36V, Iout=2A, F=1400kHz, Adjustable output voltage, HSOP-8', 'kicadSymbolki_fp_filters': 'Texas*HSOP*1EP*'}])
    newPart['name'].append('LMR33620BDDA')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

