
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "ACPL-W343"
    hexID = "SZKDRIVERFETACPLW343"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACPL-W343', 'kicadSymbolFootprint': 'Package_SO:SSO-6_6.8x4.6mm_P1.27mm_Clearance8mm', 'kicadSymbolDatasheet': 'http://www.avagotech.com/docs/AV02-2928EN', 'kicadSymbolki_keywords': 'MOSFET Driver IGBT Driver Optocoupler', 'kicadSymbolki_description': 'Gate Drive Optocoupler, Output Current 4.0/4.0A, Propagation Delay 200ns, SSO-6', 'kicadSymbolki_fp_filters': 'SSO*6.8x4.6mm*P1.27mm*Clearance8mm*'}])
    newPart['name'].append('Driver_FET : ACPL-W343')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

