
######  Auto translated oomp file

def load(newPart):
    oType = "FOOTPRINT"
    oSize = "kicad"
    oColor = "kicad-footprints"
    oDesc = "Diode_THT"
    oIndex = "Diode_Bridge_28.6x28.6x7.3mm_P18.0mm_P11.6mm"
    hexID = "FZKDDIODEBRIDGE286X286X73P18P116"

    newPart['oompType'].append(oType)
    newPart['oompSize'].append(oSize)
    newPart['oompColor'].append(oColor)
    newPart['oompDesc'].append(oDesc)
    newPart['oompIndex'].append(oIndex)
    oompID = oType + "-" + oSize + "-" + oColor + "-" + oDesc + "-" + oIndex 
    newPart['oompID'].append(oompID)

    newPart['footprintKicadDetails'].append({'name': 'Diode_Bridge_28.6x28.6x7.3mm_P18.0mm_P11.6mm', 'description': 'Single phase bridge rectifier case 28.6x28.6mm, pitch 18.0mm & 11.6mm, see https://diotec.com/tl_files/diotec/files/pdf/datasheets/kbpc1500fw.pdf', 'tags': 'Diode Bridge KBPCxxxxWP', 'attributeType': 'through_hole', 'threeDModel': '${KICAD6_3DMODEL_DIR}/Diode_THT.3dshapes/Diode_Bridge_28.6x28.6x7.3mm_P18.0mm_P11.6mm.wrl', 'pins': {'type': 'thru_hole', 'shape': 'rect'}})
    newPart['name'].append('Diode_THT : Diode_Bridge_28.6x28.6x7.3mm_P18.0mm_P11.6mm')


    ######  Common
    newPart['hexID'].append(hexID)

    ######  Housekeeping
    #OOMPtags.addTags(newPart,oompId)

    return newPart

