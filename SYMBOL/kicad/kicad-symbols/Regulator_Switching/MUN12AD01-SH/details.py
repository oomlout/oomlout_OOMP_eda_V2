
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "MUN12AD01-SH"
    hexID = "SZKREGULATORSWITCHINGMUN12AD1SH"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MUN12AD01-SH', 'kicadSymbolFootprint': 'Converter_DCDC:Converter_DCDC_Cyntec_MUN12AD01-SH', 'kicadSymbolDatasheet': 'http://www.cyntec.com/upfile/products/download/Cyntec%20MUN12AD01-SH_Datasheet.pdf', 'kicadSymbolki_keywords': 'DC/DC Switching Regulator Power Module 1A Cyntec MUN12AD01', 'kicadSymbolki_description': 'DC/DC Switching Regulator, Power Module, 1A, Cyntec MUN12AD01', 'kicadSymbolki_fp_filters': 'Converter?DCDC?Cyntec?MUN12AD01?SH*'}])
    newPart['name'].append('MUN12AD01-SH')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

