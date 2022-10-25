
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MASWSS0179"
    hexID = "SZKRFSWITCHMASWSS179"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MASWSS0179', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-6', 'kicadSymbolDatasheet': 'https://cdn.macom.com/datasheets/MASWSS0179.pdf', 'kicadSymbolki_keywords': 'RF SWITCH SPDT', 'kicadSymbolki_description': 'Macom GaAs RF SPDT switch, DC-2GHz, 0.6/22dB loss/isolation, SOT-26 (SOT-23-6)', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('RF_Switch : MASWSS0179')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

