# SNP Counts Plot
# By: Pavel Salazar
# Description: Takes the output of SNPCounter.py and plots the density of SNP per MB while ignoring the heterochromatin regions.

#<START>

#<INPUT>
setwd("PATH")
snps <- read.table("FILE.snpcounts.txt",stringsAsFactors = F)
hetc <- read.table("chr.hetero.highlights.txt",stringsAsFactors = F)
#</INPUT>

#<PROCESSING>
hetc[,3] <- hetc[,3]-1

for (r in 1:dim(snps)[1]){
  chr <- snps[r,1]
  if(any(snps[r,2] >= hetc[hetc[,1] == chr,2]) & all(snps[r,3] <= hetc[hetc[,1] == chr,3])){
    snps[r,4] <- NA
  }
}

counts <- as.vector(snps[,4])
summary(counts)
counts[counts > 40] <- 40
counts <- na.omit(counts)
#</PROCESSING>

#<OUTPUT>
plot(table(counts), type = "h", col = "#FC4349", lwd = 7, xlab = NA, ylab = NA, main ="SNPs per MB", bty="n")
abline(v = mean(counts), col="#218BC9")
#</OUTPUT>

#<END>
