
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "BD9778HFP"
    hexID = "SZKREGULATORSWITCHINGBD9778HFP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'BD9778HFP', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Rohm_HRP7', 'kicadSymbolDatasheet': 'http://rohmfs.rohm.com/en/products/databook/datasheet/ic/power/switching_regulator/bd9778f-e.pdf', 'kicadSymbolki_keywords': 'DC-DC Step-Down Switching Regulator', 'kicadSymbolki_description': '35V 2A, Flexible Step-Down Switching Regulator, HRP7', 'kicadSymbolki_fp_filters': 'Rohm*HRP7*'}])
    newPart['name'].append('Regulator_Switching : BD9778HFP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

