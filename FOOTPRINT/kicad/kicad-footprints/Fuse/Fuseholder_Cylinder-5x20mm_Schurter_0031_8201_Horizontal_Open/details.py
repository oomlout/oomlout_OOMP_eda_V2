
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Schurter_0031_8201_Horizontal_Open"
    hexID = "FZKFUFUHOLDERCYLINDER5X2SCHURTER31821HORIZONTALOPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Schurter_0031_8201_Horizontal_Open', 'description': 'Fuseholder horizontal open, 5x20mm, 500V, 16A, Schurter 0031.8201, https://us.schurter.com/bundles/snceschurter/epim/_ProdPool_/newDS/en/typ_OGN.pdf', 'tags': 'Fuseholder horizontal open 5x20 Schurter 0031.8201', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Schurter_0031_8201_Horizontal_Open.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Schurter_0031_8201_Horizontal_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

