# Author: mdavis2@scu.edu
# Last updated: 2020-04-26
# Context: Latest US-State ISO codes from https://en.wikipedia.org/wiki/ISO_3166-2:US 

us_state_iso_codes = {
    'US-AL': {'name': 'Alabama', 'classification': 'state'},
    'US-AK': {'name': 'Alaska', 'classification': 'state'},
    'US-AZ': {'name': 'Arizona', 'classification': 'state'},
    'US-AR': {'name': 'Arkansas', 'classification': 'state'},
    'US-CA': {'name': 'California', 'classification': 'state'},
    'US-CO': {'name': 'Colorado', 'classification': 'state'},
    'US-CT': {'name': 'Connecticut', 'classification': 'state'},
    'US-DE': {'name': 'Delaware', 'classification': 'state'},
    'US-FL': {'name': 'Florida', 'classification': 'state'},
    'US-GA': {'name': 'Georgia', 'classification': 'state'},
    'US-HI': {'name': 'Hawaii', 'classification': 'state'},
    'US-ID': {'name': 'Idaho', 'classification': 'state'},
    'US-IL': {'name': 'Illinois', 'classification': 'state'},
    'US-IN': {'name': 'Indiana', 'classification': 'state'},
    'US-IA': {'name': 'Iowa', 'classification': 'state'},
    'US-KS': {'name': 'Kansas', 'classification': 'state'},
    'US-KY': {'name': 'Kentucky', 'classification': 'state'},
    'US-LA': {'name': 'Louisiana', 'classification': 'state'},
    'US-ME': {'name': 'Maine', 'classification': 'state'},
    'US-MD': {'name': 'Maryland', 'classification': 'state'},
    'US-MA': {'name': 'Massachusetts', 'classification': 'state'},
    'US-MI': {'name': 'Michigan', 'classification': 'state'},
    'US-MN': {'name': 'Minnesota', 'classification': 'state'},
    'US-MS': {'name': 'Mississippi', 'classification': 'state'},
    'US-MO': {'name': 'Missouri', 'classification': 'state'},
    'US-MT': {'name': 'Montana', 'classification': 'state'},
    'US-NE': {'name': 'Nebraska', 'classification': 'state'},
    'US-NV': {'name': 'Nevada', 'classification': 'state'},
    'US-NH': {'name': 'New Hampshire', 'classification': 'state'},
    'US-NJ': {'name': 'New Jersey', 'classification': 'state'},
    'US-NM': {'name': 'New Mexico', 'classification': 'state'},
    'US-NY': {'name': 'New York', 'classification': 'state'},
    'US-NC': {'name': 'North Carolina', 'classification': 'state'},
    'US-ND': {'name': 'North Dakota', 'classification': 'state'},
    'US-OH': {'name': 'Ohio', 'classification': 'state'},
    'US-OK': {'name': 'Oklahoma', 'classification': 'state'},
    'US-OR': {'name': 'Oregon', 'classification': 'state'},
    'US-PA': {'name': 'Pennsylvania', 'classification': 'state'},
    'US-RI': {'name': 'Rhode Island', 'classification': 'state'},
    'US-SC': {'name': 'South Carolina', 'classification': 'state'},
    'US-SD': {'name': 'South Dakota', 'classification': 'state'},
    'US-TN': {'name': 'Tennessee', 'classification': 'state'},
    'US-TX': {'name': 'Texas', 'classification': 'state'},
    'US-UT': {'name': 'Utah', 'classification': 'state'},
    'US-VT': {'name': 'Vermont', 'classification': 'state'},
    'US-VA': {'name': 'Virginia', 'classification': 'state'},
    'US-WA': {'name': 'Washington', 'classification': 'state'},
    'US-WV': {'name': 'West Virginia', 'classification': 'state'},
    'US-WI': {'name': 'Wisconsin', 'classification': 'state'},
    'US-WY': {'name': 'Wyoming', 'classification': 'state'},
    'US-DC': {'name': 'District of Columbia', 'classification': 'district'},
    'US-AS': {'name': 'American Samoa', 'classification': 'outlying area'},
    'US-GU': {'name': 'Guam', 'classification': 'outlying area'},
    'US-MP': {'name': 'Northern Mariana Islands', 'classification': 'outlying area'},
    'US-PR': {'name': 'Puerto Rico', 'classification': 'outlying area'},
    'US-UM': {'name': 'United States Minor Outlying Islands', 'classification': 'outlying area'},
    'US-VI': {'name': 'Virgin Islands, U.S.', 'classification': 'outlying area'}
}

if __name__ == '__main__':
    print(f"Number of US state/territories: {len(us_state_iso_codes)}")
    example_state = list(us_state_iso_codes.keys())[0]
    example_data = us_state_iso_codes[example_state]
    print(f"Example entry: '{example_state}': {example_data}")
