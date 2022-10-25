
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Power_Management"
    oIndex = "FPF2005"
    hexID = "SZKPOWERMANAGEMENTFPF25"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'FPF2000', 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'FPF2005', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:SOT-353_SC-70-5', 'kicadSymbolDatasheet': 'https://www.onsemi.com/pub/Collateral/FPF2001-D.pdf', 'kicadSymbolki_keywords': '1-chanel power-distribution USB', 'kicadSymbolki_description': 'Single power-distribution switcher, current limit = 100mA, blanking time = 10 ms, auto-restart time = 80 ms, ON Pin Polarity = LOW, SOT-353', 'kicadSymbolki_fp_filters': 'SOT?353*'}])
    newPart['name'].append('Power_Management : FPF2005')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

