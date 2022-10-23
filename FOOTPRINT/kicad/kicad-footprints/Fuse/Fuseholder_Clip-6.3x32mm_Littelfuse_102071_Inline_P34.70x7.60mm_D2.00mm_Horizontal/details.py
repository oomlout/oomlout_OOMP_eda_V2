
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Clip-6.3x32mm_Littelfuse_102071_Inline_P34.70x7.60mm_D2.00mm_Horizontal"
    hexID = "FZKFUFUHOLDERCLIP63X32LITTELFU1271IP347X76D2HORIZONTAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Clip-6.3x32mm_Littelfuse_102071_Inline_P34.70x7.60mm_D2.00mm_Horizontal', 'description': 'Fuseholder Clips, 6.3x32mm Cylinder Fuse, Pins Inline, Horizontal, Littelfuse 102071, https://www.littelfuse.com/~/media/electronics/datasheets/fuse_clips/littelfuse_fuse_clip_520_521_102071_datasheet.pdf.pdf', 'tags': 'fuse clip open', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Clip-6.3x32mm_Littelfuse_102071_Inline_P34.70x7.60mm_D2.00mm_Horizontal.wrl', 'pins': {'type': 'thru_hole', 'shape': 'roundrect'}})
    newPart['name'].append('Fuse : Fuseholder_Clip-6.3x32mm_Littelfuse_102071_Inline_P34.70x7.60mm_D2.00mm_Horizontal')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

