
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Battery_Management"
    oIndex = "ADP5090ACP"
    hexID = "SZKBATMANAGEMENTADP59ACP"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ADP5090ACP', 'kicadSymbolFootprint': 'Package_CSP:LFCSP-16-1EP_3x3mm_P0.5mm_EP1.7x1.7mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/ADP5090.pdf', 'kicadSymbolki_keywords': 'boost regulator MPPT charge', 'kicadSymbolki_description': 'Ultralow Power Boost Regulator with MPPT and Charge Management, LFCSP-16', 'kicadSymbolki_fp_filters': 'LFCSP*1EP*3x3mm*P0.5mm*'}])
    newPart['name'].append('Battery_Management : ADP5090ACP')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

