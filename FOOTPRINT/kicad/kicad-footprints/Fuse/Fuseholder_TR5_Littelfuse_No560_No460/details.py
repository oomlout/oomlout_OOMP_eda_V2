
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_TR5_Littelfuse_No560_No460"
    hexID = "FZKFUFUHOLDERTR5LITTELFUNO56NO46"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_TR5_Littelfuse_No560_No460', 'description': 'Fuse, Fuseholder, TR5, Littelfuse/Wickmann, No. 460, No560, https://www.littelfuse.com/~/media/electronics/datasheets/fuse_holders/littelfuse_fuse_holder_559_560_datasheet.pdf.pdf', 'tags': 'Fuse Fuseholder TR5 Littelfuse/Wickmann No. 460 No560 ', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_TR5_Littelfuse_No560_No460.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_TR5_Littelfuse_No560_No460')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

