
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Regulator_Linear"
    oIndex = "TPS77701_HTSSOP20"
    hexID = "SZKREGULATORLINEARTPS7771HTSS2"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'U', 'kicadSymbolValue': 'TPS77701_HTSSOP20', 'kicadSymbolFootprint': 'Package_SO:HTSSOP-20-1EP_4.4x6.5mm_P0.65mm_EP3.4x6.5mm_ThermalVias', 'kicadSymbolDatasheet': 'http://www.ti.com/lit/ds/symlink/tps777.pdf', 'kicadSymbolki_keywords': '750mA LDO Regulator Adjustable Positive', 'kicadSymbolki_description': '750mA Fast-Transient Low Dropout Voltage Regulator, Adjustable Output 1.5-5.5V, HTSSOP20', 'kicadSymbolki_fp_filters': 'HTSSOP*4.4x6.5mm*P0.65mm*'}])
    newPart['name'].append('Regulator_Linear : TPS77701_HTSSOP20')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

