
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5176PWP"
    hexID = "SZKREGULATORSWITCHINGLM5176PWP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LM5175PWP', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5176PWP', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-28-1EP_4.4x9.7mm_P0.65mm_EP3.4x9.5mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5176.pdf', 'kicadSymbolki_keywords': 'Buck Boost step-up step-down', 'kicadSymbolki_description': '55-V wide Vin synchronous 4-switch Buck-Boost controller, HTSSOP-28 package', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x9.7mm*P0.65*ThermalVias*'}])
    newPart['name'].append('Regulator_Switching : LM5176PWP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

