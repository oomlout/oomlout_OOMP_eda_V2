
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM5175RHF"
    hexID = "SZKREGULATORSWITCHINGLM5175RHF"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM5175RHF', 'kicadSymbolFootprint': 'Package_DFN_QFN:VQFN-28-1EP_4x5mm_P0.5mm_EP2.55x3.55mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm5175.pdf', 'kicadSymbolki_keywords': 'Buck Boost step-up step-down', 'kicadSymbolki_description': '42-V wide Vin synchronous 4-switch Buck-Boost controller, QFN-28 package', 'kicadSymbolki_fp_filters': 'VQFN*4x5mm*P0.5*'}])
    newPart['name'].append('Regulator_Switching : LM5175RHF')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

