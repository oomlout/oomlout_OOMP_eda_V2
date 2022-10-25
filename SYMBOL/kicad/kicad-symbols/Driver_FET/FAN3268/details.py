
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "FAN3268"
    hexID = "SZKDRIVERFETFAN3268"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FAN3268', 'kicadSymbolFootprint': 'Package_SO:SOIC-8_3.9x4.9mm_P1.27mm', 'kicadSymbolDatasheet': 'http://www.onsemi.com/pub/Collateral/FAN3268T_F085-D.PDF', 'kicadSymbolki_keywords': 'Driver MOSFET', 'kicadSymbolki_description': 'Low-Voltage 18V PMOS-NMOS Bridge Driver, SOIC-8', 'kicadSymbolki_fp_filters': '*SOIC*3.9x4.9mm*P1.27mm*'}])
    newPart['name'].append('Driver_FET : FAN3268')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

