
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_Motor"
    oIndex = "L298P"
    hexID = "SZKDRIVERMOTORL298P"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'L298P', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.st.com/st-web-ui/static/active/en/resource/technical/document/datasheet/CD00000240.pdf', 'kicadSymbolki_keywords': 'H-bridge motor driver', 'kicadSymbolki_description': 'Dual full bridge motor driver, up to 46V, 4A'}])
    newPart['name'].append('Driver_Motor : L298P')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

