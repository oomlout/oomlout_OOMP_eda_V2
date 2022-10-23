
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "QRE1113GR"
    hexID = "SZKSENPROXIMITYQRE1113GR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'QRE1113GR', 'kicadSymbolFootprint': 'OptoDevice:OnSemi_CASE100CY', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/QRE1113-D.PDF', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto reflex coupler', 'kicadSymbolki_description': 'Miniature Reflective Optical Object Sensor, SMD-4', 'kicadSymbolki_fp_filters': 'OnSemi*CASE100CY*'}])
    newPart['name'].append('QRE1113GR')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

