
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Zener_Dual_CommonCathode_AAK"
    hexID = "SZKDEVICEDZENERDUALCOONCATHODEAAK"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_Zener_Dual_CommonCathode_AAK', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'diode zener dual', 'kicadSymbolki_description': 'Dual Zener diode, common cathode on pin 3', 'kicadSymbolki_fp_filters': 'SOT* SC*'}])
    newPart['name'].append('D_Zener_Dual_CommonCathode_AAK')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

