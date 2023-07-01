import camelot

pdf = camelot.read_pdf('./crash_and_claims_reports/2014-Crash-and-Claims-Report.pdf')
table = print(pdf[2].df)