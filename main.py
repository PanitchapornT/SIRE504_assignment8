# from SeqCal import gcContent, atContent, countBasesDict
# from SeqPattern import cpgSearch, enzTargetsScan
# from SeqMan import reverseComplementSeq, dna2rna, dna2protein

from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.SeqMan import *

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    subparsers.required = True

    # SeqCal
    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    atc_command = subparsers.add_parser('atContent', help='Calculate AT content')
    atc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")    

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")

    # SeqMan
    transcription_command = subparsers.add_parser('transcription', help='Convert DNA->RNA')
    transcription_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    transcription_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")

    translation_command = subparsers.add_parser('translation', help='Convert DNA->Protein')
    translation_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    translation_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")

    # SeqPattern
    cpg_command = subparsers.add_parser('cpgSearch', help='Find CpG position')
    cpg_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    cpg_command.add_argument("-r", "--revcomp", action="store_true",
                             help="Convet DNA to reverse-complementary")
     
    enz_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enz_command.add_argument("-s", "--seq", type=str, default=None,
                                help="Provide sequence")
    enz_command.add_argument("-e", "--enz", type=str, default='EcoRI',
                                    help="Enzyme name: EcoRI, BamHI, HindIII, AccB2I, AasI, AceI (default: EcoRI)")
    enz_command.add_argument("-r", "--revcomp", action="store_true",
                                 help="Convet DNA to reverse-complementary")

    # parser.print_help()
    return parser

def test():
    # Input
    parser = argparserLocal()
    args = parser.parse_args(["cpgScan","-s","ATCGCT"])
    print("Input",args.seq,"\ncpgScan =", cpgSearch(args.seq) )    
    
def main():
    parser = argparserLocal()
    args = parser.parse_args()

    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
    # Input
    # seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'

    if args.command == 'gcContent':
        if args.seq == None:
            exit(parser.parse_args(['gcContent','-h']))
        print("Input",args.seq,"\nGC content =", gcContent(seq) )

    elif args.command == 'atContent':
        if args.seq == None:
            exit(parser.parse_args(['atContent','-h']))
        print("Input",args.seq,"\nAT content =", atContent(seq) )

    elif args.command == 'countBases':
        if args.seq == None:
            exit(parser.parse_args(['countBases','-h']))
        else:
            if args.revcomp:
                revcomp_seq = reverseComplementSeq(seq)
                print("Input",args.seq,"\ncountBases =", countBasesDict(revcomp_seq) )
            else:
                print("Input",args.seq,"\ncountBases =", countBasesDict(seq) )

    elif args.command == 'transcription':
        if args.seq == None:
            exit(parser.parse_args(['transcription','-h']))
        else:
            if args.revcomp:
                revcomp_seq = reverseComplementSeq(seq)
                print("Input",args.seq,"\nTranscription =", dna2rna(revcomp_seq) )
            else:
                print("Input",args.seq,"\nTranscription =", dna2rna(seq) )    

    elif args.command == 'translation':
        if args.seq == None:
            exit(parser.parse_args(['translation','-h']))
        else:
            if args.revcomp:
                revcomp_seq = reverseComplementSeq(seq)
                print("Input",args.seq,"\nTranslation =", dna2protein(revcomp_seq) )
            else:
                print("Input",args.seq,"\nTranslation =", dna2protein(seq) )  

    elif args.command == 'cpgSearch':
        if args.seq == None:
            exit(parser.parse_args(['cpgSearch','-h']))
        else:
            if args.revcomp:
                revcomp_seq = reverseComplementSeq(seq)
                print("Input",args.seq,"\nCpG position =", cpgSearch(revcomp_seq) )
            else:
                print("Input",args.seq,"\nCpG position =", cpgSearch(seq) )  
    
    elif args.command == 'enzTargetsScan':
        if args.seq == None:
            exit(parser.parse_args(['enzTargetsScan','-h']))
        else:
            if args.revcomp:
                revcomp_seq = reverseComplementSeq(seq)
                print(f"Input",args.seq,f"\n{args.enz} sites =", enzTargetsScan(revcomp_seq, args.enz) )
                # print("Input",args.seq,"\nTranslation =", enzTargetsScan(revcomp_seq) )
            else:
                print(f"Input",args.seq,f"\n{args.enz} sites =", enzTargetsScan(seq, args.enz) ) 

# print(__name__)
if __name__ == "__main__":
    # test()
    main()

