
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Connector_Dsub"
    oIndex = "DSUB-15_Female_EdgeMount_P2.77mm"
    hexID = "FZKCNDSUBDSUB15FEMALEEDGEMOUNTP277"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'DSUB-15_Female_EdgeMount_P2.77mm', 'description': '15-pin D-Sub connector, solder-cups edge-mounted, female, x-pin-pitch 2.77mm, distance of mounting holes 33.3mm, see https://disti-assets.s3.amazonaws.com/tonar/files/datasheets/16730.pdf', 'tags': '15-pin D-Sub connector edge mount solder cup female x-pin-pitch 2.77mm mounting holes distance 33.3mm', 'attributeType': 'smd', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Connector_Dsub.3dshapes/DSUB-15_Female_EdgeMount_P2.77mm.wrl', 'pins': {'type': 'smd', 'shape': 'rect'}})
    newPart['name'].append('Connector_Dsub : DSUB-15_Female_EdgeMount_P2.77mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

