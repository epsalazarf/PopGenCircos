# SNP Counts Plot
# By: Pavel Salazar
# Description: Takes the output of SNPCounter.py and plots the density of SNP per MB while ignoring the heterochromatin regions.

#<START>
options(scipen = 999)
library(scales)
#<INPUT>
setwd("PATH")
snps <- read.table(input_file,stringsAsFactors = F)
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


#<SANDBOX>
aggregate(data_pvar$COUNT, by = as.list(data_pvar$CHROM), FUN = sum)

chromsums <- aggregate(COUNT ~ CHROM, data_pvar, sum)
chromsums$CHROM <- as.factor(chromsums$CHROM)

ggplot(chromsums, aes(x = CHROM, y = COUNT, fill = CHROM)) +
  geom_bar(stat="identity") +
  scale_x_discrete(labels = c(1:22,"X","Y")) +
  scale_y_continuous(labels = label_number(suffix = " K", scale = 1e-3)) +
  geom_text(aes(label = scales::comma(COUNT)), hjust = "right",  angle = 90, position = position_dodge(0.9), size = 3) +
  theme_linedraw() +
  theme(legend.position = "none", axis.title.x = element_blank(), axis.title.y = element_blank())
