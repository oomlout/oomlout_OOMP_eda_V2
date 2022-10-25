
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SFH9202"
    hexID = "SZKSENPROXIMITYSFH922"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH9206', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH9202', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH9x0x', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic0/00083379_0.pdf/SFH%209202,%20Lead%20%28Pb%29%20Free%20Product%20-%20RoHS%20Compliant.pdf', 'kicadSymbolki_keywords': 'Reflective Opto Interrupter Coupler', 'kicadSymbolki_description': 'Reflective Opto Interrupter/Coupler, SMD-6', 'kicadSymbolki_fp_filters': 'Osram*SFH9x0x*'}])
    newPart['name'].append('Sensor_Proximity : SFH9202')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

