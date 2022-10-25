
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Display_Character"
    oIndex = "RC1602A-GHW-ESX"
    hexID = "SZKDICHARACTERRC162AGHWESX"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'RC1602A-GHW-ESX', 'kicadSymbolFootprint': 'Display:RC1602A', 'kicadSymbolDatasheet': 'http://www.raystar-optronics.com/down.php?ProID=18', 'kicadSymbolki_keywords': 'display LCD dot-matrix', 'kicadSymbolki_description': 'LCD 16x2 Alphanumeric 16pin Gray Backlight', 'kicadSymbolki_fp_filters': 'RC1602A*'}])
    newPart['name'].append('Display_Character : RC1602A-GHW-ESX')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

