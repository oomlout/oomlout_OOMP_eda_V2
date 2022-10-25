
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IGT40R070D1_E8220"
    hexID = "SZKTRANSISTORFETIGT4R7D1E822"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': 'IGT60R070D1', 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IGT40R070D1_E8220', 'kicadSymbolFootprint': 'Package_TO_SOT_SMD:Infineon_PG-HSOF-8-3_ThermalVias', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IGT40R070D1%20E8220-DataSheet-v02_00-EN.pdf?fileId=5546d4626afcd350016b269dd8f34ec4', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '31A Id, 400V Vds, 70mOhm, N-Channel GaN MOSFET, HSOF-8', 'kicadSymbolki_fp_filters': 'Infineon*PG*HSOF*3*'}])
    newPart['name'].append('Transistor_FET : IGT40R070D1_E8220')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

