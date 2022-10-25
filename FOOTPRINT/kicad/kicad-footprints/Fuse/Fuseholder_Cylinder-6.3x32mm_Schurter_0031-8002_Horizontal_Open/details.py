
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-6.3x32mm_Schurter_0031-8002_Horizontal_Open"
    hexID = "FZKFUFUHOLDERCYLINDER63X32SCHURTER3182HORIZONTALOPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-6.3x32mm_Schurter_0031-8002_Horizontal_Open', 'description': 'Fuseholder, horizontal, open, 6.3x32, Schurter, 0031.8002, https://www.schurter.com/en/datasheet/typ_OG__Holder__6.3x32.pdf', 'tags': 'Fuseholder horizontal open 6.3x32 Schurter 0031.8002', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-6.3x32mm_Schurter_0031-8002_Horizontal_Open.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-6.3x32mm_Schurter_0031-8002_Horizontal_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

