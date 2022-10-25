
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS74401_VQFN"
    hexID = "SZKREGULATORLINEARTPS7441VQFN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS74401_VQFN', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'http://www.ti.com/general/docs/lit/getliterature.tsp?genericPartNumber=tps74401&fileType=pdf', 'kicadSymbolki_keywords': 'LDO, Voltage Regulator', 'kicadSymbolki_description': '0.8 to 3.6V adjustable, 3.0-A, Ultra-LDO with Programmable Soft-Start', 'kicadSymbolki_fp_filters': 'Texas*VQFN*RGR* Texas*VQFN*RGW*'}])
    newPart['name'].append('Regulator_Linear : TPS74401_VQFN')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

