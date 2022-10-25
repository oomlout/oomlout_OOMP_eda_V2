
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SFH900"
    hexID = "SZKSENPROXIMITYSFH9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH900', 'kicadSymbolFootprint': 'OptoDevice:Siemens_SFH900', 'kicadSymbolDatasheet': 'https://www.batronix.com/pdf/sfh900.pdf', 'kicadSymbolki_keywords': 'Reflective Optical Sensor Opto', 'kicadSymbolki_description': 'Miniature Light Reflection Switches', 'kicadSymbolki_fp_filters': 'Siemens*SFH900*'}])
    newPart['name'].append('Sensor_Proximity : SFH900')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

