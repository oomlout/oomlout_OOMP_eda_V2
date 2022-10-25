
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "KPS-3227"
    hexID = "SZKSENOPTICALKPS3227"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'KPS-3227', 'kicadSymbolFootprint': 'OptoDevice:Kingbright_KPS-3227', 'kicadSymbolDatasheet': 'https://www.kingbright.com/attachments/file/psearch/000/00/00/KPS-3227SP1C(Ver.16).pdf', 'kicadSymbolki_keywords': 'Kingbright npn phototransistor ambient light photo sensor', 'kicadSymbolki_description': 'Ambient light NPN phototransistor, KPS-3227', 'kicadSymbolki_fp_filters': 'Kingbright*KPS?3227*'}])
    newPart['name'].append('Sensor_Optical : KPS-3227')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

