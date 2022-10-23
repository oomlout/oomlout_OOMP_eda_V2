
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Button_Switch_THT"
    oIndex = "SW_MEC_5GTH9"
    hexID = "FZKBSWMEC5GTH9"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'SW_MEC_5GTH9', 'description': 'MEC 5G single pole normally-open tactile switch https://cdn.sos.sk/productdata/80/f6/aabf7be6/5gth9358222.pdf', 'tags': 'switch normally-open pushbutton push-button', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Button_Switch_THT.3dshapes/SW_MEC_5GTH9.wrl', 'pins': {'type': 'thru_hole', 'shape': 'circle'}})
    newPart['name'].append('Button_Switch_THT : SW_MEC_5GTH9')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

