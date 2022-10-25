
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BCP56"
    hexID = "SZKTRANSISTORBJTBCP56"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'PZT3904', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BCP56', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-223-3_TabPin2', 'kicadSymbolDatasheet': 'http://cache.nxp.com/documents/data_sheet/BCP56_BCX56_BC56PA.pdf?pspll=1', 'kicadSymbolki_keywords': 'NPN Transistor', 'kicadSymbolki_description': '1A Ic, 80V Vce, NPN Medium Power Transistor, SOT-223', 'kicadSymbolki_fp_filters': 'SOT?223*'}])
    newPart['name'].append('Transistor_BJT : BCP56')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

