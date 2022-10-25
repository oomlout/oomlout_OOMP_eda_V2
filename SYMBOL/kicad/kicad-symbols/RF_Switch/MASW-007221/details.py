
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "RF_Switch"
    oIndex = "MASW-007221"
    hexID = "SZKRFSWITCHMASW7221"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'MASWSS0136', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MASW-007221', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-363_SC-70-6', 'kicadSymbolDatasheet': 'http://cdn.macom.com/datasheets/masw-007221.pdf', 'kicadSymbolki_keywords': 'RF SWITCH SPDT', 'kicadSymbolki_description': 'Macom GaAs RF SPDT switch, DC-3GHz, 0.56/12dB loss/isolation, SOT-363', 'kicadSymbolki_fp_filters': 'SOT*363*'}])
    newPart['name'].append('RF_Switch : MASW-007221')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

