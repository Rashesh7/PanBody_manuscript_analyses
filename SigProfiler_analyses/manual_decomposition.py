#!/usr/bin/env python

import sys, argparse
from SigProfilerExtractor import decomposition as decomp

#Testing 6 de-novo signature solution
signatures = "./All_Matched_output_v1.015-gpu/SBS96/All_Solutions/SBS96_6_Signatures/Signatures/SBS96_S6_Signatures.txt"
activities="./All_Matched_output_v1.015-gpu/SBS96/All_Solutions/SBS96_6_Signatures/Activities/SBS96_S6_NMF_Activities.txt"
samples="./All_Matched_output_v1.015-gpu/SBS96/Samples.txt"
output="./All_Matched_output_v1.015-gpu/SBS96/Suggested_Solution_6-COSMICv3.1"

if __name__=="__main__":
	decomp.decompose(signatures, activities, samples, output, genome_build="GRCh37", verbose=True)


#Testing 4 de-novo signature solution
signatures = "./All_Matched_output_v1.015-gpu/SBS96/All_Solutions/SBS96_4_Signatures/Signatures/SBS96_S4_Signatures.txt"
activities="./All_Matched_output_v1.015-gpu/SBS96/All_Solutions/SBS96_4_Signatures/Activities/SBS96_S4_NMF_Activities.txt"
samples="./All_Matched_output_v1.015-gpu/SBS96/Samples.txt"
output="./All_Matched_output_v1.015-gpu/SBS96/Suggested_Solution_4-COSMICv3.1"

if __name__=="__main__":
	decomp.decompose(signatures, activities, samples, output, genome_build="GRCh37", verbose=True)

#Testing 5 de-novo signature solution
signatures = "./All_Matched_output_v1.015-gpu/SBS96/All_Solutions/SBS96_5_Signatures/Signatures/SBS96_S5_Signatures.txt"
activities="./All_Matched_output_v1.015-gpu/SBS96/All_Solutions/SBS96_5_Signatures/Activities/SBS96_S5_NMF_Activities.txt"
samples="./All_Matched_output_v1.015-gpu/SBS96/Samples.txt"
output="./All_Matched_output_v1.015-gpu/SBS96/Suggested_Solution_5-COSMICv3.1"

if __name__=="__main__":
	decomp.decompose(signatures, activities, samples, output, genome_build="GRCh37", verbose=True)
