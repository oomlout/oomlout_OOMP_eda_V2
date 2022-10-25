
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Switching"
    oIndex = "LT1301"
    hexID = "SZKREGULATORSWITCHINGLT131"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'LT1301', 'kicadSymbolFootprint': '', 'kicadSymbolDatasheet': 'https://www.analog.com/media/en/technical-documentation/data-sheets/lt1301.pdf', 'kicadSymbolki_keywords': '5v 12v dc converter boost', 'kicadSymbolki_description': 'Micropower High Efficiency 5V/12V Step-Up DC/DC Converter for Flash Memory, DIP-8/SOIC-8', 'kicadSymbolki_fp_filters': 'DIP*7.62mm* SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Regulator_Switching : LT1301')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

