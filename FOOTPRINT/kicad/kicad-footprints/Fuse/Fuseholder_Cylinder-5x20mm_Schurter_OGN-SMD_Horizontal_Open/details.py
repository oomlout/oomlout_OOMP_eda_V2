
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Schurter_OGN-SMD_Horizontal_Open"
    hexID = "FZKFUFUHOLDERCYLINDER5X2SCHURTEROGNSMHORIZONTALOPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Schurter_OGN-SMD_Horizontal_Open', 'description': 'Fuseholder horizontal open, 5x20mm, 500V, 16A (https://us.schurter.com/bundles/snceschurter/epim/_ProdPool_/newDS/en/typ_OGN-SMD.pdf)', 'tags': 'Fuseholder horizontal open 5x20 Schurter 0031.8221', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Schurter_OGN-SMD_Horizontal_Open.wrl', 'pins': {'type': 'smd', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Schurter_OGN-SMD_Horizontal_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

