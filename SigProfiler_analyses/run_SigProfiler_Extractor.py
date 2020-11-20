#!/usr/bin/env python

import sys, argparse
from SigProfilerExtractor import sigpro as sig


parser = argparse.ArgumentParser()
parser.add_argument("input", help="input matrix file or folder contating vcf files")
parser.add_argument("-o", "--output", type=str, default="output_folder", help="output folder")
parser.add_argument("-d", "--data_type", type=str, default="vcf")
parser.add_argument("-r", "--reference", type=str, default="GRCh37")
args = parser.parse_args()
print(args)

if __name__=="__main__":
	sig.sigProfilerExtractor(args.data_type, args.output, args.input, cpu=8, minimum_signatures=2, maximum_signatures=20, gpu=True)
	

