
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "LED_Cree_XHP50_6V"
    hexID = "SZKLLCREEXHP56V"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LED_Cree_XHP50_6V', 'kicadSymbolFootprint': 'LED_SMD:LED_Cree-XHP50_6V', 'kicadSymbolDatasheet': 'http://www.cree.com/%7E/media/Files/Cree/LED%20Components%20and%20Modules/XLamp/Data%20and%20Binning/ds%20XHP50.pdf', 'kicadSymbolki_keywords': 'led diode', 'kicadSymbolki_description': 'XLamp® XHP50 LED, 6V footprint (2x2 serial LEDs in parallel)', 'kicadSymbolki_fp_filters': 'LED?Cree?XHP50?6V*'}])
    newPart['name'].append('LED : LED_Cree_XHP50_6V')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

