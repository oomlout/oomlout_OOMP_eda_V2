
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "TFBGA-216_13x13mm_Layout15x15_P0.8mm"
    hexID = "FZKBGATFBGA21613X13LAYOUT15X15P8"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'TFBGA-216_13x13mm_Layout15x15_P0.8mm', 'description': 'TFBGA-216, 15x15 raster, 13x13mm package, pitch 0.8mm; see section 6.8 of http://www.st.com/resource/en/datasheet/stm32f746zg.pdf', 'tags': 'BGA 216 0.8', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/TFBGA-216_13x13mm_Layout15x15_P0.8mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : TFBGA-216_13x13mm_Layout15x15_P0.8mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

