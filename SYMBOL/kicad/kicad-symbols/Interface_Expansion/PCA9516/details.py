
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCA9516"
    hexID = "SZKINTERFACEEXPANSIONPCA9516"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCA9516', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/PCA9518.pdf', 'kicadSymbolki_keywords': 'I2C Hub', 'kicadSymbolki_description': '5 channels I2C Hub, SO/TSSOP16', 'kicadSymbolki_fp_filters': 'SO* SOIC* TSSOP*'}])
    newPart['name'].append('Interface_Expansion : PCA9516')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

