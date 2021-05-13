import us
from fuzzywuzzy import process

global names_and_metaphones
global abbreviations

names_and_metaphones = []
abbreviations = []

# add state name and state abbreviations to list of potential
# search strings to use for fuzzy string matching
for state in us.states.STATES_AND_TERRITORIES:
    abbreviations.append(state.abbr)
    names_and_metaphones.append(state.name)
    names_and_metaphones.append(state.name_metaphone)

# add state name and abbreviations to list for obsolete entities
for state in us.states.OBSOLETE:
    abbreviations.append(state.abbr)
    names_and_metaphones.append(state.name)
    names_and_metaphones.append(state.name_metaphone)


# returns list of abbrevations created
def get_all_abbrevations():
    return abbreviations


# returns list of names and metaphones created
def get_all_names_and_metaphones():
    return names_and_metaphones


def get_fuzzy_match(search_string, lookup_set, ngram_len):
    match_results = process.extractOne(search_string, lookup_set)
    matched_name = match_results[0]
    return matched_name

# fuzzy-matches a search string to state/territory abbreviations,
# metaphones, and abbreviations
def match_search_string(search_string):
    lookup_set = abbreviations if len(search_string) < 4 else names_and_metaphones
    ngram_len = 1 if len(search_string) < 4 else 2

    if len(search_string) == 2 and search_string in abbreviations:
        matched_name = search_string
    else:
        matched_name = get_fuzzy_match(search_string, lookup_set, ngram_len)

    return matched_name

# returns a formatted text version of full name and abbreviation
# of given state. sTate should be a state object from package us
def get_name(state):
    return state.name + " (" + state.abbr + ")"


# returns a formatted text version of statehood info for given state
# state should be a state object from package us
def get_statehood(state):
    if state.is_territory:
        statehood = "US territory"
    elif state.is_obsolete:
        statehood = "obsolete entity"
    else:
        statehood = "gained statehood in " + str(state.statehood_year)  
        
    return statehood


# returns a formatted text version of state's capital
# state should be a state object from package us
def get_capital(state):
    return state.capital if not state.is_obsolete else "N/A"


# returns a formatted text version of state's timezones
# state should be a state object from package us
def get_timezones(state):
    return ", ".join(state.time_zones)


# given a state name or abbreviation that exists in either list
# names_and_metaphones or abbrevations, returns the state object
# for the given name
def get_state(state_name_or_abbrev):
    return us.states.lookup(state_name_or_abbrev)


# fuzzy-matches a state name or abbreviation and returns a 
# formatted, multi-line string with the matched state's info
def get_state_info(state_name_or_abbrev):
    state = get_state(state_name_or_abbrev)

    state_info = {"name":get_name(state),
                  "capital":get_capital(state),
                  "statehood":get_statehood(state), 
                  "timezones":get_timezones(state)}
    
    return state_info


def get_safe_state_info(search_string):
    state_name = match_search_string(search_string)

    return get_state_info(state_name)