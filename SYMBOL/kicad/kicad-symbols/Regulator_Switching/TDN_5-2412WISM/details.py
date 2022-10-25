
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "TDN_5-2412WISM"
    hexID = "SZKREGULATORSWITCHINGTDN52412WISM"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'TDN_5-0910WISM', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TDN_5-2412WISM', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_TRACO_TDN_5-xxxxWISM_SMD', 'kicadSymbolDatasheet': 'https://assets.tracopower.com/20190626081517/TDN5WISM/documents/tdn5wism-datasheet.pdf', 'kicadSymbolki_keywords': 'dcdc traco 5W', 'kicadSymbolki_description': 'Input 9.0 to 36.0V, Output 12.0V', 'kicadSymbolki_fp_filters': 'Converter?DCDC?TRACO?TDN?5*WISM?SMD*'}])
    newPart['name'].append('Regulator_Switching : TDN_5-2412WISM')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

