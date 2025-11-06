def Write_list2(list,outputfilename):
    outputfile=open(outputfilename,'w')
    for rec in list:
        for i in range(0,len(rec)-1):
            outputfile.write(str(rec[i])+'\t')
        outputfile.write(str(rec[len(rec)-1])+'\n')


def Count_target_mutation(inputdata,targetinfo,minimumtagcount,outputfilename,mode="target"):

    delimiter2 = "GTACTCGCAGTAGTC"
    tmplist2 = [(x[0][:9] + x[0][x[0].find(delimiter2)-9:x[0].find(delimiter2)], x[0][x[0].find(delimiter2):], x[1]) for x in inputdata if delimiter2 in x[0]] 
    if mode=="target":
        primerlist=[x[0] for x in targetinfo]
        targetlist=[x[1] for x in targetinfo]
    else:
        primer1=[x[0] for x in targetinfo]
        primer2=[x[1] for x in targetinfo]
        primerlist=[x[0] for x in targetinfo]
        targetlist=primerlist
    outlist=[]
    tmpcount=0
    targetcountlist=[['BC','count']+targetlist]
    
    for i in range(0,len(tmplist2)-1):
        tmpBC=tmplist2[i][0]
        if tmpBC==tmplist2[i+1][0]:
            tmpcount=tmpcount+1
        else:
            tmpcount=tmpcount+1
            if tmpcount>minimumtagcount:
                print(str(tmpcount)+'\t'+tmpBC)
                tmpPcountlist=[tmpBC,tmpcount]
                for j in range(0,len(primerlist)): 
                    if mode=="target":
                        primer=targetinfo[j][0];start=int(targetinfo[j][2]);end=int(targetinfo[j][3]);target=targetinfo[j][1]
                        tmplist3=tmplist2[i-tmpcount+1:i]
                        outlist=[x[2][start:end] for x in tmplist3 if primer in x[2]]
                        tmpPcountlist.append(outlist.count(target))
                    else:
                        tmplist3=tmplist2[i-tmpcount+1:i]
                        primerF=primer1[j]
                        primerR = primer2[j]
                        outlist = []
                        for x in tmplist3:
                            if primerF in x[1]:
                                if primerR in x[2]:
                                    outlist.append(x) 
                        tmpPcountlist.append(len(outlist))
                targetcountlist.append(tmpPcountlist)
            tmpcount=0
    
    Write_list2(targetcountlist,outputfilename)
