
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "LTC4364CDE"
    hexID = "SZKPOWERMANAGEMENTLTC4364CDE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4364CDE', 'kicadSymbolFootprint': 'Package_DFN_QFN:DFN-14-1EP_3x4mm_P0.5mm_EP1.7x3.3mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/436412f.pdf', 'kicadSymbolki_keywords': 'ideal-diode or-ing reverse-protection undervoltage overvoltage surge-stopper', 'kicadSymbolki_description': 'Surge stopper with ideal diode, UV and OV protection, -40V to +80V operation, DFN-14 package, 0°C to +40°C', 'kicadSymbolki_fp_filters': 'DFN*3x4mm*P0.5mm*'}])
    newPart['name'].append('Power_Management : LTC4364CDE')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

