
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_SMD"
    oIndex = "L_Neosid_Ms95T"
    hexID = "FZKINDUCTORSMLNEOSIDMS95T"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'L_Neosid_Ms95T', 'description': 'Neosid,Inductor,Ms95, Ms95a, Ms95T, Fixed inductor, SMD, https://neosid.de/import-data/product-pdf/neoFestind_Ms95T.pdf', 'tags': 'NeosidInductorMs95 Ms95a Ms95T Fixed inductor SMD', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_SMD.3dshapes/L_Neosid_Ms95T.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Inductor_SMD : L_Neosid_Ms95T')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

