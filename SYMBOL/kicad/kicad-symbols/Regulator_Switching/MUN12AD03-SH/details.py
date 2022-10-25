
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MUN12AD03-SH"
    hexID = "SZKREGULATORSWITCHINGMUN12AD3SH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MUN12AD03-SH', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Cyntec_MUN12AD03-SH', 'kicadSymbolDatasheet': 'http://www.cyntec.com/upfile/products/download/Cyntec%20MUN12AD03-SH_Datasheet.pdf', 'kicadSymbolki_keywords': 'DC/DC Switching Regulator Power Module 3A Cyntec MUN12AD03', 'kicadSymbolki_description': 'DC/DC Switching Regulator, Power Module, 3A, Cyntec MUN12AD03', 'kicadSymbolki_fp_filters': 'Converter?DCDC?Cyntec?MUN12AD03?SH*'}])
    newPart['name'].append('Regulator_Switching : MUN12AD03-SH')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

