
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Switch"
    oIndex = "SW_MEC_5G_2LED"
    hexID = "SZKSWITCHSWMEC5G2L"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'SW', 'kicadSymbolValue': 'SW_MEC_5G_2LED', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.apem.com/int/index.php?controller=attachment&id_attachment=488', 'kicadSymbolki_keywords': 'switch normally-open pushbutton push-button LED', 'kicadSymbolki_description': 'MEC 5G single pole normally-open illuminated tactile switch with two LEDs', 'kicadSymbolki_fp_filters': 'SW*MEC*5G*'}])
    newPart['name'].append('Switch : SW_MEC_5G_2LED')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

