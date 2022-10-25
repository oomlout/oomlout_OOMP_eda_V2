
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Clip-5x20mm_Schurter_OG_Lateral_P15.00x5.00mm_D1.3mm_Horizontal"
    hexID = "FZKFUFUHOLDERCLIP5X2SCHURTEROGLATERALP15X5D13HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Clip-5x20mm_Schurter_OG_Lateral_P15.00x5.00mm_D1.3mm_Horizontal', 'description': 'Fuseholder Clips, 5x20mm Cylinder Fuse, Pins Inline, Horizontal, Schurter OG, https://ch.schurter.com/en/datasheet/typ_OG__Clip__5x20.pdf', 'tags': 'fuse clip open', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Clip-5x20mm_Schurter_OG_Lateral_P15.00x5.00mm_D1.3mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuseholder_Clip-5x20mm_Schurter_OG_Lateral_P15.00x5.00mm_D1.3mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

