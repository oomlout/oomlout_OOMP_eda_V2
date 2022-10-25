
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT3580xMS8E"
    hexID = "SZKREGULATORSWITCHINGLT358XMS8E"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT3580xMS8E', 'kicadSymbolFootprint': 'Package_SO:MSOP-8-1EP_3x3mm_P0.65mm_EP1.68x1.88mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/3580fg.pdf', 'kicadSymbolki_keywords': 'boost inverting dc-dc', 'kicadSymbolki_description': 'Boost/Inverting DC/DC Converter with 2A Switch, Soft-Start, and Synchronization, MSOP-8', 'kicadSymbolki_fp_filters': 'MSOP*1EP*3x3mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Switching : LT3580xMS8E')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

