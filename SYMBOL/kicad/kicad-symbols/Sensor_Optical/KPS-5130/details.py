
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "KPS-5130"
    hexID = "SZKSENOPTICALKPS513"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'KPS-5130', 'kicadSymbolFootprint': 'OptoDevice:Kingbright_KPS-5130', 'kicadSymbolDatasheet': 'https://www.kingbright.com/attachments/file/psearch/000/00/00/KPS-5130PD7C(Ver.16).pdf', 'kicadSymbolki_keywords': 'opto photodiode RGB colour sensor', 'kicadSymbolki_description': 'RGB Colour Sensor, KPS-5130', 'kicadSymbolki_fp_filters': 'Kingbright*KPS?5130*'}])
    newPart['name'].append('KPS-5130')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

