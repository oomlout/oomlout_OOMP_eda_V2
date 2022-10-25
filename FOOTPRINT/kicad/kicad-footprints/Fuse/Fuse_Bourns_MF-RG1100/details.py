
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuse_Bourns_MF-RG1100"
    hexID = "FZKFUFUBOURNSMFRG11"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuse_Bourns_MF-RG1100', 'description': 'PTC Resettable Fuse, Ihold = 11.0A, Itrip=18.7A, http://www.bourns.com/docs/Product-Datasheets/mfrg.pdf', 'tags': 'ptc resettable fuse polyfuse THT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_Bourns_MF-RG1100.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuse_Bourns_MF-RG1100')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

