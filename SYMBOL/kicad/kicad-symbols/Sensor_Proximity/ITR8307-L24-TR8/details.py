
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "ITR8307-L24-TR8"
    hexID = "SZKSENPROXIMITYITR837L24TR8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'ITR1201SR10AR', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ITR8307-L24-TR8', 'kicadSymbolFootprint': 'OptoDevice:Everlight_ITR1201SR10AR', 'kicadSymbolDatasheet': 'https://www.everlight.com/file/ProductFile/ITR8307-L24-TR8.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto reflex coupler', 'kicadSymbolki_description': 'Miniature Reflective Optical Object Sensor, SMD-4', 'kicadSymbolki_fp_filters': 'Everlight*ITR1201SR10AR*'}])
    newPart['name'].append('Sensor_Proximity : ITR8307-L24-TR8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

