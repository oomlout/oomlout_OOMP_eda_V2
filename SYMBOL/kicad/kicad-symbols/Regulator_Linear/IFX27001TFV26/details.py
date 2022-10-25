
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "IFX27001TFV26"
    hexID = "SZKREGULATORLINEARIFX271TFV26"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IFX27001TFV15', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IFX27001TFV26', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:TO-252-3_TabPin2', 'kicadSymbolDatasheet': 'https://static6.arrow.com/aropdfconversion/dc75757ae45a88e5f69bdce3f2a651a5fe0ca07d/ifx27001_ds_10.pdf', 'kicadSymbolki_keywords': 'LDO positive voltage industrial', 'kicadSymbolki_description': '1A Low Dropout Regulator, positive, 2.6V fixed output, TO-252-3', 'kicadSymbolki_fp_filters': 'TO?252*'}])
    newPart['name'].append('Regulator_Linear : IFX27001TFV26')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

