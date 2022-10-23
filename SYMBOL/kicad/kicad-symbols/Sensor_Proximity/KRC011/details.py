
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "KRC011"
    hexID = "SZKSENPROXIMITYKRC11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'KRC011', 'kicadSymbolFootprint': 'OptoDevice:Kingbright_KRC011_Vertical', 'kicadSymbolDatasheet': 'http://www.kingbright.com/attachments/file/psearch/000/00/00/KRC011(Ver.15).pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Subminiature Reflective Optical Sensor', 'kicadSymbolki_fp_filters': 'Kingbright?KRC011*'}])
    newPart['name'].append('KRC011')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

