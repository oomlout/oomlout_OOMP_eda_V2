
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MASWSS0143"
    hexID = "SZKRFSWITCHMASWSS143"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MASWSS0136', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MASWSS0143', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'https://cdn.macom.com/datasheets/MASWSS0143.pdf', 'kicadSymbolki_keywords': 'RF SWITCH SPDT', 'kicadSymbolki_description': 'Macom GaAs RF SPDT switch, DC-3GHz, 0.4/16dB loss/isolation, IP 58dB@1GHz, SOT-363', 'kicadSymbolki_fp_filters': 'SOT*363*'}])
    newPart['name'].append('RF_Switch : MASWSS0143')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

