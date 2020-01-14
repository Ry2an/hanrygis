get_var<-read.csv(file="C:/HanryGIS/China-Province/Variables.csv",header=T,sep=",")
a<-matrix(nrow=2,ncol=1)
for(i in 1:33){
  a[1,1]=get_var$X2[i]
  a[2,1]=get_var$X3[i]
  setwd("c://HanryGIS//China-Province//bar//")
  barplot(a,beside=T,axes=F,ylim=c(0,1))
  png(file=paste("mui",as.character(i),".png",sep=""),bg="transparent")
  barplot(a,beside=T,axes=F,ylim=c(0,1))
  dev.off()
}