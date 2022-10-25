
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "ABS2"
    hexID = "SZKDIODEBRIDGEABS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ABS2', 'kicadSymbolFootprint': 'Diode_SMD:Diode_Bridge_Diotec_ABS', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/abs2.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Miniature Glass Passivated Single-Phase Surface Mount Bridge Rectifiers, 140V Vrms, 0.8A If, ABS SMD package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Diotec*ABS*'}])
    newPart['name'].append('Diode_Bridge : ABS2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

