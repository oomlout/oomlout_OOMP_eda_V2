
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Driver_FET"
    oIndex = "ACPL-336J"
    hexID = "SZKDRIVERFETACPL336J"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'ACPL-336J', 'kicadSymbolFootprint': 'Package_SO:SOIC-16W_7.5x10.3mm_P1.27mm', 'kicadSymbolDatasheet': 'https://docs.broadcom.com/docs/AV02-4391EN', 'kicadSymbolki_keywords': 'Gate Driver IGBT', 'kicadSymbolki_description': '2.5A Gate Drive Optocoupler with Integrated LED Driver, Active Miller Clamp, DESAT Detection, and Fault & UVLO Status Feedback, SOIC-16', 'kicadSymbolki_fp_filters': 'SOIC*7.5x10.3*P1.27mm*'}])
    newPart['name'].append('Driver_FET : ACPL-336J')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

