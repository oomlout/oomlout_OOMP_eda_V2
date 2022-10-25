
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode_Bridge"
    oIndex = "ABS4"
    hexID = "SZKDIODEBRIDGEABS4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ABS2', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'ABS4', 'kicadSymbolFootprint': 'Diode_SMD:Diode_Bridge_Diotec_ABS', 'kicadSymbolDatasheet': 'https://diotec.com/tl_files/diotec/files/pdf/datasheets/abs2.pdf', 'kicadSymbolki_keywords': 'rectifier acdc', 'kicadSymbolki_description': 'Miniature Glass Passivated Single-Phase Surface Mount Bridge Rectifiers, 280V Vrms, 0.8A If, ABS SMD package', 'kicadSymbolki_fp_filters': 'Diode*Bridge*Diotec*ABS*'}])
    newPart['name'].append('Diode_Bridge : ABS4')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

