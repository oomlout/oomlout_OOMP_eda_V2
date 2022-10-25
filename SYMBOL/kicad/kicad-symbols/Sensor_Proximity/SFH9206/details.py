
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Sensor_Proximity"
    oIndex = "SFH9206"
    hexID = "SZKSENPROXIMITYSFH926"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SFH9206', 'kicadSymbolFootprint': 'OptoDevice:Osram_SFH9x0x', 'kicadSymbolDatasheet': 'http://www.osram-os.com/Graphics/XPic6/00200860_0.pdf', 'kicadSymbolki_keywords': 'Reflective Opto Interrupter Coupler', 'kicadSymbolki_description': 'Reflective Opto Interrupter/Coupler, SMD-6', 'kicadSymbolki_fp_filters': 'Osram*SFH9x0x*'}])
    newPart['name'].append('Sensor_Proximity : SFH9206')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

