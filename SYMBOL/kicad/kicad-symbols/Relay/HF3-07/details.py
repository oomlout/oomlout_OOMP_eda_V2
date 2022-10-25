
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Relay"
    oIndex = "HF3-07"
    hexID = "SZKRELAYHF37"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'HF3-01', 'kicadSymbolReference': 'K', 'kicadSymbolValue': 'HF3-07', 'kicadSymbolFootprint': 'Relay_SMD:Relay_SPDT_AXICOM_HF3Series_75ohms_Pitch1.27mm', 'kicadSymbolDatasheet': 'http://hiqsdr.com/images/3/3e/Axicom-HF3.pdf', 'kicadSymbolki_keywords': 'Single Pole Relay SPDT', 'kicadSymbolki_description': 'AXICOM HF3 relay, 3GHz, SPDT RF Switching Relay, 75ohm, 24Vdc, Single-Side Stable', 'kicadSymbolki_fp_filters': 'Relay*SPDT*AXICOM*HF3Series*75ohms*Pitch1.27mm*'}])
    newPart['name'].append('Relay : HF3-07')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

