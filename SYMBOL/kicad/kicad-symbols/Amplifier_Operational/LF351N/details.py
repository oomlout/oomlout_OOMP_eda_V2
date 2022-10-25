
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Operational"
    oIndex = "LF351N"
    hexID = "SZKAMPLIFIEROPERATIONALLF351N"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LF351N', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/lf351.pdf', 'kicadSymbolki_keywords': 'Single OpAmp JFET', 'kicadSymbolki_description': 'Wide bandwidth single JFET operational amplifier, DIP-8', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('Amplifier_Operational : LF351N')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

