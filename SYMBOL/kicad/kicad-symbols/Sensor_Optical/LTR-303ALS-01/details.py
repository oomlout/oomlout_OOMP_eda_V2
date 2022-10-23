
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "LTR-303ALS-01"
    hexID = "SZKSENOPTICALLTR33ALS1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTR-303ALS-01', 'kicadSymbolFootprint': 'OptoDevice:Lite-On_LTR-303ALS-01', 'kicadSymbolDatasheet': 'http://optoelectronics.liteon.com/upload/download/DS86-2013-0004/LTR-303ALS-01_DS_V1.pdf', 'kicadSymbolki_keywords': 'ambient light sensor i2c', 'kicadSymbolki_description': 'ambient light sensor, i2c interface, 0.01 to 64k lux, 2.4-3.6V', 'kicadSymbolki_fp_filters': 'Lite*On*LTR*303ALS*01*'}])
    newPart['name'].append('LTR-303ALS-01')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

