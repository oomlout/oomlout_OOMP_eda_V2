
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Telecom"
    oIndex = "FX614"
    hexID = "SZKINTERFACETELECOMFX614"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FX614', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.cmlmicro.com/wp-content/uploads/2017/06/FX614_ds.pdf', 'kicadSymbolki_keywords': 'Bell Modem', 'kicadSymbolki_description': 'Bell 202 Compatible Modem, DIP-16/SO-16', 'kicadSymbolki_fp_filters': 'DIP* PDIP* SO*'}])
    newPart['name'].append('Interface_Telecom : FX614')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

