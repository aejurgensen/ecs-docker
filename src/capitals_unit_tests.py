import capitals as caps


def test_get_fuzzy_string_match():
    expected = "Alabama"
    actual = caps.get_fuzzy_match("alama", ["AL", "Califonria", "Alaska", "Arkansas", "Alabama"], 3)
    assert expected == actual

def test_match_search():
    expected = "California"
    actual = caps.match_search_string("califor")
    assert expected == actual


def test_match_search_abbrev():
    expected = "New Mexico"
    actual = caps.match_search_string("new m")
    assert expected == actual


def test_get_name():
    expected = "New Jersey (NJ)"
    actual = caps.get_name(caps.get_state("NJ"))
    assert expected == actual


def test_get_capital():
    expected = "Denver"
    actual = caps.get_capital(caps.get_state("Colorado"))
    assert expected == actual


def test_get_statehood_state():
    expected = "gained statehood in 1959"
    actual = caps.get_statehood(caps.get_state("Alaska"))
    assert expected == actual


def test_get_statehood_territory():
    expected = "US territory"
    actual = caps.get_statehood(caps.get_state("Guam"))
    assert expected == actual


def test_get_statehood_obsolete():
    expected = "obsolete entity"
    actual = caps.get_statehood(caps.get_state("Orleans"))
    assert expected == actual


def test_get_timezones_single():
    expected = "America/Los_Angeles"
    actual = caps.get_timezones(caps.get_state("WA"))
    assert expected == actual


def test_get_timezones_multi():
    expected = "America/Chicago, America/Denver"
    actual = caps.get_timezones(caps.get_state("Kansas"))
    assert expected == actual