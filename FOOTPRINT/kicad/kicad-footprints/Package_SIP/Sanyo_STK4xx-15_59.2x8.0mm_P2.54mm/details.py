
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Package_SIP"
    oIndex = "Sanyo_STK4xx-15_59.2x8.0mm_P2.54mm"
    hexID = "FZKSIPSANYOSTK4XX15592X8P254"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Sanyo_STK4xx-15_59.2x8.0mm_P2.54mm', 'description': 'Sanyo SIP-15, 59.2mm x 8.0mm bosy size, STK-433E STK-435E STK-436E (http://datasheet.octopart.com/STK430-Sanyo-datasheet-107060.pdf)', 'tags': 'Sanyo SIP-15', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Package_SIP.3dshapes/Sanyo_STK4xx-15_59.2x8.0mm_P2.54mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Package_SIP : Sanyo_STK4xx-15_59.2x8.0mm_P2.54mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

