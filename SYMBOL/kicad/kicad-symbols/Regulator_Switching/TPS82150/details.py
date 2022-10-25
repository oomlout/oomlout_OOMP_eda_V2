
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TPS82150"
    hexID = "SZKREGULATORSWITCHINGTPS8215"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TPS82130', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS82150', 'kicadSymbolFootprint': 'Package_LGA:Texas_MicroSiP-8-1EP_2.8x3.0mm_P0.65mm_EP1.1x1.9mm_SMD_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps82150.pdf', 'kicadSymbolki_keywords': '17V 1A Step-down Buck Module', 'kicadSymbolki_description': '17V Input 1A Step-Down Converter MicroSiP Module with Integrated Inductor, μSiL-8', 'kicadSymbolki_fp_filters': 'Texas*MicroSiP*1EP*2.8x3.0mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : TPS82150')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

