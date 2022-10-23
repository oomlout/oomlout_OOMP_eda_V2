
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Cylinder-6.3x32mm_Schurter_FUP_0031.2520_Horizontal_Closed"
    hexID = "FZKFUFUHOLDERCYLINDER63X32SCHURTERFUP31252HORIZONTALCLOSED"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Cylinder-6.3x32mm_Schurter_FUP_0031.2520_Horizontal_Closed', 'description': 'Shock-Safe closed Fuseholder, Schurter FUP Series, 6.3 x 32 mm, Slotted Cap, horizontal, 500 VAC 4W/16A (VDE), 600V 30A (UL/CSA), order numbers: 0031.2520 (0031.2500 + 0031.2321), http://www.schurter.ch/bundles/snceschurter/epim/_ProdPool_/newDS/en/typ_FUP.pdf', 'tags': 'Fuseholder 6.3x32mm horizontal closed', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Cylinder-5x20mm_Schurter_FUP_0031.2510_Horizontal_Closed.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Cylinder-6.3x32mm_Schurter_FUP_0031.2520_Horizontal_Closed')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

