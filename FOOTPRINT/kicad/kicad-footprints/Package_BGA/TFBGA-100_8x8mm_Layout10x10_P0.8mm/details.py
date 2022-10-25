
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "TFBGA-100_8x8mm_Layout10x10_P0.8mm"
    hexID = "FZKBGATFBGA18X8LAYOUT1X1P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TFBGA-100_8x8mm_Layout10x10_P0.8mm', 'description': 'TFBGA-100, 10x10 raster, 8x8mm package, pitch 0.8mm; see section 6.2 of http://www.st.com/resource/en/datasheet/stm32f746zg.pdf', 'tags': 'BGA 100 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/TFBGA-100_8x8mm_Layout10x10_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : TFBGA-100_8x8mm_Layout10x10_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

