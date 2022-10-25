
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TC2014-2.8VxCTTR"
    hexID = "SZKREGULATORLINEARTC21428VXCTTR"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LP2985-1.8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TC2014-2.8VxCTTR', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-23-5', 'kicadSymbolDatasheet': 'http://ww1.microchip.com/downloads/en/DeviceDoc/21662F.pdf', 'kicadSymbolki_keywords': 'low dropout 2.8V 50mA', 'kicadSymbolki_description': '2.8V 50mA CMOS LDO with Shutdown and Vref Bypass, SOT-23-5', 'kicadSymbolki_fp_filters': 'SOT?23*'}])
    newPart['name'].append('Regulator_Linear : TC2014-2.8VxCTTR')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

