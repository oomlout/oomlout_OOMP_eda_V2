
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "SM6T33A"
    hexID = "SZKDIODESM6T33A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SM6T6V8A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SM6T33A', 'kicadSymbolFootprint': 'Diode_SMD:D_SMB', 'kicadSymbolDatasheet': 'https://www.st.com/resource/en/datasheet/sm6t.pdf', 'kicadSymbolki_keywords': 'diode TVS voltage suppressor', 'kicadSymbolki_description': '600W unidirectional Transil Transient Voltage Suppressor, 33Vrwm, DO-214AA', 'kicadSymbolki_fp_filters': 'D*SMB*'}])
    newPart['name'].append('Diode : SM6T33A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

