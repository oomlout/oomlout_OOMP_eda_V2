
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_BJT"
    oIndex = "BC860"
    hexID = "SZKTRANSISTORBJTBC86"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'BC807', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'BC860', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23', 'kicadSymbolDatasheet': 'http://www.infineon.com/dgdl/Infineon-BC857SERIES_BC858SERIES_BC859SERIES_BC860SERIES-DS-v01_01-en.pdf?fileId=db3a304314dca389011541da0e3a1661', 'kicadSymbolki_keywords': 'PNP Transistor', 'kicadSymbolki_description': '0.1A Ic, 45V Vce, PNP Small Signal Transistor, SOT-23', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Transistor_BJT : BC860')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

