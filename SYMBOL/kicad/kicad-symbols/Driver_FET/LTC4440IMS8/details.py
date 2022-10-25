
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "LTC4440IMS8"
    hexID = "SZKDRIVERFETLTC444IMS8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LTC4440EMS8', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LTC4440IMS8', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/4440fb.pdf', 'kicadSymbolki_keywords': 'high-side mosfet-driver', 'kicadSymbolki_description': 'High-side, N-Channel, Mosfet driver, 80V input, -40°C to +125°C, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Driver_FET : LTC4440IMS8')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

