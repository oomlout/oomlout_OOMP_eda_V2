
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "MAX17261xxTD"
    hexID = "SZKBATMANAGEMENTMAX17261XXTD"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'MAX17261xxTD', 'kicadSymbolFootprint': 'Package_DFN_QFN:TDFN-14-1EP_3x3mm_P0.4mm_EP1.78x2.35mm', 'kicadSymbolDatasheet': 'https://datasheets.maximintegrated.com/en/ds/MAX17261.pdf', 'kicadSymbolki_keywords': 'Charge pump, battery', 'kicadSymbolki_description': '5.1μA Multi-Cell Fuel Gauge with ModelGauge m5 EZ, TDFN-14', 'kicadSymbolki_fp_filters': 'TDFN*1EP*3x3mm*P0.4mm*'}])
    newPart['name'].append('Battery_Management : MAX17261xxTD')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

