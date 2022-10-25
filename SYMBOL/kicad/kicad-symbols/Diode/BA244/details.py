
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Diode"
    oIndex = "BA244"
    hexID = "SZKDIODEBA244"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '1N4001', 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'BA244', 'kicadSymbolFootprint': 'Diode_THT:D_DO-35_SOD27_P7.62mm_Horizontal', 'kicadSymbolDatasheet': 'http://cdn-reichelt.de/documents/datenblatt/A400/BA243_TFK.pdf', 'kicadSymbolki_keywords': 'diode', 'kicadSymbolki_description': '20V 0.1A silicon planar diode for VHF tuner band selection, DO-35', 'kicadSymbolki_fp_filters': 'D*DO?35*'}])
    newPart['name'].append('Diode : BA244')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

