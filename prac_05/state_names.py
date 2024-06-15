"""
CP1404/CP5632 Practical
State names in a dictionary
File needs reformatting
"""

CODE_TO_NAME = {"QLD": "Queensland", "NSW": "New South Wales", "NT": "Northern Territory", "WA": "Western Australia",
                "ACT": "Australian Capital Territory", "VIC": "Victoria", "TAS": "Tasmania"}
print(CODE_TO_NAME)

state_codes = []
state_code = input("Enter short state: ").upper()
while state_code != "":
    if state_code in CODE_TO_NAME:
        print(state_code, "is", CODE_TO_NAME[state_code])
        state_codes.append(state_code)
    else:
        print("Invalid short state")
    state_code = input("Enter short state: ").upper()

abbreviation_width = max(len(state_code) for state_code in state_codes)
[print(f"{state_code:{abbreviation_width}} is {CODE_TO_NAME[state_code]}") for state_code in state_codes]
