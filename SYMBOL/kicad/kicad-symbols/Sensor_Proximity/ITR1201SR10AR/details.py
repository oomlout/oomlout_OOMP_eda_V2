
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "ITR1201SR10AR"
    hexID = "SZKSENPROXIMITYITR121SR1AR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ITR1201SR10AR', 'kicadSymbolFootprint': 'OptoDevice:Everlight_ITR1201SR10AR', 'kicadSymbolDatasheet': 'http://www.everlight.com/file/ProductFile/ITR1201SR10AR-TR.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto reflex coupler', 'kicadSymbolki_description': 'Miniature Reflective Optical Object Sensor, SMD-4', 'kicadSymbolki_fp_filters': 'Everlight*ITR1201SR10AR*'}])
    newPart['name'].append('Sensor_Proximity : ITR1201SR10AR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

