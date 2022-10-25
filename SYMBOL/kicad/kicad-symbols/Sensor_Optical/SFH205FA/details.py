
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Optical"
    oIndex = "SFH205FA"
    hexID = "SZKSENOPTICALSFH25FA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SFH205F', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SFH205FA', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH205', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic9/00101665_0.pdf', 'kicadSymbolki_keywords': 'PIN Photodiode', 'kicadSymbolki_description': 'Silicon PIN Photodiode with Daylight Blocking Filter', 'kicadSymbolki_fp_filters': 'Osram*SFH205*'}])
    newPart['name'].append('Sensor_Optical : SFH205FA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

