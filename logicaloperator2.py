#if applicant has high income AND good credit, eligible for loan
has_high_income = True
has_good_credit = True
has_criminal_record = False

if has_high_income and has_good_credit:
    print("Eligible for loan")

else:
    print("Ineligible for loan")

#if applicant has high income OR good credit, eligible for loan

if has_high_income or has_good_credit :
    print("Eligible for loan")

else:
    print("Ineligible for loan")

#if applicant has good credit and has no criminal record, eligible for loan

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Ineligible for loan")

#if applicant has high income and has good credit and has no criminal record, eligible for loan

if has_high_income and has_good_credit and not has_criminal_record:
    print("Eligible for loan")

else:
    print("Ineligible for loan")