
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Neosid_SM-NE127"
    hexID = "FZKINDUCTORSMLNEOSIDSMNE127"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Neosid_SM-NE127', 'description': 'Neosid, Inductor, SM-NE127, Fixed inductor, SMD, https://neosid.de/import-data/product-pdf/neoFestind_SMNE127.pdf', 'tags': 'Neosid Inductor SM-NE127 Fixed inductor SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_SM-NE127.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Neosid_SM-NE127')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

