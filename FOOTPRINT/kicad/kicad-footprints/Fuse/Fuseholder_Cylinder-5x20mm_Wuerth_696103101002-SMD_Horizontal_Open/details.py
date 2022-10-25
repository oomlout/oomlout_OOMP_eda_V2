
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Wuerth_696103101002-SMD_Horizontal_Open"
    hexID = "FZKFUFUHOLDERCYLINDER5X2WUERTH69613112SMHORIZONTALOPEN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Wuerth_696103101002-SMD_Horizontal_Open', 'description': 'Fuseholder horizontal open 5x20mm 250V 10A Würth 696103101002', 'tags': 'Fuseholder horizontal open 5x20mm 250V 10A', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Wuerth_696103101002-SMD_Horizontal_Open.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Wuerth_696103101002-SMD_Horizontal_Open')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

