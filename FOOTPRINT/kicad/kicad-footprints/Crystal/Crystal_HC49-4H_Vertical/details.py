
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_HC49-4H_Vertical"
    hexID = "FZKXXHC494HVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_HC49-4H_Vertical', 'description': 'Crystal THT HC-49-4H http://5hertz.com/pdfs/04404_D.pdf', 'tags': 'THT crystalHC-49-4H', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_HC49-4H_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Crystal_HC49-4H_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

