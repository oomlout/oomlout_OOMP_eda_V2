
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Amplifier_Audio"
    oIndex = "THAT2180"
    hexID = "SZKAMPLIFIERAUDIOTHAT218"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'THAT2180', 'kicadSymbolFootprint': 'Package_SIP:SIP-8_19x3mm_P2.54mm', 'kicadSymbolDatasheet': 'http://www.thatcorp.com/datashts/THAT_2180-Series_Datasheet.pdf', 'kicadSymbolki_keywords': 'audio vca', 'kicadSymbolki_description': 'Blackmer Pre-Trimmed IC Voltage Controlled Amplifiers, SIP-8', 'kicadSymbolki_fp_filters': 'SIP*19x3mm*P2.54mm*'}])
    newPart['name'].append('Amplifier_Audio : THAT2180')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

