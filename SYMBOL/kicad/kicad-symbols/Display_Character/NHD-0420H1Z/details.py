
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "NHD-0420H1Z"
    hexID = "SZKDICHARACTERNHD42H1Z"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'NHD-0420H1Z', 'kicadSymbolFootprint': 'Display:NHD-0420H1Z', 'kicadSymbolDatasheet': 'http://www.newhavendisplay.com/specs/NHD-0420H1Z-FSW-GBW-33V3.pdf', 'kicadSymbolki_keywords': 'display LCD 20x4', 'kicadSymbolki_description': 'LCD 20x4 Alphanumeric 16pin Blue/White/Green Backlight, 8bit parallel, 3.3V VDD', 'kicadSymbolki_fp_filters': 'NHD*0420H1Z*'}])
    newPart['name'].append('Display_Character : NHD-0420H1Z')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

