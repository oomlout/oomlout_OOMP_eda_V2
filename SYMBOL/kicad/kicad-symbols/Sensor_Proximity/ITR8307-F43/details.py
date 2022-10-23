
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "ITR8307-F43"
    hexID = "SZKSENPROXIMITYITR837F43"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ITR8307-F43', 'kicadSymbolFootprint': 'OptoDevice:Everlight_ITR8307F43', 'kicadSymbolDatasheet': 'https://everlighteurope.com/index.php?controller=attachment&id_attachment=5385', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Subminiature Reflective Optical Sensor, DIP-like THT-package', 'kicadSymbolki_fp_filters': 'Everlight*ITR8307F43*'}])
    newPart['name'].append('ITR8307-F43')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

