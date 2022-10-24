
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SO"
    oIndex = "HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugDown"
    hexID = "FZKSOHS361EP11X159P65SLUGDOWN"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugDown', 'description': 'HSOP 11.0x15.9mm Pitch 0.65mm Slug Down (PowerSO-36) [JEDEC MO-166] (http://www.st.com/resource/en/datasheet/vn808cm-32-e.pdf, http://www.st.com/resource/en/application_note/cd00003801.pdf)', 'tags': 'HSOP 11.0 x 15.9mm Pitch 0.65mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SO.3dshapes/HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugDown.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Package_SO : HSOP-36-1EP_11.0x15.9mm_P0.65mm_SlugDown')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

