
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Blade_ATO_Littelfuse_Pudenz_2_Pin"
    hexID = "FZKFUFUHOLDERBLADEATOLITTELFUPUDENZ2PIN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Blade_ATO_Littelfuse_Pudenz_2_Pin', 'description': 'Fuseholder ATO Blade littelfuse Pudenz 2 Pin', 'tags': 'Fuseholder ATO Blade littelfuse Pudenz 2 Pin', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Blade_ATO_Littelfuse_Pudenz_2_Pin.wrl', 'pins': {'type': 'np_thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuseholder_Blade_ATO_Littelfuse_Pudenz_2_Pin')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

