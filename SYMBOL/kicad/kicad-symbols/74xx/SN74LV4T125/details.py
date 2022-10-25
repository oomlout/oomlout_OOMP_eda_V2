
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "74xx"
    oIndex = "SN74LV4T125"
    hexID = "SZK74XXSN74LV4T125"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': '74LS125', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'SN74LV4T125', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.ti.com/lit/ds/symlink/sn74lv4t125.pdf', 'kicadSymbolki_keywords': '3State CMOS shifter translator', 'kicadSymbolki_description': 'Single Supply Logic Level Translator Quad Buffer with 3-State Outputs', 'kicadSymbolki_fp_filters': 'DIP*W7.62mm*'}])
    newPart['name'].append('74xx : SN74LV4T125')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

