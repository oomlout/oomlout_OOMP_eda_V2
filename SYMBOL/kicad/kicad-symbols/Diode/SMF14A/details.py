
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "SMF14A"
    hexID = "SZKDIODESMF14A"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'SM6T6V8A', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'SMF14A', 'kicadSymbolFootprint': 'Diode_SMD:D_SMF', 'kicadSymbolDatasheet': 'https://www.vishay.com/doc?85881', 'kicadSymbolki_keywords': 'diode TVS voltage suppressor', 'kicadSymbolki_description': '200W unidirectional Transil Transient Voltage Suppressor, 14Vrwm, SMF', 'kicadSymbolki_fp_filters': 'D*SMF*'}])
    newPart['name'].append('Diode : SMF14A')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

