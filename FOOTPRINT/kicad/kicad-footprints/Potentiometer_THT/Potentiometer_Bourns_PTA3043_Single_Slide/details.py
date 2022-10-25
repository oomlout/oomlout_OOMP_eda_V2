
######  Auto translated oomp file

def load(newPart,it):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Potentiometer_THT"
    oIndex = "Potentiometer_Bourns_PTA3043_Single_Slide"
    hexID = "FZKPPOTENTIOMETERBOURNSPTA343SINGLESLIDE"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Potentiometer_Bourns_PTA3043_Single_Slide', 'description': 'Bourns single-gang slide potentiometer, 30.0mm travel, https://www.bourns.com/docs/Product-Datasheets/pta.pdf', 'tags': 'Bourns single-gang slide potentiometer 30.0mm', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Potentiometer_THT.3dshapes/Potentiometer_Bourns_PTA3043_Single_Slide.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Potentiometer_THT : Potentiometer_Bourns_PTA3043_Single_Slide')


    ######  Common
    newPart['hexID'].append(hexID)

    return newPart

