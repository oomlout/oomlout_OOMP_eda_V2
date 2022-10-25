
######  Auto translated oomp file

def load(newPart,it):
    oType = "SYMBOL"
    oSize = "kicad"
    oColor = "kicad-symbols"
    oDesc = "Transistor_FET"
    oIndex = "IGO60R070D1"
    hexID = "SZKTRANSISTORFETIGO6R7D1"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['symbolKicadDetails'].append([{'kicadSymbolExtends': None, 'kicadSymbolReference': 'Q', 'kicadSymbolValue': 'IGO60R070D1', 'kicadSymbolFootprint': 'Package_SO:Infineon_PG-DSO-20-85', 'kicadSymbolDatasheet': 'https://www.infineon.com/dgdl/Infineon-IGO60R070D1-DataSheet-v02_01-EN.pdf?fileId=5546d46265f064ff016685f053216514', 'kicadSymbolki_keywords': 'N-Channel GaN MOSFET', 'kicadSymbolki_description': '31A Id, 600V Vds, 70mOhm, N-Channel GaN MOSFET, PD-DSO-20-85', 'kicadSymbolki_fp_filters': 'Infineon*PG*DSO*85*'}])
    newPart['name'].append('Transistor_FET : IGO60R070D1')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

