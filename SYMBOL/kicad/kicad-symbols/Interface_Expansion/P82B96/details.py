
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Expansion"
    oIndex = "P82B96"
    hexID = "SZKINTERFACEEXPANSIONP82B96"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'P82B96', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.nxp.com/documents/data_sheet/P82B96.pdf', 'kicadSymbolki_keywords': 'I2C Bus Buffer', 'kicadSymbolki_description': 'Dual I2C Bus Buffer, DIP8/SO8/TSSOP8', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SOIC* SO* TSSOP*'}])
    newPart['name'].append('Interface_Expansion : P82B96')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

