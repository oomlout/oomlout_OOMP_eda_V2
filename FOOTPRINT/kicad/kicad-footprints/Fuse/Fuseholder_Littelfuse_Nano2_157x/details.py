
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Fuse"
    oIndex = "Fuseholder_Littelfuse_Nano2_157x"
    hexID = "FZKFUFUHOLDERLITTELFUNANO2157X"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fuseholder_Littelfuse_Nano2_157x', 'description': 'Littelfuse NANO2 holder, https://www.littelfuse.com/~/media/electronics/datasheets/fuses/littelfuse_fuse_157_datasheet.pdf.pdf', 'tags': 'SMD Nano2 holder', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Fuse.3dshapes/Fuseholder_Littelfuse_Nano2_157x.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Fuse : Fuseholder_Littelfuse_Nano2_157x')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

