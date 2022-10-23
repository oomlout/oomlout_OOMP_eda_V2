
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "Flir_LEPTON"
    hexID = "SZKSENOPTICALFLIRLEPTON"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'Flir_LEPTON', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://cdn.sparkfun.com/datasheets/Sensors/Infrared/FLIR_Lepton_Data_Brief.pdf', 'kicadSymbolki_keywords': 'LWIR camera', 'kicadSymbolki_description': 'LWIR camera 8 to 14um 80x60 pixel', 'kicadSymbolki_fp_filters': '*105028*1001* *105028*2011*'}])
    newPart['name'].append('Flir_LEPTON')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

