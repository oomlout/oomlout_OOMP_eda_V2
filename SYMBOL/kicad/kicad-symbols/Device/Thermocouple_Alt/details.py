
######  Auto translated oomp file

def load(newPart):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Device"
    oIndex = "Thermocouple_Alt"
    hexID = "SZKDEVICETHERMOCOUPLEALT"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'TC', 'kicadSymbolValue': 'Thermocouple_Alt', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': '~', 'kicadSymbolki_keywords': 'thermocouple temperature sensor cold junction', 'kicadSymbolki_description': 'Thermocouple with connector block', 'kicadSymbolki_fp_filters': 'PIN?ARRAY* bornier* *Terminal?Block* Thermo*Couple*'}])
    newPart['name'].append('Thermocouple_Alt')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

