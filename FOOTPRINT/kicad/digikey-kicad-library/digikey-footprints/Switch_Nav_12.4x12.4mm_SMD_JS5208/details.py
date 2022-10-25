
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "digikey-kicad-library"
    oDesc = "digikey-footprints"
    oIndex = "Switch_Nav_12.4x12.4mm_SMD_JS5208"
    hexID = "FZKICADDIGIKEYKICADLIBRARYDIGIKEYFOOTPRINTSSWITCHNAV124X124SMJS528"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Switch_Nav_12.4x12.4mm_SMD_JS5208', 'tags': None, 'attributeType': 'smd', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('digikey-footprints : Switch_Nav_12.4x12.4mm_SMD_JS5208')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

