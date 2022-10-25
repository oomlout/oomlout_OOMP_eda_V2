
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuse_Bourns_MF-RHT1300"
    hexID = "FZKFUFUBOURNSMFRHT13"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuse_Bourns_MF-RHT1300', 'description': 'PTC Resettable Fuse, Ihold = 13.0A, Itrip=24.0A, http://www.bourns.com/docs/product-datasheets/mfrht.pdf', 'tags': 'ptc resettable fuse polyfuse THT', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuse_Bourns_MF-RHT1300.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Fuse : Fuse_Bourns_MF-RHT1300')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

