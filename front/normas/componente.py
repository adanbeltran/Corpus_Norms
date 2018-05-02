class TagNorm:

    def __init__(self):
        '''

        '''


    def tag_Norm( self, text, setTags):
        textTagged= []
        for tag in setTags:
            nameTagger= tag[0]
            # aca llamara al  metodo NameTagger correspondiente
            textTagged.append(nameTagger)
            i=4
            for nameTag in tag[1]:
                textTagged.append([nameTag,text[0:i]])
                i+=4
        return textTagged


setTags=[['SP0',["Object","Subject","Predicate"] ], ['AHOHFELD',["RIGHT[]", "DUTY[]","PRIVILEGE[]" ]]]
oTagNorm= TagNorm.tag_Norm('', "la casa en el lago",setTags)
print(oTagNorm)
#for tag in oTagNorm:
#    print(tag)