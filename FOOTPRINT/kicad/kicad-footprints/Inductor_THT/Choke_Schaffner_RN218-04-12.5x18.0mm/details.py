
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Inductor_THT"
    oIndex = "Choke_Schaffner_RN218-04-12.5x18.0mm"
    hexID = "FZKINCHOKESCHAFFNERRN2184125X18"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Choke_Schaffner_RN218-04-12.5x18.0mm', 'description': 'Current-compensated Chokes, Schaffner, RN218-04, 12.5mmx18.0mm https://www.schaffner.com/products/download/product/datasheet/rn-series-common-mode-chokes-new/', 'tags': 'chokes schaffner tht', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Inductor_THT.3dshapes/Choke_Schaffner_RN218-04-12.5x18.0mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Inductor_THT : Choke_Schaffner_RN218-04-12.5x18.0mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

