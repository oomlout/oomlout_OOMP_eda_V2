
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT8610AC-1"
    hexID = "SZKREGULATORSWITCHINGLT861AC1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'LT8610AC', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT8610AC-1', 'kicadSymbolFootprint': 'Package_SO:LTC_MSOP-16-1EP_3x4mm_P0.5mm_EP2.15x3.26mm', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/8610acfa.pdf', 'kicadSymbolki_keywords': 'high efficiency speed synchronous monolithic buck step-down switching regulator 42V 3.5A lower feedback voltage minimum vin internal compensation soft-start', 'kicadSymbolki_description': '42V, 3.5A Synchronous Step-Down Regulator with 2.5uA Quiescent Current, Internal Compensation for Improved Transient, Soft-Start at Dropout and Brownout, MSOP-16', 'kicadSymbolki_fp_filters': 'LTC*MSOP*16*1EP*3x4mm*P0.5mm*EP2.15x3.26mm*'}])
    newPart['name'].append('Regulator_Switching : LT8610AC-1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

