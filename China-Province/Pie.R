get_Var<-read.csv(file="C:/HanryGIS/China-Province/Variables.csv",header=T,sep=",")
sum=0
count=0
good=0
for(i in 1:33){
  sum=sum+get_Var$X4[i]
  count=count+1
  if(!is.na(get_Var$X4[i])){
    good=good+1
  }
}
if((good/count)<0.5){
  for(i in 1:33){
    if(!is.na(get_Var$X4[i])){
    setwd("c://HanryGIS//China-Province//Muity//")
    pie(c(sum,get_Var$X4[i]),label="")
    png(file=paste("mui",as.character(i),".png",sep=""),bg="transparent")
    pie(c(sum,get_Var$X4[i]),label="")
    dev.off()
    }
  }
}
if((good/count)>=0.5){
  a<-matrix(nrow=2,ncol=1)
  for(i in 1:33){
    a[1,1]=get_Var$X2[i]
    a[2,1]=get_Var$X3[i]
    setwd("c://HanryGIS//China-Province//Muity//")
    barplot(a,beside=T,axes=F,ylim=c(0,1))
    png(file=paste("mui",as.character(i),".png",sep=""),bg="transparent")
    barplot(a,beside=T,axes=F,ylim=c(0,1))
    dev.off()
  }
}