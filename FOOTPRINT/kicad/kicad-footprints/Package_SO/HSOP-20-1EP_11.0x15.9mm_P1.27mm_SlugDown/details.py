
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HSOP-20-1EP_11.0x15.9mm_P1.27mm_SlugDown"
    hexID = "FZKSOHS21EP11X159P127SLUGDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HSOP-20-1EP_11.0x15.9mm_P1.27mm_SlugDown', 'description': 'HSOP 11.0x15.9mm Pitch 1.27mm Slug Down (PowerSO-20) [JEDEC MO-166] (http://www.st.com/resource/en/datasheet/tda7266d.pdf, www.st.com/resource/en/application_note/cd00003801.pdf)', 'tags': 'HSOP 11.0 x 15.9mm Pitch 1.27mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HSOP-20-1EP_11.0x15.9mm_P1.27mm_SlugDown.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : HSOP-20-1EP_11.0x15.9mm_P1.27mm_SlugDown')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

