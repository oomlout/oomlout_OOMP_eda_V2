
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_BGA"
    oIndex = "ST_uTFBGA-36_3.6x3.6mm_Layout6x6_P0.5mm"
    hexID = "FZKBGASTUTFBGA3636X36LAYOUT6X6P5"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'ST_uTFBGA-36_3.6x3.6mm_Layout6x6_P0.5mm', 'description': 'ST uTFBGA-36, 0.25mm pad, 3.6x3.6mm, 36 Ball, 6x6 Layout, 0.5mm Pitch, https://www.st.com/resource/en/datasheet/stulpi01a.pdf', 'tags': 'BGA 36 0.5', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_BGA.3dshapes/ST_uTFBGA-36_3.6x3.6mm_Layout6x6_P0.5mm.wrl', 'pins': {'type': 'smd', 'shape': 'circle'}})
    newPart['name'].append('Package_BGA : ST_uTFBGA-36_3.6x3.6mm_Layout6x6_P0.5mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

