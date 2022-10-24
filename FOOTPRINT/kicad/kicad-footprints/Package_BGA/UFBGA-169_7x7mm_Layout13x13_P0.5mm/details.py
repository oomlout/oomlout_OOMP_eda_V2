
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "UFBGA-169_7x7mm_Layout13x13_P0.5mm"
    hexID = "FZKBGAUFBGA1697X7LAYOUT13X13P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'UFBGA-169_7x7mm_Layout13x13_P0.5mm', 'description': 'UFBGA-169, 13x13 raster, 7x7mm package, pitch 0.5mm; see section 7.6 of http://www.st.com/resource/en/datasheet/stm32f429ng.pdf', 'tags': 'BGA 169 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/UFBGA-169_7x7mm_Layout13x13_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : UFBGA-169_7x7mm_Layout13x13_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

