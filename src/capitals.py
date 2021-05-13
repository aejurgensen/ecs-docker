import us
import tfidf_matcher as tm 

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


# returns list of abbrevations created
def get_all_abbrevations():
    return abbreviations


# returns list of names and metaphones created
def get_all_names_and_metaphones():
    return names_and_metaphones


# fuzzy-matches a search string to state/territory abbreviations,
# metaphones, and abbreviations
def match_search_string(search_string):
    lookup_set = abbreviations if len(search_string) < 3 else names_and_metaphones
    ngram_len = 1 if len(search_string) < 3 else 2
    
    match_results = tm.matcher(original=[search_string], 
                      lookup=lookup_set, 
                      k_matches=1, 
                      ngram_length=ngram_len)
    matched_name = match_results.lookup([0], ["Lookup 1"])[0]
    return matched_name


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
    return  state.capital if not state.is_obsolete else "N/A"


# returns a formatted text version of state's timezones
# state should be a state object from package us
def get_timezones(state):
    return ", ".join(state.time_zones)


# fuzzy-matches a state name or abbreviation and returns a 
# formatted, multi-line string with the matched state's info
def get_state_info(state_name_or_abbrev):
    state = us.states.lookup(state_name_or_abbrev)
    
    info_string = state.name + " (" + state.abbr + ")<br/>"
    info_string += "capital: " + get_capital(state) + "<br/>"    
    info_string += "statehood: " + get_statehood(state) + "<br/>"
    info_string += "time zones: " + get_timezones(state)
    
    return info_string