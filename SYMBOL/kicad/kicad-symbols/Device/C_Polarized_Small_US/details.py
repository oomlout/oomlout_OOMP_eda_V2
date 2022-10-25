
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "C_Polarized_Small_US"
    hexID = "SZKDEVICECPOLARIZEDSLLUS"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'C', 'kicadSymbolValue': 'C_Polarized_Small_US', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'cap capacitor', 'kicadSymbolki_description': 'Polarized capacitor, small US symbol', 'kicadSymbolki_fp_filters': 'CP_*'}])
    newPart['name'].append('Device : C_Polarized_Small_US')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

