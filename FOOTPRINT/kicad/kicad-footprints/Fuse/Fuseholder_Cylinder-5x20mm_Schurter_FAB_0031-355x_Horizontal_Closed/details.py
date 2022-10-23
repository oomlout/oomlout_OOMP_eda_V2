
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-5x20mm_Schurter_FAB_0031-355x_Horizontal_Closed"
    hexID = "FZKFUFUHOLDERCYLINDER5X2SCHURTERFAB31355XHORIZONTALCLOSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-5x20mm_Schurter_FAB_0031-355x_Horizontal_Closed', 'description': 'Fuseholder 5x20mm horizontal Shurter model FAB, Suitable for order numbers 0031.3551 and 0031.3558  (https://www.schurter.com/bundles/snceschurter/epim/_ProdPool_/newDS/en/typ_FAB.pdf)', 'tags': 'Fuseholder 5x20mm closed horizontal', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Schurter_FAB_0031-355x_Horizontal_Closed.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-5x20mm_Schurter_FAB_0031-355x_Horizontal_Closed')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

