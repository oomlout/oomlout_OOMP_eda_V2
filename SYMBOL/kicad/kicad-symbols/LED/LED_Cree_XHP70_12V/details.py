
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "LED"
    oIndex = "LED_Cree_XHP70_12V"
    hexID = "SZKLLCREEXHP712V"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'LED_Cree_XHP70_12V', 'kicadSymbolFootprint': 'LED_SMD:LED_Cree-XHP70_12V', 'kicadSymbolDatasheet': 'http://www.cree.com/%7E/media/Files/Cree/LED%20Components%20and%20Modules/XLamp/Data%20and%20Binning/ds%20XHP70.pdf', 'kicadSymbolki_keywords': 'led diode', 'kicadSymbolki_description': 'XLamp® XHP70 LED, 12V footprint (all 4 LEDs in series)', 'kicadSymbolki_fp_filters': 'LED?Cree?XHP70?12V*'}])
    newPart['name'].append('LED_Cree_XHP70_12V')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

