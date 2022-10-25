
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuse_Bourns_MF-RG400"
    hexID = "FZKFUFUBOURNSMFRG4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuse_Bourns_MF-RG400', 'description': 'PTC Resettable Fuse, Ihold = 4.0A, Itrip=6.8A, http://www.bourns.com/docs/Product-Datasheets/mfrg.pdf', 'tags': 'ptc resettable fuse polyfuse THT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_Bourns_MF-RG400.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuse_Bourns_MF-RG400')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

