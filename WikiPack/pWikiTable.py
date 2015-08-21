import argparse
import wTable

parser = argparse.ArgumentParser(description="Turns a CSV or TSV into a wiki-Format Table, or Vice Versa",
                                 prog="python Wiki Table")
group = parser.add_mutually_exclusive_group(required=False)
group.add_argument("--tsv", help="force to tab separated parsing", action='store_const', const='True')
group.add_argument("--csv", help="force to comma separated parsing", action='store_const', const='True')

wikiparser = wTable.parseIntoWiki()

args = parser.parse_args()

if args.tsv:
    wikiparser.parseTSVFromClip()
elif args.csv:
    wikiparser.parseCSVFromClip()
else:
    wikiparser.parseTSVFromClip()




