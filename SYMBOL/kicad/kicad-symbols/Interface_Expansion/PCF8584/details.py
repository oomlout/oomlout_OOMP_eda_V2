
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "PCF8584"
    hexID = "SZKINTERFACEEXPANSIONPCF8584"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'PCF8584', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/PCF8584.pdf', 'kicadSymbolki_keywords': 'I2C Bus', 'kicadSymbolki_description': 'I2C Bus Controller, DIP/SOIC-20', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO* SOIC*'}])
    newPart['name'].append('Interface_Expansion : PCF8584')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

