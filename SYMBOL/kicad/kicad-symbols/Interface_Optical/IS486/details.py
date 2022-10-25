
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Interface_Optical"
    oIndex = "IS486"
    hexID = "SZKINTERFACEOPTICALIS486"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS486', 'kicadSymbolFootprint': 'OptoDevice:Sharp_IS485', 'kicadSymbolDatasheet': 'https://media.digikey.com/pdf/Data%20Sheets/Sharp%20PDFs/is485,486_e.pdf', 'kicadSymbolki_keywords': 'opto receiver amplifier light detector OPIC', 'kicadSymbolki_description': 'Built-in Amplifier Type OPIC Light Detector', 'kicadSymbolki_fp_filters': 'Sharp*IS485*'}])
    newPart['name'].append('Interface_Optical : IS486')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

