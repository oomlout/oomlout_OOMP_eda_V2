
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "LFBGA-100_10x10mm_Layout10x10_P0.8mm"
    hexID = "FZKBGALFBGA11X1LAYOUT1X1P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'LFBGA-100_10x10mm_Layout10x10_P0.8mm', 'description': 'LFBGA-100, 10x10 raster, 10x10mm package, pitch 0.8mm; see section 6.3 of http://www.st.com/resource/en/datasheet/stm32f103tb.pdf', 'tags': 'BGA 100 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/LFBGA-100_10x10mm_Layout10x10_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : LFBGA-100_10x10mm_Layout10x10_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

