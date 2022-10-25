
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_QFP"
    oIndex = "PQFP-132_24x24mm_P0.635mm_i386"
    hexID = "FZKQFPPQFP13224X24P635I386"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'PQFP-132_24x24mm_P0.635mm_i386', 'description': 'PQFP, 132 pins, 24mm sq body, 0.635mm pitch, Intel 386EX (https://www.intel.com/content/dam/www/public/us/en/documents/packaging-databooks/packaging-chapter-02-databook.pdf, http://www.nxp.com/docs/en/application-note/AN4388.pdf)', 'tags': 'PQFP 132 Intel 386EX', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_QFP.3dshapes/PQFP-132_24x24mm_P0.635mm_i386.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_QFP : PQFP-132_24x24mm_P0.635mm_i386')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

