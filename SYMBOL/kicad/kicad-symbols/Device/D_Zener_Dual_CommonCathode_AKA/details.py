
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "D_Zener_Dual_CommonCathode_AKA"
    hexID = "SZKDEVICEDZENERDUALCOONCATHODEAKA"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'D', 'kicadSymbolValue': 'D_Zener_Dual_CommonCathode_AKA', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'diode zener dual', 'kicadSymbolki_description': 'Dual Zener diode, common cathode on pin 2', 'kicadSymbolki_fp_filters': 'SOT* SC*'}])
    newPart['name'].append('Device : D_Zener_Dual_CommonCathode_AKA')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

