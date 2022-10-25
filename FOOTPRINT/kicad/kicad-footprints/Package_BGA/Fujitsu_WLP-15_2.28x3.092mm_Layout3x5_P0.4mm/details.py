
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm"
    hexID = "FZKBGAFUJITSUWLP15228X392LAYOUT3X5P4"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm', 'description': 'WLP-15, 3x5 raster, 2.28x3.092mm package, pitch 0.4mm; http://www.fujitsu.com/global/documents/products/devices/semiconductor/fram/lineup/MB85RS1MT-DS501-00022-7v0-E.pdf', 'tags': 'BGA 8 0.4', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : Fujitsu_WLP-15_2.28x3.092mm_Layout3x5_P0.4mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

