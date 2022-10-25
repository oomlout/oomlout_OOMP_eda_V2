
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Clip-5x20mm_Littelfuse_100_Inline_P20.50x4.60mm_D1.30mm_Horizontal"
    hexID = "FZKFUFUHOLDERCLIP5X2LITTELFU1IP25X46D13HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Clip-5x20mm_Littelfuse_100_Inline_P20.50x4.60mm_D1.30mm_Horizontal', 'description': 'Fuseholder Clips, 5x20mm Cylinder Fuse, Pins Inline, Horizontal, Littelfuse 100, https://m.littelfuse.com/~/media/electronics/datasheets/fuse_clips/littelfuse_fuse_clip_100_445_030_520_datasheet.pdf.pdf', 'tags': 'fuse clip open', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Clip-5x20mm_Littelfuse_100_Inline_P20.50x4.60mm_D1.30mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuseholder_Clip-5x20mm_Littelfuse_100_Inline_P20.50x4.60mm_D1.30mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

