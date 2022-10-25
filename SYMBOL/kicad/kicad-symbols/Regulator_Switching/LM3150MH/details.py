
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LM3150MH"
    hexID = "SZKREGULATORSWITCHINGLM315MH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LM3150MH', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-14-1EP_4.4x5mm_P0.65mm_EP3.4x5mm_Mask3x3.1mm', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/lm3150.pdf', 'kicadSymbolki_keywords': 'Buck step-down converter', 'kicadSymbolki_description': '42V Wide Vin synchronous Buck controller, HTSSOP-14', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x5mm*P0.65*'}])
    newPart['name'].append('Regulator_Switching : LM3150MH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

