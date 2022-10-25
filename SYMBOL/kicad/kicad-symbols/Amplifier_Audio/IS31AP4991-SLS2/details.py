
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "IS31AP4991-SLS2"
    hexID = "SZKAMPLIFIERAUDIOIS31AP4991SLS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'IS31AP4991-SLS2', 'kicadSymbolFootprint': 'Package_SO:MSOP-8_3x3mm_P0.65mm', 'kicadSymbolDatasheet': 'http://www.issi.com/WW/pdf/31AP4991.pdf', 'kicadSymbolki_keywords': 'ultra low consumption distortion', 'kicadSymbolki_description': '1.2W, 2.7-5.5V, Audio Power Amplifier, Active-Low Standby, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Amplifier_Audio : IS31AP4991-SLS2')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

