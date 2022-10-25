
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Crystal"
    oIndex = "Crystal_HC49-U-3Pin_Vertical"
    hexID = "FZKXXHC49U3PINVERTICAL"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Crystal_HC49-U-3Pin_Vertical', 'description': 'Crystal THT HC-49/U, 3pin-version, http://www.raltron.com/products/pdfspecs/crystal_hc_49_45_51.pdf', 'tags': 'THT crystalHC-49/U', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Crystal.3dshapes/Crystal_HC49-U-3Pin_Vertical.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Crystal : Crystal_HC49-U-3Pin_Vertical')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

